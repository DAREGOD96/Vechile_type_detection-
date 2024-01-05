import tensorflow as tf
from pathlib import Path
from src.VehicleTypeDetection.utils.common import save_json
from src.VehicleTypeDetection.entity.config_entity import ModelEvaluationConfig
class Evaluation:
    def __init__(self, config:ModelEvaluationConfig):
        self.config=config

    def train_validaiton_data_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.20
        )

        dataflow_kwargs = dict(
            target_size=self.config.input_shape[:-1],
            batch_size=self.config.batch_size,
            interpolation="bilinear"
        )

        validation_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = validation_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

    @staticmethod
    def _load_model(path:Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    
    def model_evaluation(self) -> None:
        trained_model=self._load_model(self.config.model_path)
        self.train_validaiton_data_generator()
        self.score=trained_model.evaluate(self.valid_generator)

    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path=Path("scores.json"), data=scores)
