import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import GlobalMaxPooling2D
from tensorflow.keras.applications.resnet50 import ResNet50,preprocess_input
import numpy as np
from numpy.linalg import norm
import os
from tqdm import tqdm #to view progress
import pickle

model = ResNet50(weights='imagenet',
                 include_top=False,
                 input_shape=(224, 224, 3))

model.trainable = False #fix weights

model = tf.keras.Sequential([
    model,
    GlobalMaxPooling2D()
])

#function to extract features from an image
def extract_features(img_path,model):
    img = image.load_img(img_path,target_size=(224,224))
    img_array = image.img_to_array(img)
    expanded_img_array = np.expand_dims(img_array, axis=0)
    preprocessed_img = preprocess_input(expanded_img_array)
    result = model.predict(preprocessed_img).flatten()
    normalized_result = result / norm(result)

    return normalized_result

#create a list of file names
filenames = []

for file in os.listdir('images'):
    filenames.append(os.path.join('images',file))

#extract features and store them in a list
feature_list = []

for file in tqdm(filenames):
    feature_list.append(extract_features(file,model))

#save the features and filenames in a pickle file
pickle.dump(feature_list,open('embeddings.pkl','wb'))
pickle.dump(filenames,open('filenames.pkl','wb'))
