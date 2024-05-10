# Handwritten Digits Recognition

<img src="https://th.bing.com/th/id/OIG.ieprritn78p5xfpmSIRL?pid=ImgGn" alt="Image" width="2000" height="600"> 

## Overview

This project demonstrates handwritten digits recognition using a neural network model. It includes training a model on the MNIST dataset and using it to predict custom images of handwritten digits.

## Table of Contents

- [Introduction](#introduction)
- [Dataset](#dataset)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Welcome to the Handwritten Digits Recognition project. This project showcases the recognition of handwritten digits using machine learning techniques. It includes training a neural network model on the MNIST dataset and using it to predict digits in custom images.

## Dataset

The project uses the MNIST dataset, a widely-used dataset for handwritten digit recognition tasks. The dataset contains a large number of grayscale images of handwritten digits (0-9) and corresponding labels.

## Getting Started

### Prerequisites

- Python (>=3.6)
- TensorFlow (>=2.0)
- NumPy
- OpenCV (cv2)
- Matplotlib

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/20481A5450/NumberRecognition.git
   cd  NumberRecognition
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Choose whether to train a new model or use an existing one by setting `train_new_model` in the script.

2. If training a new model, run the script:

   ```bash
   python NumberRecognition.py
   ```

3. If using an existing model, simply run the script:

   ```bash
   python NumberRecognition.py
   ```

4. Follow the prompts to input custom images of handwritten digits for recognition.

## Results

The project will display the predicted digit for each custom image along with a visualization of the image. The accuracy of the model on the MNIST test dataset is also displayed.

## Contributing

Contributions are welcome! If you'd like to improve this project or report issues, please submit a pull request or open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
