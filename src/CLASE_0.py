import dlib
import numpy as np
from PIL import Image

class FaceVerifier:
    """
    Clase para verificar si dos imágenes PIL corresponden a la misma persona usando Dlib.
    """
    
    def __init__(self, predictor_path, face_rec_model_path, threshold):
        """
        Inicializa el detector, el predictor y el modelo de reconocimiento de rostros,
        además de establecer el umbral de decisión.
        
        Args:
        predictor_path (str): Ruta al predictor de puntos faciales.
        face_rec_model_path (str): Ruta al modelo de reconocimiento facial.
        threshold (float): Umbral para determinar si dos imágenes son de la misma persona.
        """
        self.detector = dlib.get_frontal_face_detector()
        self.predictor = dlib.shape_predictor(predictor_path)
        self.face_rec_model = dlib.face_recognition_model_v1(face_rec_model_path)
        self.threshold = threshold

    def convert_and_encode(self, image):
        """
        Convierte una imagen PIL a un formato compatible con Dlib, detecta un rostro y calcula su descriptor.
        
        Args:
        image (PIL.Image): Imagen PIL.
        
        Returns:
        numpy.ndarray or None: Descriptor del rostro o None si no se detecta ningún rostro.
        """
        try:
            # Convertir imagen PIL a formato RGB para Dlib
            image_rgb = image.convert('RGB')
            img_array = np.array(image_rgb)
            dets = self.detector(img_array, 1)
            if len(dets) > 0:
                shape = self.predictor(img_array, dets[0])
                face_descriptor = self.face_rec_model.compute_face_descriptor(img_array, shape)
                return np.array(face_descriptor)
            else:
                raise ValueError("No se detectaron rostros en la imagen.")
        except Exception as e:
            raise ValueError(f"Error al procesar la imagen: {e}")

    def verify_faces(self, image_id, image_eval):
        """
        Verifica si dos imágenes PIL son de la misma persona basándose en el umbral establecido.
        
        Args:
        image_id (PIL.Image): Imagen de identificación.
        image_eval (PIL.Image): Imagen de evaluación.
        
        Returns:
        bool: True si las imágenes son de personas distintas, False si son de la misma persona.
        """
        try:
            encoding_id = self.convert_and_encode(image_id)
            encoding_eval = self.convert_and_encode(image_eval)
            
            if encoding_id is not None and encoding_eval is not None:
                distance = np.linalg.norm(encoding_id - encoding_eval)
                return distance >= self.threshold
            else:
                return False
        except ValueError as e:
            print(e)
            return False

