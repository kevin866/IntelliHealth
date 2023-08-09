from utils.utils import ModelPrediction


class ModelService:
    def __init__(self, model_prediction_bean):
        self.model_prediction = model_prediction_bean

    def predict(self, x_input):
        return self.model_prediction.predict(x_input)
