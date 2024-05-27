import torch
from torchvision import transforms as T
from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
import argparse


class AgeEstimator:
    def __init__(self, face_size=64, weights=None, device='cpu', tpx=500):
        self.thickness_per_pixels = tpx
        if isinstance(face_size, int):
            self.face_size = (face_size, face_size)
        else:
            self.face_size = face_size

        self.device = torch.device(device if (device in ['cuda', 'gpu'] and torch.cuda.is_available()) else 'cpu')

        from Facenet.models.mtcnn import MTCNN
        self.facenet_model = MTCNN(device=self.device)

        from AgeNet.models import Model
        self.model = Model().to(self.device)
        self.model.eval()
        if weights:
            self.model.load_state_dict(torch.load(weights, map_location=self.device))
            print('Weights loaded successfully from path:', weights)
            print('====================================================')

    def transform(self, image):
        return T.Compose([
            T.Resize(self.face_size),
            T.ToTensor(),
            T.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
        ])(image)

 
    def predict(self, img, min_prob=0.9):
        if isinstance(img, Image.Image):
            image = img  # img is already a PIL image
        else:
            image = T.ToPILImage()(img.squeeze())  # Convert back to PIL if it's a tensor

        ndarray_image = np.array(image)
        image_shape = ndarray_image.shape

        bboxes, prob = self.facenet_model.detect(image)
        bboxes = bboxes[prob > min_prob]

        face_images = []
        for box in bboxes:
            box = np.clip(box, 0, np.inf).astype(np.uint32)
            padding = max(image_shape) * 5 / self.thickness_per_pixels
            padding = int(max(padding, 10))
            box = self.padding_face(box, padding)

            face = image.crop(box)
            transformed_face = self.transform(face)
            face_images.append(transformed_face)

        if len(face_images) > 0:
            face_images = torch.stack(face_images, dim=0)
            genders, ages = self.model(face_images)
            ages = torch.round(ages).float()  # Convert ages to float for mean calculation

            return ages.mean() if ages.numel() > 0 else torch.tensor([float('inf')])

        return torch.tensor([float('inf')])  # In case no faces were detected




    def padding_face(self, box, padding=10):
        return [
            box[0] - padding,
            box[1] - padding,
            box[2] + padding,
            box[3] + padding
        ]