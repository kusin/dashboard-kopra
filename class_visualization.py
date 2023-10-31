# library ui-dashboard
import streamlit as st;

# library manipulation dataset
import pandas as pd;

# library manipulation array
import numpy as np;

# library data visualization
import plotly.express as px;
import plotly.graph_objects as go;

class visualization:
     
    # func line_plot
    @staticmethod
    def line_plot(df, title):
        
        # define a new figure
        fig = go.Figure();

        # line plot with plotly
        for column in df.columns:
            fig.add_trace(go.Scatter(x=df.index, y=df[column], mode='lines+markers', name=column))

        # Menetapkan judul dan nama sumbu
        fig.update_layout(
            title=title,
            xaxis_title="Experiment", 
            yaxis_title="", 
            yaxis=dict(range=[0, 100]),
            legend=dict(orientation="h", yanchor="top", y=1, xanchor="right", x=1)
        )

        # return values
        return fig;