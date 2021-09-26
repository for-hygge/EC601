# Project 1: RSNA-MICCAI Brain Tumor Radiogenomic Classification 

## Problem statement
   ### o	What does this topic cover?
      
      The main content of this topic is to compare the MRI scan results of the brain with empirical data to detect the presence of MGMT promoter methylation, thereby classifying and identifying the status of malignant brain tumors and assisting doctors in the diagnosis and treatment of brain cancer[1].

   ### o	Why is it important? 
      
      1.    Unpredictable-- Overgrowth of abnormal cells in the brain accumulate to form brain tumors. The shape, size, and location of the brain tumors are all unpredictable, as well as the direction of spread. Brain tumors can be malignant or benign. Although not all of them can cause cancer, they all increase intracranial pressure and cause certain damage to the brain[1], [2].
      
      2.	Life-threatening-- The World Health Organization (WHO) classified more than 120 classes of brain tumors in four levels according to the level malignancy[3]. Glioblastoma, the most generic form of primary malignant brain tumors, the five-year relative survival rate of which is only 7.2% and median survival is only 8 months[4].
      
      3.	Difficult to classify-- Recognizing the type and exact location of tumors artificially relies heavily on experience accumulation, especially when it is difficult to define the boundaries of tumors, and the probability of misjudgment is high.

      4.	Complex and time-consuming surgeries-- The current genetic analysis method requires a series of surgeries to extract tissue samples. It takes several weeks to detect genetic feature and compare the test results with the original symptom types, and then repeat the subsequent surgical extraction and testing. However, MRI scans provide a helpful solution. If doctors can obtain tumor information by processing MRI scans of the patients’ brains, they can get results faster. And for the patient, this method will not only reduce their pain, but also let them get better diagnosis and treatment.

## Applications
   ### o	What are applications of the topic? 
      
      This topic is generally used in medical field, especially in classifying and treating cancerous tumors.
   
   ### o	What is the societal significance of the research?  
      
      As discussed above, malignant tumors have a significant impact on people's lives, and they are also one of the problems that need to be solved urgently in the medical field. Therefore, advancing this research can not only bring innovative ideas to traditional medicine and promote the advancement of medicine, but also bring hope of survival to patients from all over the world.

## Pick an area of focus that interests you in the topic
   I am very interested in how to extract information by denoising images and how to accurately classify the training data into different classes.

## Literature review 
   A basic procedure of this research consists of five steps. Firstly, researchers need to obtain data. Then, they preprocess these images--usually denoise them. Next, they choose some data as samples and create a model to pre-train these data and label them. After that, the rest data will be trained and compared with the samples in order to optimize the model. Finally, researchers predict on test set with best model.  
   
   The most common method of image processing is digital signal filtering and feature extraction. The aim is to remove as much noise as possible in images. Among them, the wavelet transform is the most popular because of its advantages of retaining frequency and position information at the same time. The wavelet transform can learn each element with a resolution adapted to its state[5]. To optimizing processing, Principal Component Analysis (PCA) is used to prevent overfitting by reducing dimensionality of the predictor space[7][8]. Besides, Otsu[9] promoted a method which reduces a grey-level image into a binary image, so that it is easier to calculate and classify the most essential information and intuitively represent it in a histogram.  
   
   The application of machine learning algorithms for data set training is widely adopted by scientific researchers because machine learning has shown good performance in data classification. Many researchers applied Support Vector Machine (SVM) to train the data[3][10]. In [11], Convolutional Neural Network (CNN) is chosen together with SVM to do the extraction based on the depth of feature.

## Open-Source research
   Famous open-source projects: the MONAI framework, TorchIO, CaPTK.  
   
   *  the MONAI framework[12]: The MONAI framework is the open-source foundation being created by Project MONAI. MONAI is a freely available, community-supported, PyTorch-based framework for deep learning in healthcare imaging. It provides domain-optimized foundational capabilities for developing healthcare imaging training workflows in a native PyTorch paradigm. Project MONAI also includes MONAI Label, an intelligent open source image labeling and learning tool that helps researchers and clinicians collaborate, create annotated datasets, and build AI models in a standardized MONAI paradigm. 
   
   *  TorchIO[13]: TorchIO is a Python library for efficient loading, preprocessing, augmentation and patch-based sampling of 3D medical images in deep learning, following the design of PyTorch.  
   
   *  CaPTK[14]: CaPTk is a software platform for analysis of radiographic cancer images, currently focusing on brain, breast, and lung cancer. CaPTk integrates advanced, validated tools performing various aspects of medical image analysis, which have been developed in the context of active clinical research studies and collaborations toward addressing real clinical needs. With emphasis given in its use as a very lightweight and efficient viewer, and with no prerequisites for substantial computational background, CaPTk aims to facilitate the swift translation of advanced computational algorithms into routine clinical quantification, analysis, decision making, and reporting workflow. Its long-term goal is providing widely used technology that leverages the value of advanced imaging analytics in cancer prediction, diagnosis and prognosis, as well as in better understanding the biological mechanisms of cancer development.

