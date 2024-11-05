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

## Disclaimer

All images and people that appear in this repository are synthetic images created using STYLEGAN.



## Abstract
The growing adoption of digital onboarding by the retail financial sector has streamlined the integration of new customers, offering a quick and easy experience for accessing services. However, the increase in identity fraud cases has pressured companies to strengthen their verification and detection mechanisms. Additionally, training detection models while complying with new data protection regulations presents challenges: on the one hand, training highly complex models requires a large volume of images; on the other hand, data protection regulations, especially regarding biometric data, require the authorization of data subjects for specific uses. This work presents a methodology based on four key elements: a CRISP-DM-like methodology that integrates Data Protection Impact Assessment (DPIA) to ensure compliance with data protection regulations; the use of synthetic data to provide sufficient information for training balanced models; the application of simple models that focus on the strengths of algorithms and the weaknesses of each fraud type rather than relying on a single, highly complex solution; and a sequential modular pipeline optimized for Type I and Type II error costs, allowing the integration of multiple specialized models. The proposed solution was applied in a business case at a Chilean retail financial company focused on the middle-lower socioeconomic segment, which has implemented digital onboarding, allowing the methodology to be tested and its financial impact evaluated.

## Keywords

Identity Fraud Detection, Synthetic Data, Modular Model Pipelines, Data Protection, CRISP-DM, DPIA, Regulatory Compliance.

## I. Introduction

### Problem Statement

The primary issue addressed is the fraudulent use of stolen identity cards, where individuals substitute their photos on the stolen IDs to validate themselves. The goal is to develop a system that can accurately determine whether an identity validation is legitimate or fraudulent while ensuring compliance with regulatory standards.

## II. Background

### Omnichannel Strategies in Retail Finance

The advancement of omnichannel strategies has revolutionized how retail and credit companies interact with their customers. The integration of multiple channels, both digital and physical, has significantly enhanced operational efficiency and customer experience. However, this shift has also increased the complexity of identity verification processes, necessitating more sophisticated methods to prevent fraud.

### Identity Verification Techniques

Traditional identity verification techniques, such as manual checks of identity documents, are inadequate in the digital age. Advanced methods, including biometric verification, facial recognition, and real-time selfie comparisons with ID photos, have emerged. Despite their advantages, these techniques face challenges like variability in lighting, poses, and expressions.

### Synthetic Data in Machine Learning

Synthetic data has become a valuable resource in training machine learning models, especially when dealing with sensitive information like facial images. Projects like Microsoft’s DigiFace-1M and frameworks like StyleGAN2 have demonstrated the effectiveness of synthetic data in enhancing model performance and reducing biases while maintaining privacy.

## III. Methodology

### Evolution of CRISP-DM

The proposed methodology evolves the traditional CRISP-DM framework by integrating Data Protection Impact Assessment (DPIA). This integration ensures that data protection considerations are embedded throughout the project lifecycle, from business understanding to deployment.

### Data Collection and Synthetic Data Generation

Data collection involves gathering diverse and high-quality images to train robust facial recognition models. Given privacy concerns, synthetic data generated using tools like StyleGAN2 offers a viable alternative. Synthetic images mimic real-world variations in lighting, poses, and expressions, providing a rich dataset for model training without compromising user privacy.

### Model Training and Evaluation

Training robust facial recognition models requires handling significant variability in image data. The use of GPUs and other specialized hardware accelerates this process. Models are evaluated based on their accuracy and their ability to minimize Type I (false positives) and Type II (false negatives) errors.

### Modular Model Pipeline

A modular pipeline approach is employed, where multiple simpler models are integrated to detect specific types of fraud. Each model focuses on particular aspects of the image, such as landmarks and other vulnerable regions, and their combined outputs enhance the overall accuracy and robustness of the system.

### Optimization Techniques

Optimization techniques and sensitivity analysis, are used to determine the optimal order of model execution. This process helps balance the trade-off between minimizing false positives and false negatives, thereby improving the overall effectiveness of the fraud detection system.

## IV. Case Study: Retail Finance Company

### Business Context

The case study focuses on a retail finance company serving low-income segments. The company has transitioned to digital channels and faces challenges with identity fraud, where stolen ID cards are manipulated to validate false identities.

### Results

The implementation results are evaluated based on key metrics such as accuracy, false positive rate, and false negative rate. The system demonstrates significant improvements over baseline methods, particularly in reducing false positives, which enhances user trust and operational efficiency.

## V. Discussion

This work presents four innovative points:
- CRISP-DM Methodology Integrated with DPIA: Integrating DPIA into the CRISP-DM methodology ensures compliance with data protection regulations, providing a robust framework to manage privacy risks throughout the project lifecycle.
- Use of Synthetic Data: Synthetic data allowed us to generate the large volumes necessary to train balanced models without compromising privacy. The added randomizations improve the generalization capacity of the models, partly explaining the good results obtained.
- Simple and Effective Models: Using simple models focused on the strengths of the algorithms and the weaknesses of each fraud attempt offers an innovative and effective solution. Instead of relying on a single complex solution, this modular strategy allows for more flexible adaptation and updating.
- Sequential Modular Pipeline: Implementing a sequential modular pipeline optimized for Type I and Type II error costs allows for integrating multiple specialized models. This approach improves the accuracy and robustness of the fraud detection system and makes it easier to maintain and scale.

The results obtained surpass the company's current methods. The synthetic data generated, with appropriate randomizations, has proven to be effective in improving the generalization of the models. However, the system's production results should be closer to the company's current numbers.

The methodology addresses a critical problem of identity theft in the financial sector, proposing an innovative solution. With the imminent release of a new Identity Card in Chile, a solution based on a single step would have become obsolete. This methodological approach allows for easy system modification, using existing data to train additional pipeline elements.
Although the results are promising, the system must be validated with customer-specific data for proper fine-tuning. Future research could improve synthetic data generation algorithms to make them even more realistic and extend the modular approach to other biometric verification and fraud detection applications.

## VI. Conclusion

This work presents a comprehensive approach to identity fraud detection in retail finance using synthetic data and modular model pipelines. The proposed methodology ensures compliance with data protection regulations and demonstrates significant improvements in fraud detection accuracy and operational efficiency.

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
