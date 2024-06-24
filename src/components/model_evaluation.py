import pandas as pd
import numpy as np
from src.logger.logging import logging
from src.exception.exception import CustomException
import os
import sys
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn


from dataclasses import dataclass
from pathlib import Path


@dataclass
class ModelEvaluationConfig:
    pass


class ModelEvaluation:
    def __init__(self):
        pass
    
    def initiate_model_evaluation(self):
        try:
            pass
        
        except Exception as e:
            logging.info()
            raise CustomException(e,sys)
    
    
    
