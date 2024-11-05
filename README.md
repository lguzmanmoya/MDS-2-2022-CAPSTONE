# Uso de Datos Sintéticos para garantizar la protección de datos personales por diseño en el entrenamiento de modelos de detección de fraude de identidad
authors:
  - "Leandro Guzman, MDS2-2022, UAI"
  - "Carlos Muñoz, MDS2-2022, UAI"
  - "Francisco Guzman, MDS2-2022, UAI"
  - "Cristopher Lincoleo, MDS2-2022, UAI"
  - "Andrés Pumarino, Profesor Guía"

## Resumen

La creciente adopción del onboarding digital por parte del sector financiero minorista ha agilizado la incorporación de nuevos clientes, ofreciendo una experiencia fácil y rápida para acceder a sus servicios. No obstante, el aumento de casos de fraude por suplantación de identidad ha presionado a las empresas a reforzar sus mecanismos de verificación y detección. Además, entrenar modelos de detección cumpliendo con las nuevas normativas de protección de datos personales presenta desafíos: por un lado, entrenar modelos altamente complejos requiere una gran cantidad de imágenes, y por otro lado, la protección de datos personales, particularmente datos biométricos, requiere la autorización de los titulares para el uso específico de este tipo de datos. Este trabajo presenta una metodología basada en cuatro elementos clave: una metodología similar a CRISP-DM que integra la Evaluación de Impacto en la Protección de Datos (DPIA) para garantizar el cumplimiento de las normativas de protección de datos; el uso de datos sintéticos para proporcionar suficiente información para entrenar modelos equilibrados; el uso de modelos simples que se centran en las fortalezas de los algoritmos y las debilidades de cada tipo de fraude en lugar de una única solución altamente compleja; y una tubería modular secuencial optimizada para los costos de errores Tipo I y Tipo II, que permite la integración de múltiples modelos especializados. La solución propuesta se aplicó a través de un caso de negocio en una empresa del sector minorista financiero chileno enfocada en el nivel socioeconómico medio-bajo, la cual tiene implementado el onboarding digital, lo que permitió probar la metodología y evaluar su impacto financiero.

## Palabras clave

Biometric Validation, Facial Recognition, Fraud Detection, Deep Learning, Data Privacy, Synthetic Data, Generative Adversarial Networks (GANs), CRISP-DM, Regulatory Compliance

## Introducción

La transformación digital en el sector financiero minorista ha impulsado significativamente la eficiencia operativa y la accesibilidad de sus clientes con la incorporación del proceso de onboarding digital, pero también ha generado nuevos desafíos en términos de seguridad. A medida que las empresas han sumado este proceso de incorporación digital de nuevos clientes, han debido reforzar sus mecanismos de verificación y detección para prevenir el fraude por suplantación de identidad.

*Ejemplo de placeholder de imagen:*

