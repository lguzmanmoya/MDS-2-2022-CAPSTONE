# Modelo de Detección de fraude biométrico en el proceso de onboarding digital



## Descripción

El avance de la omnicanalidad ha revolucionado la forma en que las empresas de retail y crédito interactúan con sus clientes. La creciente adopción de canales digitales no solo ha mejorado la eficiencia operativa, sino que también ha aumentado la necesidad de mecanismos robustos de identificación y verificación de identidad. Esto hace esencial la integración de métodos que comparan selfies en tiempo real con fotos de documentos de identidad para prevenir fraudes y garantizar la autenticidad de los usuarios.

## Desafíos Técnicos y Logísticos

La validación de imágenes presenta varios desafíos técnicos y logísticos. Requiere grandes volúmenes de datos diversificados para entrenar modelos de reconocimiento facial precisos y justos, manejando variaciones en iluminación, poses y expresiones faciales, lo cual incrementa significativamente la complejidad del entrenamiento.

Por ejemplo, entrenar un modelo robusto de reconocimiento facial puede requerir millones de imágenes diversificadas y hardware especializado como GPUs de alto rendimiento, incrementando los costos de implementación.

## Errores Tipo I y Tipo II

Es crucial equilibrar los errores tipo I (falsos positivos) y tipo II (falsos negativos) más que enfocarse únicamente en la precisión global del modelo. Un falso positivo, donde se detecta fraude incorrectamente, puede causar problemas significativos al usuario legítimo y afectar la confianza del cliente. Por otro lado, un falso negativo permite que el fraude pase desapercibido, resultando en pérdidas financieras para la empresa.

## Restricciones Legales y Éticas

Las restricciones legales y éticas juegan un papel crucial en la implementación de estos sistemas. El Reglamento General de Protección de Datos (GDPR) de la Unión Europea impone estrictas normas sobre la recopilación y procesamiento de datos personales, incluyendo imágenes faciales, y requiere el consentimiento explícito de los usuarios. Las infracciones pueden resultar en multas significativas. Estas regulaciones no solo protegen la privacidad de los usuarios, sino que también imponen desafíos adicionales a las empresas que deben equilibrar la seguridad y la conformidad normativa.

## Caso de Negocio

En este contexto, se ha desarrollado un caso de negocio específico para una empresa de retail que ofrece servicios financieros asociados y se enfoca en el segmento de bajos ingresos. La empresa ha migrado a canales digitales y enfrenta el problema de fraudes de identidad, donde individuos utilizan tarjetas de identidad robadas y las falsifican poniendo fotos de ellos mismos para validarse. El objetivo es desarrollar un sistema capaz de identificar si una validación es legítima o fraudulenta, comparando dos imágenes: una del rostro en el documento de identidad y otra del rostro de la persona que se está validando. Este sistema debe ser robusto, preciso y capaz de operar en condiciones variadas de iluminación y calidad de imagen.

## Metodología Propuesta

Para resolver este problema, se propone una evolución de la metodología CRISP-DM que integre el Data Protection Impact Assessment (DPIA), asegurando que la solución cumpla plenamente con las normativas de protección de datos personales, evaluando y mitigando los riesgos asociados desde las primeras fases del proyecto hasta su implementación y operación.

### Uso de Datos Sintéticos

De este proceso se concluyó que el uso de datos sintéticos es una alternativa viable. El uso de datos sintéticos permite la creación de un conjunto de datos diversificado y equilibrado, mitigando los problemas de privacidad asociados con el uso de datos reales.

Proyectos como DigiFace-1M de Microsoft y frameworks como StyleGAN2 han demostrado la efectividad de las imágenes sintéticas para mejorar la precisión y reducir el sesgo en modelos de reconocimiento facial.

### Modelos de Reconocimiento de Fraude

El uso de modelos de reconocimiento de fraude en imágenes es complejo debido a la necesidad de identificar patrones sutiles y manipulaciones en las imágenes. Los modelos avanzados de machine learning (ML) y deep learning (DL) son esenciales para analizar grandes volúmenes de datos y adaptarse a patrones de fraude en constante evolución, requiriendo una alta capacidad computacional y un entrenamiento intensivo con grandes conjuntos de datos diversificados.

### Simplificación del Análisis

Una alternativa para simplificar la detección de fraude en imágenes es focalizar el análisis en zonas vulnerables específicas de las imágenes, como áreas donde es más probable que ocurran manipulaciones. Este enfoque puede reducir la complejidad del modelo y mejorar la eficiencia del proceso de detección. Por ejemplo, el uso de landmarks (puntos de referencia) permite identificar áreas específicas y analizar inconsistencias en estas regiones focalizadas, mejorando la detección de manipulaciones sutiles.

### Cañería Modular

En lugar de utilizar un único modelo complejo, la integración de múltiples modelos simples en una cañería modular puede mejorar la precisión y la robustez de la detección de fraude en imágenes. Cada modelo puede estar especializado en detectar tipos específicos de fraude o manipulación, y sus resultados pueden combinarse para proporcionar una decisión final más precisa.

### Optimización del Orden de Ejecución

El orden de los modelos en una cañería de ejecución es crucial para optimizar el balance entre errores tipo I y tipo II. Determinar el orden óptimo de ejecución de los modelos puede maximizar la precisión y minimizar los falsos positivos (errores tipo I) y falsos negativos (errores tipo II). Técnicas de optimización, como el uso de algoritmos evolutivos y análisis de sensibilidad, pueden ayudar a encontrar el mejor orden de ejecución, priorizando los modelos más precisos en las primeras etapas para filtrar rápidamente los casos más obvios de fraude y dejando los casos más ambiguos para análisis más detallados en etapas posteriores.

La optimización del orden de ejecución de los modelos se puede lograr mediante análisis iterativos y evaluaciones basadas en métricas de rendimiento como la matriz de confusión, que mide los verdaderos positivos, verdaderos negativos, falsos positivos y falsos negativos. Integrar técnicas de optimización en el diseño de la cañería permite ajustar dinámicamente el orden de los modelos según el rendimiento actual y las características del conjunto de datos.

## Conclusión

Estos enfoques y técnicas son fundamentales para desarrollar sistemas eficaces de detección de fraude en imágenes, mejorando tanto la precisión como la eficiencia operativa al tiempo que cumplen con los requisitos legales y éticos.


## Licencias

Este proyecto utiliza las siguientes librerías:

- DLIB y los siguientes modelos: dlib_face_recognition_resnet_model_v1.dat y shape_predictor_68_face_landmarks.dat. Ambos se encuentran bajo licencia Boost Software License, versión 1.0.
- Facenet-pytorch, agenet y sus pesos, los que están distribuidos bajo la licencia MIT.
  

## Instrucciones de Uso

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/lguzmanmoya/MDS-2-2022-CAPSTONE.git
   cd MDS-2-2022-CAPSTONE

2. Bajar weights.pt, este archivo no se puede dejar en github por temas de tamaño. Se baja de [gtihub, Pytorch-Age-Estimation](https://github.com/manhcuong02/Pytorch-Age-Estimation).

3. Instalación de dependencias
   ```bash
   pip install -r requirements.txt
