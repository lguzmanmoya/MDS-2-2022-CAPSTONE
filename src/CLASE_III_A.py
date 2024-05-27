import numpy as np
import dlib
from PIL import Image, ImageDraw
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

class Fake_III_A_detector:
    def __init__(self, model_path, predictor_path):
        self.model_paths = {
            'neural_network': model_path,
            'predictor_path': predictor_path
        }
        # Cargar la red neuronal
        self.model = load_model(self.model_paths['neural_network'])

    def linearize_oval_face_contour(self, image_pil, n=10, output_size=(50, 50)):
        image_np = np.array(image_pil)
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor(self.model_paths['predictor_path'])
        detected_faces = detector(image_np, 1)

        if not detected_faces:
            raise ValueError("No faces detected in the image.")

        face = detected_faces[0]
        landmarks = predictor(image_np, face)
        contour_points = np.array([[landmarks.part(i).x, landmarks.part(i).y] for i in range(0, 17)])

        width, height = 2 * n + 1, len(contour_points)
        result_image = Image.new('RGB', (width, height), (255, 255, 255))
        draw = ImageDraw.Draw(result_image)

        for i, (x, y) in enumerate(contour_points):
            left_x = n
            for offset in range(-n, n + 1):
                source_x = x + offset
                if 0 <= source_x < image_np.shape[1]:
                    color = tuple(image_np[y, source_x])
                    draw.point((left_x + offset, i), fill=color)

        result_image = result_image.resize(output_size, Image.Resampling.LANCZOS)
        return result_image

    def predict(self, image_pil):
        try:
            processed_image = self.linearize_oval_face_contour(image_pil)
            image_array = img_to_array(processed_image)
            image_array = image_array / 255.0  # Normalizar los datos de imagen
            image_array = np.expand_dims(image_array, axis=0)  # Añadir una dimensión de batch

            prediction = self.model.predict(image_array, verbose=0)
            return prediction[0][0] > 0.5
        except Exception as e:
            print(f"Error processing image: {e}")
            return False

    def predict_proba(self, image_pil):
        try:
            processed_image = self.linearize_oval_face_contour(image_pil)
            image_array = img_to_array(processed_image)
            image_array = image_array / 255.0  # Normalizar los datos de imagen
            image_array = np.expand_dims(image_array, axis=0)  # Añadir una dimensión de batch

            prediction = self.model.predict(image_array, verbose=0)
            return prediction[0][0]  # Devuelve la probabilidad de que la imagen sea de la clase positiva
        except Exception as e:
            print(f"Error processing image: {e}")
            return None

