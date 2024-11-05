
---
title: "Uso de Datos Sintéticos para garantizar la protección de datos personales por diseño en el entrenamiento de modelos de detección de fraude de identidad"
authors:
  - "Leandro Guzman, MDS2-2022, UAI"
  - "Carlos Muñoz, MDS2-2022, UAI"
  - "Francisco Guzman, MDS2-2022, UAI"
  - "Cristopher Lincoleo, MDS2-2022, UAI"
  - "Andrés Pumarino, Profesor Guía"
---

## Resumen

La creciente adopción del onboarding digital en el sector financiero ha facilitado la incorporación de nuevos clientes. Sin embargo, el aumento del fraude por suplantación de identidad ha obligado a las empresas a fortalecer sus mecanismos de verificación. Este trabajo presenta una metodología que integra la Evaluación de Impacto en la Protección de Datos (DPIA) en el marco CRISP-DM para garantizar el cumplimiento de normativas. Se propone el uso de datos sintéticos para entrenar modelos de machine learning, minimizando los riesgos de privacidad y optimizando el balance entre precisión y costos de error.

## Palabras clave

Biometric Validation, Facial Recognition, Fraud Detection, Deep Learning, Data Privacy, Synthetic Data, GAN, CRISP-DM, Regulatory Compliance

## Introducción

La transformación digital en el sector financiero ha mejorado la eficiencia operativa y la accesibilidad al incorporar procesos de onboarding digital. Sin embargo, esto ha planteado nuevos desafíos en términos de seguridad, especialmente en la prevención del fraude por suplantación de identidad.

*Ejemplo de placeholder de imagen:*

![Placeholder - Marco Metodológico Adaptado](#)

## Desarrollo de la Metodología

### Relevancia del Problema: Onboarding Digital y Desafío Regulatorio

Es esencial que el onboarding digital garantice tanto la autenticidad del cliente como el cumplimiento normativo en protección de datos (KYC, AML, CDD, GDPR).

*Ejemplo de placeholder de imagen:*

![Placeholder - Reporte Consumer Sentinel Network Data Book](#)

### Contexto Normativo

Se exploran normativas como el GDPR y los principios de privacidad, enfatizando la necesidad de proteger los datos biométricos y personales. En Chile, la ley de protección de datos está en proceso de actualización.

### Metodologías para la Gestión de Proyectos de Ciencia de Datos

Las metodologías tradicionales como KDD, CRISP-DM y SEMMA no consideran riesgos normativos. Aquí, se adapta el CRISP-DM integrando el DPIA.

### Selección de un Marco Metodológico Adaptado

El DPIA, en conjunto con CRISP-DM, forma un proceso robusto para la detección de fraude en onboarding digital, equilibrando la capacidad de detección y el cumplimiento normativo.

*Ejemplo de placeholder de imagen:*

![Placeholder - Etapas del CRISP-DM con DPIA Integrado](#)

## Uso de Datos Sintéticos para Protección de Identidad

Los datos sintéticos se han convertido en una herramienta para proteger la privacidad mientras se preservan las propiedades estadísticas. Este estudio utiliza GANs para generar datos biométricos sintéticos.

*Ejemplo de placeholder de imagen:*

![Placeholder - Ejemplos de Imágenes Sintéticas](#)

## Desarrollo de una Estrategia para Modelos de Machine Learning

La solución se basa en segmentar el problema de fraude en clases y entrenar modelos específicos para cada clase de fraude.

## Estudio de Caso: Empresa de Servicios Financieros

### Contexto Empresarial y Desafíos

La empresa enfrenta altos costos y problemas de suplantación de identidad en onboarding digital. Un DPIA detallado reveló riesgos significativos para la empresa y los usuarios.

### DPIA y Medidas para Mitigar el Riesgo

Se sugieren medidas para mitigar riesgos, incluyendo el uso de datos sintéticos y el fortalecimiento de la validación automatizada de identidad.

*Ejemplo de placeholder de imagen:*

![Placeholder - Flujo de Trabajo para la Generación de Imágenes Sintéticas](#)

### Análisis Exploratorio de los Datos (EDA)

Se identificaron patrones de fraude en la cédula de identidad, especialmente en el área del rostro. Estas características fueron categorizadas en clases.

*Ejemplo de placeholder de imagen:*

![Placeholder - Ejemplos de Adulteraciones por Clase](#)

## Generación de Datos Sintéticos utilizando StyleGAN

Se creó un flujo de generación de imágenes para representar los tipos de fraude identificados. Las imágenes fueron adaptadas para simular las condiciones reales de la captura.

*Ejemplo de placeholder de imagen:*

![Placeholder - Proceso de Generación de Imágenes Sintéticas](#)

## Desarrollo y Entrenamiento de Modelos Individuales

Cada clase de fraude se abordó con un modelo específico, minimizando el uso de modelos complejos. Los modelos se encapsulan en Python para facilitar su integración en un pipeline.

*Ejemplo de placeholder de imagen:*

![Placeholder - Modelo CNN para Detección de Fraude](#)

## Pipeline de Modelos Modulares para la Detección de Fraude

Se diseñó una pipeline secuencial optimizada en costos para ejecutar cada modelo hasta que uno detecte un posible fraude.

## Resultados y Métricas de Desempeño Técnico y Económico

El modelo propuesto reduce la tasa de error Tipo II y mejora la eficiencia en detección de fraude, generando un ahorro significativo en comparación con el sistema actual de la empresa.

*Ejemplo de placeholder de imagen:*

![Placeholder - Comparación de Costos](#)

## Discusión

### Elementos Distintivos

1. **Metodología Integrada CRISP-DM + DPIA**
2. **Uso de Datos Sintéticos para Privacidad**
3. **Pipeline Modular de Modelos**

### Limitaciones y Futuras Investigaciones

Futuras investigaciones deben enfocarse en mejorar la generación de datos sintéticos y explorar aplicaciones de detección de fraude en otros sectores.

## Conclusión

Este trabajo demuestra la viabilidad de desarrollar un sistema de detección de fraude preciso y seguro, utilizando datos sintéticos y un pipeline modular, con un ahorro económico significativo.

## Agradecimientos

Los autores agradecen a sus familias y al profesor guía por el apoyo durante el desarrollo de este proyecto.

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
