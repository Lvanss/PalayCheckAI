# PalayCheck AI
### An AI-Assisted Paddy Leaf Disease Classification System Using MobileNetV2

PalayCheck AI is an Artificial Intelligence-assisted image classification system designed to classify paddy leaf images into disease and condition categories using a trained MobileNetV2 deep learning model.

The application allows users to upload a paddy leaf image and receive a predicted class, a model confidence score, and the top three predictions. It is developed for educational and experimental purposes as a project for **CPE126-4: Introduction to Artificial Intelligence**.

## Project Objectives

- Develop an AI-assisted paddy leaf disease classification system using MobileNetV2.
- Apply image preprocessing techniques, including resizing and normalization.
- Train and evaluate a deep learning image classification model.
- Integrate the trained model into a usable application.
- Demonstrate the practical application of Artificial Intelligence and computer vision in agriculture.

## Features

- Paddy leaf image upload.
- Classification into 10 disease and condition categories.
- Predicted class and model confidence score.
- Display of the top three predictions.
- Locally running application with offline inference after setup or packaging.

## Supported Classes

The model is configured to predict the following categories:

1. Bacterial Leaf Blight
2. Bacterial Leaf Streak
3. Bacterial Panicle Blight
4. Blast
5. Brown Spot
6. Dead Heart
7. Downy Mildew
8. Hispa
9. Normal
10. Tungro

## Technologies Used

- Python
- TensorFlow and Keras
- MobileNetV2
- NumPy
- Pillow
- Streamlit
- Jupyter Notebook
- PyInstaller for executable packaging

## Project Structure

```text
PalayCheckAI/
├── app.py
├── launcher.py
├── requirements.txt
├── README.md
├── .gitignore
├── model_outputs/
│   ├── palaycheck_mobilenetv2_best.keras
│   └── palaycheck_mobilenetv2_finetuned.keras
├── Rivera_Noble_CPE126-4_FOPI01_PalayCheckAI_MainProject.ipynb
├── Rivera_Noble_CPE126-4_FOPI01_ProjectSprint1.ipynb
├── sample_augmented_images/
├── train.csv
└── sample_submission.csv
```

The original and processed image datasets are maintained separately because of their size. Refer to the dataset section below.

## Dataset

The project uses the **Paddy Doctor / Paddy Disease Classification** image dataset.

The original and processed dataset folders, along with the dataset archive, are not included in this GitHub repository because of their large size. Obtain the dataset from its original authorized source and arrange the files according to the paths used in the project notebook.

Dataset source: [Paddy Doctor — Kaggle](https://www.kaggle.com/competitions/paddy-disease-classification)

## Installation and Usage

### Option 1: Run from Source

1. Install a compatible Python environment.
2. Clone or download this repository.
3. Open a terminal in the project directory.
4. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Ensure that `model_outputs/palaycheck_mobilenetv2_best.keras` exists.
6. Start the application:

   ```bash
   streamlit run app.py
   ```

7. Open the local URL displayed in the terminal and upload a paddy leaf image.

### Option 2: Run the Packaged Application

A packaged Windows application can be distributed separately from the source repository. Keep the complete `PalayCheckAI` output folder produced by PyInstaller together when distributing the executable.

Launch `PalayCheckAI.exe` to open the application in the default browser.

The packaged application can perform inference offline when its required dependencies and model are included correctly. Internet access is not required for local inference.

## Model and Evaluation

The application loads the trained model from:

`model_outputs/palaycheck_mobilenetv2_best.keras`

The main project notebook documents the model development and evaluation workflow. Refer to the notebook for the actual training configuration and evaluation results.

## Limitations

- Predictions are based on visual patterns learned from the training dataset.
- Model confidence scores do not guarantee prediction correctness.
- Image quality, lighting, background, and differences between field conditions and training images may affect predictions.
- The application is intended for educational and experimental use and should not replace professional agricultural diagnosis.

## Academic Context

**Course:** CPE126-4 — Introduction to Artificial Intelligence  
**Project:** PalayCheck AI: An AI-Assisted Paddy Leaf Disease Classification System Using MobileNetV2  
**Developers:** Lester Van E. Rivera and Robemar L. Noble

## License

No open-source license has been specified for this repository. Contact the project authors for permission before redistributing or modifying the project outside its intended academic use.