![Placeholder - Introducción al Fraude en Onboarding Digital](#)

## Desarrollo de la Metodología

### Relevancia del Problema: Onboarding Digital, Innovación Empresarial y Desafío Regulatorio

Es importante entender el proceso de onboarding digital no solo como proceso remoto para la captura de nuevos clientes, sino como un proceso que debe asegurar una relación de confianza entre el cliente y la empresa, garantizando la legitimidad de los usuarios a incorporar y cumpliendo con normativas como KYC (Know Your Client), AML (Anti Money Laundry), CDD (Customer Due Diligence) y regulaciones de protección de datos como GDPR (General Data Protection Regulation). 

*Ejemplo de placeholder de imagen:*

![Placeholder - Reporte de Fraude en Onboarding](#)

### Contexto Normativo

Tanto por razones éticas como normativas es necesario proteger la identidad de las personas. Con la implementación del GDPR, los países han adecuado sus leyes sobre protección de datos personales. En este contexto, el uso de datos biométricos para el entrenamiento de modelos de detección de fraude presenta un dilema crucial: la necesidad de grandes volúmenes de datos de alta calidad para lograr precisión y la obligación de proteger estos datos sensibles para cumplir con las normativas de privacidad.

### Metodologías para la Gestión de Proyectos de Ciencia de Datos

Las metodologías convencionales como KDD, CRISP-DM y SEMMA no contemplan los riesgos normativos. Este estudio propone integrar el DPIA al proceso CRISP-DM, adaptando sus etapas con una perspectiva de la protección de datos y la privacidad por diseño.

*Ejemplo de placeholder de imagen:*

![Placeholder - Integración del DPIA en CRISP-DM](#)

## Uso de Datos Sintéticos para Protección de Identidad

El uso de datos sintéticos, generados mediante GANs, ha demostrado ser una solución efectiva para cumplir con las normativas de protección de datos mientras se asegura la calidad y la utilidad de los datos para la detección de fraude.

*Ejemplo de placeholder de imagen:*

![Placeholder - Ejemplos de Imágenes Sintéticas para Detección de Fraude](#)

## Desarrollo de una Estrategia para Modelos de Machine Learning

La solución se basa en segmentar el problema de fraude en clases individuales y entrenar modelos específicos para cada clase, en lugar de desarrollar una única solución compleja.

*Ejemplo de placeholder de imagen:*

![Placeholder - Pipeline Modular para Modelos de Machine Learning](#)

## Estudio de Caso: Empresa de Servicios Financieros

### Contexto Empresarial y Desafíos

La compañía analizada pertenece al sector minorista financiero chileno. Su mercado objetivo es el nivel socioeconómico medio-bajo. Su producto principal es la tarjeta de crédito, y ha incorporado el onboarding digital para la captura de nuevos clientes. No obstante, esta solución digital no ha disminuido la tasa de fraudes, lo que ha motivado una revisión de su proceso de verificación.

### DPIA

Se detallan los pasos del DPIA que fueron necesarios para el análisis de este caso, identificando y mitigando riesgos relacionados con la privacidad de los datos.

*Ejemplo de placeholder de imagen:*

![Placeholder - Proceso de DPIA en Onboarding Digital](#)

### Análisis Exploratorio de los Datos (EDA)

Se detectaron patrones específicos en los fraudes a partir de inconsistencias en la zona de la fotografía del titular de la cédula de identidad. Estos incidentes fueron clasificados en Clases, basadas en el tipo de adulteración.

*Ejemplo de placeholder de imagen:*

![Placeholder - Clases de Adulteración en Onboarding Digital](#)

## Generación de Datos Sintéticos utilizando StyleGAN

Para este caso específico, la data sintética debe cumplir con ser fotorrealista y diversa. En el estudio se generaron imágenes sintéticas para reproducir las características de las cédulas de identidad y de los intentos de fraude.

*Ejemplo de placeholder de imagen:*

![Placeholder - Proceso de Generación de Imágenes Sintéticas](#)

## Desarrollo y Entrenamiento de Modelos Individuales

Cada clase de fraude se resolvió mediante un modelo ad-hoc que aprovecha las vulnerabilidades de cada tipo de fraude en lugar de un único modelo para todas las clases.

*Ejemplo de placeholder de imagen:*

![Placeholder - Resultados del Entrenamiento de los Modelos](#)

### Clase de Fraude 0: Cuando la Persona no es la Misma

Este caso es el punto base del proceso de validación de identidad, donde se compara la imagen de ID (cédula de identidad) y la imagen de validación.

### Clase de Fraude I: Cuando la Persona es Menor de Edad

En este caso se utiliza una red pre-entrenada para la estimación de la edad. Dado que la generación de menores sintéticos es compleja, se utiliza un punto de corte de edad estimado.

*Ejemplo de placeholder de imagen:*

![Placeholder - Ejemplos de Adulteración por Edad](#)

### Clases de Fraude II y IV: Adulteración de Firma de Colores

Aquí se analizaron los histogramas de color en las imágenes de referencia versus las adulteradas, permitiendo una clara separación de clases en función de la firma de color.

### Clase de Fraude III: Adulteración que Mantiene la Firma de Colores

Para este caso, se utilizó una red neuronal convolucional con arquitectura VGG adaptada para detectar los puntos de unión entre la imagen original y la modificación.

## Pipeline de Modelos Modulares para la Detección de Fraude

La integración de los modelos se realizó mediante una pipeline modular secuencial, optimizada en función de los costos de error Tipo I y Tipo II. Esto permite detectar fraudes de manera más precisa.

*Ejemplo de placeholder de imagen:*

![Placeholder - Pipeline Modular en Proceso](#)

## Resultados y Métricas de Desempeño Técnico y Económico

El sistema desarrollado redujo la tasa de error Tipo II en un 5.2\%, lo que permite a la empresa prescindir de su actual sistema de verificación, con un ahorro económico significativo.

*Ejemplo de placeholder de imagen:*

![Placeholder - Comparación de Resultados entre Modelos](#)

## Discusión

### Elementos Distintivos

1. **Metodología CRISP-DM Integrada con DPIA**: Garantiza el cumplimiento normativo.
2. **Uso de Datos Sintéticos**: Permite el entrenamiento de modelos sin comprometer la privacidad.
3. **Pipeline Modular**: Facilita la actualización y escalabilidad del sistema de detección de fraude.

### Limitaciones y Futuras Investigaciones

El sistema debe validarse con datos específicos del cliente para ajustar su rendimiento. Las futuras investigaciones pueden enfocarse en mejorar la generación de datos sintéticos para hacerlos aún más realistas.

## Conclusión

Este trabajo demuestra que es posible desarrollar sistemas de detección de fraude que sean precisos y respetuosos con la privacidad mediante el uso adecuado de datos sintéticos y un pipeline modular. La metodología propuesta establece un marco de referencia sólido para futuras investigaciones y aplicaciones en diversos sectores que enfrentan problemas similares de protección de datos y necesidades de modelos avanzados.

## Agradecimientos

Los autores desean agradecer a:
- Sus familias, por su paciencia y constante apoyo.
- A nuestro profesor guía, cuya enseñanza inspiró la visión integral de este proyecto.

## Referencias








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
