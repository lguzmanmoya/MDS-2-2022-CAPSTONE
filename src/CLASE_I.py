import sys
sys.path.append('../modelos/Pytorch-Age-Estimation-main')  

from PIL import Image

# Asumiendo que la clase AgeEstimator y su método predict ya están definidos
from predict import AgeEstimator

class AgeChecker:
    def __init__(self, weights, threshold):
        """
        Inicializa el verificador de edad con un modelo y un umbral específico.

        Args:
            weights (str): Ruta al archivo de pesos del modelo.
            threshold (int): Umbral de edad para determinar si la persona es menor.
        """
        self.model = AgeEstimator(weights=weights)
        self.threshold = threshold

    def is_minor(self, image):
        """
        Determina si la persona en la imagen es menor de edad según el umbral establecido.

        Args:
            image (PIL.Image): Imagen de la persona a evaluar.

        Returns:
            bool: True si la edad estimada es menor que el umbral, False de lo contrario.
        """
        try:
            # Realizar la predicción directamente con la imagen PIL
            age_estimate = self.model.predict(image).item()
            return age_estimate < self.threshold
        except Exception as e:
            print(f"Error al estimar la edad: {str(e)}")
            return False
