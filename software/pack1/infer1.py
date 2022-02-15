
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.linear_model import Ridge, Lasso
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.base import TransformerMixin, BaseEstimator
import pandas as pd
import numpy as np
import warnings
import sys
import os



warnings.filterwarnings('ignore')


def resource_path(relative_path):
    if getattr(sys, 'frozen', False): #是否Bundle Resource
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)



class DataCleaner_v0(BaseEstimator, TransformerMixin):
    def __init__(self): # no *args and **kwargs
        super().__init__()
    
    def fit(self, X, y=None):
        return self  # nothing else to do
    
    def transform(self, X, y=None):   

        # Clean some punctutations
        data_temp=X.copy()
        data_temp = data_temp.str.replace('\n', ' \n ')
        # Remove ip address
        data_temp =    data_temp.str.replace(r'(([0-9]+\.){2,}[0-9]+)',' ')
        
        data_temp = data_temp.str.replace(r'([a-zA-Z]+)([/!?.])([a-zA-Z]+)',r'\1 \2 \3')
        # Replace repeating characters more than 3 times to length of 3
        data_temp= data_temp.str.replace(r'([*!?\'])\1\1{2,}',r'\1\1\1')
        # patterns with repeating characters 
        data_temp = data_temp.str.replace(r'([a-zA-Z])\1{2,}\b',r'\1\1')
        data_temp =data_temp.str.replace(r'([a-zA-Z])\1\1{2,}\B',r'\1\1\1')
        data_temp = data_temp.str.replace(r'[ ]{2,}',' ').str.strip()   
        # Add space around repeating characters
        data_temp =data_temp.str.replace(r'([*!?\']+)',r' \1 ')     
        return data_temp



title='''

  _____                  _             ____                                                  _             _   _                   _                 
 |_   _|   ___   __  __ (_)   ___     / ___|   ___    _ __ ___    _ __ ___     ___   _ __   | |_   ___    | | | |  _   _   _ __   | |_    ___   _ __ 
   | |    / _ \  \ \/ / | |  / __|   | |      / _ \  | '_ ` _ \  | '_ ` _ \   / _ \ | '_ \  | __| / __|   | |_| | | | | | | '_ \  | __|  / _ \ | '__|
   | |   | (_) |  >  <  | | | (__    | |___  | (_) | | | | | | | | | | | | | |  __/ | | | | | |_  \__ \   |  _  | | |_| | | | | | | |_  |  __/ | |   
   |_|    \___/  /_/\_\ |_|  \___|    \____|  \___/  |_| |_| |_| |_| |_| |_|  \___| |_| |_|  \__| |___/   |_| |_|  \__,_| |_| |_|  \__|  \___| |_|   
                                                                                                                                                     

'''

print('\n\n Welcome to:\n',title)


model_path=resource_path(os.path.join("res","0.pkl"))

with open(model_path,'rb') as fr:
    pipeline = pickle.load(fr)  

while 1:
    comment=input("Please input comment (Only in English !!):")   
    score=pipeline.predict(pd.Series([comment]))
    print("The commet's toxic score is:  ", str(round(score[0],3)))