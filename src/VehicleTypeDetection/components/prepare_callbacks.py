import time
import os
import tensorflow as tf
from src.VehicleTypeDetection.entity.config_entity import PrepareCallbackConfig

class PrepareCallbacks:
    def __init__(self,config:PrepareCallbackConfig):
        self.config=config

    def create_tb_callbacks(self):
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_running_log_directory=os.path.join(
            str(self.config.tensorboard_root_log_dir),  # Convert to string
            f"tb_logs_at_{timestamp}",
        )
        return tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_directory)
    
    def create_checkpoint_callback(self):
        checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
        filepath=str(self.config.checkpoint_model_filepath),
        save_best_only=True,
        )
        return checkpoint_callback
    
    def get_tb_ckpt_callbacks(self):
        return [
            self.create_tb_callbacks(),
            self.create_checkpoint_callback()
        ]
