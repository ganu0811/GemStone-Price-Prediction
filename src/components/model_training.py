import pandas as pd
import numpy as np
from src.logger.logging import logging
from src.exception.exception import CustomException
import os
import sys
from dataclasses import dataclass
from pathlib import Path

from src.utils.utils import save_object, evaluate_model
from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet



@dataclass
class ModelTrainingConfig:
    trained_model_file_path = os.path.join('artifacts','trained_model.pkl')


class ModelTrainer:
    def __init__(self):
        self.model_training_config = ModelTrainingConfig()
    
    def initiate_model_training(self, train_array, test_array):
        try:
            logging.info('Splitting the dependent and independent variables')
            X_train, y_train, X_test, y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            
            models = {
                'LinearRegression': LinearRegression(),
                'Lasso': Lasso(),
                'Ridge': Ridge(),
                'ElasticNet': ElasticNet()
            }
            
            model_report:dict = evaluate_model(X_train,y_train,X_test,y_test,models)
            print(model_report)
            print('\n'*40)
            logging.info(f'Model Evaluation Report: {model_report}')
            
            # Saving the best model
            
            best_model_score = max(sorted(model_report.values()))
            
            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]
            
            best_model = models[best_model_name]
            print(f'Best Model: {best_model}, R2 Score: {best_model_score}')
            print('\n'*40)
            
            logging.info(f'Best Model: {best_model}')
            
            save_object(
                file_path= self.model_training_config.trained_model_file_path,
                obj=best_model
            )
        except Exception as e:
            logging.info('Exception occurred in model training')
            raise CustomException(e,sys)
    
    
    
