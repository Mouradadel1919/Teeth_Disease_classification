# Teeth Disease Detection using Computer Vision

A computer vision project that utilizes transfer learning to classify dental images into one of seven teeth diseases or none. The model leverages the VGG16 architecture and achieves an impressive accuracy of 97%. This project includes data preprocessing, visualization, augmentation, and a scalable deployment using Flask API and Docker.





https://github.com/user-attachments/assets/89ffddaf-536a-4944-809e-9b9b049ef691





## Features
- Preprocessing, visualization, and augmentation of dental images.
- Classification of dental images into 7 diseases or none using a transfer learning-based VGG16 model.
- Achieved a model accuracy of 97%.
- Deployed the model using Flask API.
- Dockerized the application for efficient deployment and scalability.

## Technologies Used
- **Programming Language:** Python
- **Libraries and Frameworks:** TensorFlow, Keras, OpenCV, NumPy, Matplotlib
- **Deployment Tools:** Flask, Docker

## Getting Started

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Mouradadel1919/Teeth_Disease_classification.git
   cd Teeth_Disease_classification
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
1. **Local Deployment:**
   ```bash
   python app.py
   ```
   The application will be accessible at `http://127.0.0.1:8080`.

2. **Docker Deployment:**
   Pull and run the Docker container from Docker Hub:
   https://hub.docker.com/repository/docker/mouradadel313/teeth_disease_classification/tags
   ```bash
   docker pull mouradadel313/teeth_disease_classification:latest
   docker run -p 8080:8080 mouradadel313/teeth_disease_classification:latest
   ```
   The application will be accessible at `http://127.0.0.1:8080`.

## Project Structure
- `data`: https://drive.google.com/drive/folders/1rC57JNtp8xfx2HkSdTzQN9osGuBe-spX?usp=sharing
- `app.py`: Flask application file for model inference.
- `Dockerfile`: Docker configuration file for containerizing the application.
- `requirements.txt`: List of dependencies.

## Results
The model achieved a classification accuracy of **97%**, making it a reliable tool for detecting teeth diseases.
