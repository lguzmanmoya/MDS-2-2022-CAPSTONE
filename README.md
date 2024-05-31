# On the Use of Synthetic Data to Ensure Personal Data Protection by Design in Fraud Detection Models.
<div style="text-align: center;">
<img src="./data/imagenes_repo/intro.png" style="width:500px;height:500px;">
</div>

## Contexto
El presente trabajo corresponde a los respaldos del proyecto capstone del Magister en Data Science de la Universidad Adolfo Ibañez. MSD-2-2022.

**Equipo:**
   - **Leandro Guzmán Moya** - Ingeniero Civil Químico
   - **Carlos Muñoz Cavieres**
   - **Cristopher Lincoleo Oyarce**
   - **Francisco Guzmán Valderrama**

**Profesor Guía:**
   - **Andrés Pumarino** - Abogado | UAI, Magíster en Negocios UAI, Profesor Fac. Ingeniería PUC, UAI/Derecho y tecnología.

**Correferente:**
   - **Fabián Palma** – Magíster en Data Science, Gerente de Riesgo de AB Servicios Financieros    

## Disclaimer

All images and people that appear in this repository are synthetic images created using STYLEGAN.



## Abstract
The increasing adoption of digital channels by retail and credit sectors has improved operational efficiency and heightened the need for robust identification and verification mechanisms. However, training detection models while complying with new personal data protection regulations presents complexities: on the one hand, training highly complex models requires a large number of images, and on the other hand, the protection of personal data, particularly biometric data, necessitates specific permissions authorizing their use for these purposes.
This paper presents a methodology based on four key elements:
A CRISP-DM-like methodology that integrates Data Protection Impact Assessment (DPIA) to ensure adherence to data protection regulations.
The use of Synthetic data to provide enough information to train balanced models.
The use of simple models that focus on the strengths of algorithms and the weaknesses of each fraud attempt rather than a single highly complex solution.
A modular sequential pipeline optimized for the costs of Type I and Type II errors, allowing for the integration of multiple specialized models.
The proposed solution was validated through a business case in a retail finance company serving low-income segments, showcasing the methodology's effectiveness.

## Keywords

Omnichannel, Identity Fraud Detection, Synthetic Data, Modular Model Pipelines, Data Protection, CRISP-DM, DPIA, Regulatory Compliance.

## I. Introduction

### A. Problem Statement

The primary issue addressed in this paper is the fraudulent use of stolen identity cards, where individuals substitute their photos on the stolen IDs to validate themselves. The goal is to develop a system that can accurately determine whether an identity validation is legitimate or fraudulent while ensuring compliance with regulatory standards.

### B. Contributions

1. Integration of synthetic data to enhance model training and ensure privacy.
2. Development of a modular pipeline for fraud detection.
3. Introduction of a CRISP-DM evolution incorporating DPIA for regulatory compliance.
4. Validation through a real-world business case in retail finance.

## II. Background and Related Work

### A. Omnichannel Strategies in Retail Finance

The advancement of omnichannel strategies has revolutionized how retail and credit companies interact with their customers. The integration of multiple channels, both digital and physical, has significantly enhanced operational efficiency and customer experience. However, this shift has also increased the complexity of identity verification processes, necessitating more sophisticated methods to prevent fraud.

### B. Identity Verification Techniques

Traditional identity verification techniques, such as manual checks of identity documents, are inadequate in the digital age. Advanced methods, including biometric verification, facial recognition, and real-time selfie comparisons with ID photos, have emerged. Despite their advantages, these techniques face challenges like variability in lighting, poses, and expressions.

### C. Synthetic Data in Machine Learning

Synthetic data has become a valuable resource in training machine learning models, especially when dealing with sensitive information like facial images. Projects like Microsoft’s DigiFace-1M and frameworks like StyleGAN2 have demonstrated the effectiveness of synthetic data in enhancing model performance and reducing biases while maintaining privacy.

## III. Methodology

### A. Evolution of CRISP-DM

The proposed methodology evolves the traditional CRISP-DM framework by integrating Data Protection Impact Assessment (DPIA). This integration ensures that data protection considerations are embedded throughout the project lifecycle, from business understanding to deployment.

### B. Data Collection and Synthetic Data Generation

Data collection involves gathering diverse and high-quality images to train robust facial recognition models. Given privacy concerns, synthetic data generated using tools like StyleGAN2 offers a viable alternative. Synthetic images mimic real-world variations in lighting, poses, and expressions, providing a rich dataset for model training without compromising user privacy.

### C. Model Training and Evaluation

Training robust facial recognition models requires handling significant variability in image data. The use of GPUs and other specialized hardware accelerates this process. Models are evaluated based on their accuracy and their ability to minimize Type I (false positives) and Type II (false negatives) errors.

### D. Modular Model Pipeline

A modular pipeline approach is employed, where multiple simpler models are integrated to detect specific types of fraud. Each model focuses on particular aspects of the image, such as landmarks and other vulnerable regions, and their combined outputs enhance the overall accuracy and robustness of the system.

### E. Optimization Techniques

Optimization techniques, such as evolutionary algorithms and sensitivity analysis, are used to determine the optimal order of model execution. This process helps balance the trade-off between minimizing false positives and false negatives, thereby improving the overall effectiveness of the fraud detection system.

## IV. Case Study: Retail Finance Company

### A. Business Context

The case study focuses on a retail finance company serving low-income segments. The company has transitioned to digital channels and faces challenges with identity fraud, where stolen ID cards are manipulated to validate false identities.

### B. Implementation

The proposed system is implemented within the company's existing infrastructure. Modifications are made to accommodate the specific needs of the company, such as handling low-quality images and ensuring compliance with relevant regulations.

### C. Results

The implementation results are evaluated based on key metrics such as accuracy, false positive rate, and false negative rate. The system demonstrates significant improvements over baseline methods, particularly in reducing false positives, which enhances user trust and operational efficiency.

## V. Discussion

### A. Technical and Logistical Challenges

Implementing the proposed system involves several technical and logistical challenges, including the need for large volumes of diversified data, high computational resources, and ensuring real-time processing capabilities. Synthetic data generation and modular pipeline integration are critical in addressing these challenges.

### B. Legal and Ethical Considerations

Legal and ethical considerations are paramount in the development and deployment of identity verification systems. Compliance with regulations like the GDPR ensures that user privacy is protected, and the DPIA integration helps manage risks associated with data processing.

### C. Future Work

Future work could explore further enhancements in synthetic data generation, such as using more advanced GAN models. Additionally, the modular pipeline approach could be extended to other types of biometric verification and fraud detection applications.

## VI. Conclusion

This paper presents a comprehensive approach to identity fraud detection in retail finance using synthetic data and modular model pipelines. The proposed methodology ensures compliance with data protection regulations and demonstrates significant improvements in fraud detection accuracy and operational efficiency.

## References





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
