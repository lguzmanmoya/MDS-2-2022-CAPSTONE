import numpy as np
import dlib
from PIL import Image, ImageDraw
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

from PIL import Image, ImageEnhance, ImageOps, ImageFilter

class Fake_III_B_detector:
    def __init__(self, model_path, predictor_path):
        self.model_paths = {
            'neural_network': model_path,
            'predictor_path': predictor_path
        }
        # Cargar la red neuronal
        self.model = load_model(self.model_paths['neural_network'])



    def crop_square(self,image, left=0, top=0, m=10, n=10):

        # Define las coordenadas de recorte
        right = left + m
        bottom = top + n

        # Recorta el área definida
        cropped_image = image.crop((left, top, right, bottom))
        return cropped_image    


    def preprocess_image_for_edge_detection_rgb(self,image):

        # Convertir a escala de grises para simplificar la detección de bordes
        grayscale_image = image.convert("L")
        
        # Aplicar un filtro de suavizado para reducir el ruido
        blurred_image = grayscale_image.filter(ImageFilter.GaussianBlur(radius=0))
        
        # Mejorar el contraste para que los bordes sean más visibles
        enhancer = ImageEnhance.Contrast(blurred_image)
        high_contrast_image = enhancer.enhance(3)
        
        # Aplicar un filtro de detección de bordes
        edge_image = high_contrast_image.filter(ImageFilter.FIND_EDGES)
        
        # Convertir la imagen de detección de bordes a modo RGB
        rgb_edge_image = edge_image.convert("RGB")

        return rgb_edge_image


    def process_and_combine_images(self,image, m=20, n=20):

        # Recortar las regiones de la parte superior izquierda y superior derecha
        left_image = self.crop_square(image, left=0, top=0, m=m, n=n)
        right_image = self.crop_square(image, left=image.width - m, top=0, m=m, n=n)
        
        # Aplicar el procesamiento de detección de bordes a cada recorte
        left_processed = self.preprocess_image_for_edge_detection_rgb(left_image)
        right_processed = self.preprocess_image_for_edge_detection_rgb(right_image)
        
        # Crear una nueva imagen uniendo ambas regiones procesadas
        combined_width = left_processed.width + right_processed.width
        combined_height = max(left_processed.height, right_processed.height)
        combined_image = Image.new("RGB", (combined_width, combined_height))
        combined_image.paste(left_processed, (0, 0))
        combined_image.paste(right_processed, (left_processed.width, 0))
        
        # Estandarizar la imagen combinada a un tamaño de 50x50
        standardized_image = combined_image.resize((50, 50), Image.Resampling.LANCZOS)

        return standardized_image




    def predict(self, image_pil):
        try:
            processed_image = self.process_and_combine_images(image_pil, m=30, n=80)
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
            processed_image = self.process_and_combine_images(image_pil, m=30, n=80)
            image_array = img_to_array(processed_image)
            image_array = image_array / 255.0  # Normalizar los datos de imagen
            image_array = np.expand_dims(image_array, axis=0)  # Añadir una dimensión de batch

            prediction = self.model.predict(image_array, verbose=0)
            return prediction[0][0]  # Devuelve la probabilidad de que la imagen sea de la clase positiva
        except Exception as e:
            print(f"Error processing image: {e}")
            return None

