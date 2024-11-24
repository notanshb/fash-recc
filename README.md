# Fashion Recommender System

This project is a Fashion Recommender System that uses a pre-trained ResNet50 model to extract features from images and recommend similar fashion items. The system allows users to upload an image and receive recommendations for similar items based on the uploaded image.

## Getting Started

To get started with this project, follow the instructions below.

### Prerequisites

- Python 3.7 or higher
- Required Python packages (listed in `requirements.txt`)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/fashion-recommender.git
    cd fashion-recommender
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

### Dataset

1. Download a fashion dataset from Kaggle. You can use any fashion dataset that contains images of clothing items. For example, you can use the "Fashion Product Images" dataset.

2. Create a folder named `images` in the project directory and save the downloaded images in this folder.

### Running the Streamlit App

You have two options to run the Streamlit app:

1. **Train your own model**:
    - Extract features from the images and save them in pickle files:
        ```sh
        python app.py
        ```
    - Run the Streamlit app:
        ```sh
        streamlit run main.py
        ```

2. **Use pre-trained weights**:
    - If you have pre-trained weights, you can directly run the Streamlit app:
        ```sh
        streamlit run main.py
        ```

3. Open your web browser and go to `http://localhost:8501` to access the Fashion Recommender System.

### Usage

1. Upload an image of a fashion item using the file uploader.
2. The system will display the uploaded image and recommend similar items based on the uploaded image.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Feel free to customize this README file as needed for your project.
