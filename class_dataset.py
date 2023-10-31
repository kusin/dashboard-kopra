# library ui-dashboard
import streamlit as st;

# library manipulation dataset
import pandas as pd;

# library manipulation array
import numpy as np;

# library data visualization
import plotly.express as px;
import plotly.graph_objects as go;

# define class dataset
class dataset:

    # method read dataset
    @staticmethod
    def get_dataset():
        df = pd.read_csv("dataset/ekstrasi-fitur-kopra-nonTelungkup.csv")
        return df
    
    # result supervised learning
    @staticmethod
    def get_result_supervised():
        df = pd.DataFrame({
            "K-NN": [0.717, 0.544, 0.799, 0.728, 0.837, 0.810, 0.842],
            "SVM": [0.701, 0.511, 0.788, 0.734, 0.853, 0.794, 0.842],
            "C45": [0.750, 0.560, 0.783, 0.745, 0.826, 0.810, 0.799],
            "GNB": [0.652, 0.457, 0.750, 0.685, 0.804, 0.739, 0.799],
            "LR": [0.669, 0.391, 0.777, 0.685, 0.821, 0.772, 0.821],
            "LDA": [0.723, 0.391, 0.750, 0.717, 0.799, 0.761, 0.804],
            "QDA" : [0.685, 0.424, 0.804, 0.728, 0.815, 0.788, 0.832]
        }, index=['1', '2', '3', '4', '5', '6', '7']) * 100
        return df
    
    # result ensemble learning
    def get_result_ensemble():
        df = pd.DataFrame({
            "KNN": [0.750, 0.592, 0.832, 0.755, 0.848, 0.804, 0.842],
            "SVM": [0.696, 0.522, 0.788, 0.734, 0.859, 0.783, 0.832],
            "C45": [0.766, 0.554, 0.799, 0.837, 0.880, 0.821, 0.864],
            "GNB": [0.658, 0.462, 0.750, 0.685, 0.799, 0.745, 0.799],
            "LR": [0.663, 0.397, 0.777, 0.696, 0.821, 0.772, 0.821],
            "LDA": [0.723, 0.391, 0.750, 0.717, 0.794, 0.766, 0.804],
            "QDA": [0.685, 0.424, 0.815, 0.734, 0.810, 0.788, 0.837],
        }, index=['1', '2', '3', '4', '5', '6', '7']) * 100
        return df
   
