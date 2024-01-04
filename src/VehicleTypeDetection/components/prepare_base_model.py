import tensorflow as tf
from pathlib import Path
from src.VehicleTypeDetection.config.configuration import PrepareBaseModelConfig

class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig) -> None:
        self.config = config

    @staticmethod
    def create_base_model(input_shape, num_classes, learning_rate, kernel_size):
        model = tf.keras.Sequential([
        tf.keras.layers.Rescaling(1./255, input_shape=input_shape),
        tf.keras.layers.Conv2D(32, kernel_size, padding="same", activation='relu'),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Conv2D(32, kernel_size, padding="same", activation='relu'),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Conv2D(32, kernel_size, padding="same", activation='relu'),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(num_classes, activation="softmax")
        ])

        model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
            loss=tf.keras.losses.SparseCategoricalCrossentropy(),
            metrics=['accuracy']
        )

        return model
    
    def get_base_model(self):
        self.model=self.create_base_model(
            input_shape=self.config.input_shape,
            num_classes=self.config.num_classes,
            kernel_size=self.config.kernel_size,
            learning_rate=self.config.learning_rate
        )
        self.save_model(path=self.config.base_model_path,model=self.model)

    
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)
