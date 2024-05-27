import numpy as np
from PIL import Image
from joblib import load

class Fake_II_IV_detector:
    def __init__(self, model_path):
        # Cargar el modelo RandomForest desde un archivo .joblib
        self.model = load(model_path)

    def max_difference_histogram(self, img_in, bins=40):
        # Convertir la imagen en un array de numpy
        image_array = np.array(img_in)
        
        # Normalizar cada canal por su valor máximo
        max_values = image_array.max(axis=(0, 1))
        normalized_image_array = image_array / max_values

        # Calcular los histogramas porcentuales para cada canal
        histograms = np.zeros((3, bins))
        for channel in range(3):  # Para cada canal RGB
            histogram, _ = np.histogram(
                normalized_image_array[:, :, channel], bins=bins, range=(0, 1)
            )
            histograms[channel] = histogram / histogram.sum()  # Porcentaje de cada bin

        # Calcular las diferencias máximas entre bins
        max_differences = np.zeros(bins)
        for i in range(bins):
            max_differences[i] = max(histograms[:, i]) - min(histograms[:, i])

        return max_differences

    def predict(self, pil_img):
        # Preprocesar la imagen para obtener las características
        features = self.max_difference_histogram(pil_img)[1:32]

        # Predecir utilizando el modelo RandomForest y devolver resultado binario
        prediction = self.model.predict([features])
        return (prediction[0] == 1)

    def predict_proba(self, pil_img):
        # Preprocesar la imagen para obtener las características
        features = self.max_difference_histogram(pil_img)[1:32]

        # Predecir la probabilidad utilizando el modelo RandomForest y devolver la probabilidad
        probabilities = self.model.predict_proba([features])
        return probabilities[0]


