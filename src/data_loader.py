import pandas as pd
import os

def load_netflix_data(filepath="data/raw/netflix_titles.csv"):
    if not os.path.exists(filepath):
        raise FileNotFoundError(
            f"Dataset not found at '{filepath}'.\n"
            "Please download it from: https://www.kaggle.com/datasets/shivamb/netflix-shows\n"
            "and place it in data/raw/"
        )

    df = pd.read_csv(filepath)
    print(f"Dataset loaded successfully!")
   
    print(f'shape: {df.shape}')
    return df

def get_basic_info(df):
    print(df.shape)
    print(df.info())
    print(df.isnull().sum())





    