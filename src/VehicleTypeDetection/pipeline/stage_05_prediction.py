import tensorflow as tf
import os
import numpy as np
class PredictionPipeline:
    def __init__(self,user_input) -> None:
        self.user_input=user_input

    def prediction(self):
        model=tf.keras.models.load_model(os.path.join("artifacts","training","trained_model.h5"))
        image_for_prediction=self.user_input

        test_image = tf.keras.preprocessing.image.load_img(image_for_prediction, target_size = (224,224))
        test_image = tf.keras.preprocessing.image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis=1)

        if result[0] == 1:
            prediction = 'Car'
            return [{ "The following vehicle is" : prediction}]
        elif result[0] == 2:
            prediction = 'Truck'
            return [{ "The following vehicle is" : prediction}]
        elif result[0] == 3:
            prediction = 'motorcycle'
            return [{ "The following vehicle is " : prediction}]
        else:
            prediction = 'Bus'
            return [{ "The following vehicle is" : prediction}]