## Duplicate the results 
   I have not yet duplicate the results. However, I found there are lots of open-source researches related to this topic on the Internet.  
   
   The following projects are all from the participants in the KAGGLE competition and the data is provided by the Radiological Society of North America (RSNA), the Medical Image Computing and Computer Assisted Intervention Society (the MICCAI Society) and the Medical Image Computing and Computer Assisted Interventions (MICCAI) society.  
   1.	Brain Tumor - Transfer Learning - FLAIR – Kfold[15]  
      In this project, in terms of image processing, Michael cropped images to reduce black borders, resized them, applied denoising filter and converted each image in 3D array.  
      In terms of classification, he used LSTM—one of RNNs to take into account the past elements of our sequence of images.
   
   2.	[RSNA-MICCAI] Monai - ensemble[16]  
      In this project, Michal used stacked images (3D) and Densenet121 3D model to train the data. The dataset he used contains a code of the framework MONAI which is a PyTorch-based, open-source framework for deep learning in healthcare imaging.
   
   There are also many good projects which are similar to our topic on GitHub.I will search more and learn from them.
   
## Reference: 
[1] 	https://www.kaggle.com/c/rsna-miccai-brain-tumor-radiogenomic-classification/overview/description  
[2]	  https://www.healthline.com/health/brain-tumor#treatment  
[3] 	M. Gurbină, M. Lascu and D. Lascu, "Tumor Detection and Classification of MRI Brain Image using Different Wavelet Transforms and Support Vector Machines," 2019 42nd International Conference on Telecommunications and Signal Processing (TSP), 2019, pp. 505-508, doi: 10.1109/TSP.2019.8769040.  
[4] 	https://braintumor.org/brain-tumor-information/brain-tumor-facts/?gclid=Cj0KCQjwv5uKBhD6ARIsAGv9a-wqPD5yoTQSBuCO-szDg-uXQDueP6VP41yYT1NuY2NZsxzLCcYc4pUaAnZEEALw_wcB  
[5] 	Kociołek, Marcin, et al. "Discrete wavelet transform-derived features for digital image texture analysis." international conference on signals and electronic systems. 2001.  
[6] 	Patil, Rajesh C., and A. S. Bhalchandra. "Brain tumour extraction from MRI images using MATLAB." International Journal of Electronics, Communication and Soft Computing Science & Engineering (IJECSCSE) 2.1 (2012): 1.  
[7]	  Xu, Yansun, et al. "Wavelet transform domain filters: a spatially selective noise filtration technique." IEEE transactions on image processing 3.6 (1994): 747-758.  
[8]	  Subashini, M. Monica, and Sarat Kumar Sahoo. "Brain MR image segmentation for tumor detection using artificial neural networks." Int. J. Eng. Technol 5.2 (2013): 925-933.  
[9]	  Otsu, Nobuyuki. "A threshold selection method from gray-level histograms." IEEE transactions on systems, man, and cybernetics 9.1 (1979): 62-66.  
[10]	Amin, Javeria, et al. "A distinctive approach in brain tumor detection and classification using MRI." Pattern Recognition Letters 139 (2020): 118-127.  
[11]	S. K. Baranwal, K. Jaiswal, K. Vaibhav, A. Kumar and R. Srikantaswamy, "Performance analysis of Brain Tumour Image Classification using CNN and SVM," 2020 Second International Conference on Inventive Research in Computing Applications (ICIRCA), 2020, pp. 537-542, doi: 10.1109/ICIRCA48905.2020.9183023.  
[12]	https://monai.io/  
[13]	https://torchio.readthedocs.io/  
[14]	https://www.med.upenn.edu/cbica/captk/  
[15]	https://www.kaggle.com/michaelfumery/brain-tumor-transfert-learning-flair-kfold  
[16]	https://www.kaggle.com/mikecho/rsna-miccai-monai-ensemble  
[17]	https://www.kaggle.com/dschettler8845/captk-brats-preprocessing-cleaned-commented  

