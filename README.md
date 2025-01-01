# Teeth Disease Detection using Computer Vision

A computer vision project that utilizes transfer learning to classify dental images into one of seven teeth diseases or none. The model leverages the VGG16 architecture and achieves an impressive accuracy of 97%. This project includes data preprocessing, visualization, augmentation, and a scalable deployment using Flask API and Docker.

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

### Prerequisites
- Python 3.7 or above
- Docker

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/teeth-disease-detection.git
   cd teeth-disease-detection
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
   The application will be accessible at `http://127.0.0.1:5000`.

2. **Docker Deployment:**
   Build and run the Docker container:
   ```bash
   docker build -t teeth-disease-detection .
   docker run -p 5000:5000 teeth-disease-detection
   ```
   The application will be accessible at `http://127.0.0.1:5000`.

## Project Structure
- `data/`: Contains sample dental images (add your dataset here).
- `models/`: Pretrained VGG16 model and saved weights.
- `notebooks/`: Jupyter notebooks for preprocessing and visualization.
- `app.py`: Flask application file for model inference.
- `Dockerfile`: Docker configuration file for containerizing the application.
- `requirements.txt`: List of dependencies.

## Results
The model achieved a classification accuracy of **97%**, making it a reliable tool for detecting teeth diseases.

## Future Improvements
- Add support for more diseases and larger datasets.
- Improve model interpretability using Grad-CAM.
- Enhance deployment with Kubernetes for scalable cloud deployment.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements
- The VGG16 architecture was pivotal in achieving high accuracy.
- Thanks to the open-source libraries and tools that made this project possible.
