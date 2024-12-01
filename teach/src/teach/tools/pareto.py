import plotly.graph_objects as go
from typing import List
import numpy as np
import pandas as pd
import streamlit as st
from crewai_tools import BaseTool


class CustomParetoPlotter(BaseTool): 
    # Data for the Pareto chart
    name str: "CustomParetoPlotter"
    description str: "collect data and plot pareto chart"
    categories = ['Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Purple', 'Pink', 'Brown', 'Gray', 'Black', 'White']
    values = [50, 30, 15, 10, 5, 2, 40, 32, 84 ,82, 10]  # Example values

    def __init__(self, categories: List[str], values: List[str], **kwargs):
        super().__init__(**kwargs)
        self.categories = categories
        self.values = values
        
    def _pareto(self, categories:List, values:List):
        # Sort values and calculate cumulative percentage
        data = pd.DataFrame({'categories': categories, 'values': values}).sort_values(by='values', ascending=False)
        data['cumulative'] = round(data['values'].cumsum() / data['values'].sum() * 100)

        # Identify the 80% threshold
        threshold = 80
        data['highlight'] = data['cumulative'] <= threshold

        # Create the Pareto chart
        fig = go.Figure()

        # Add bar trace for values, highlighting 80/20
        fig.add_trace(
            go.Bar(
                x=data['categories'],
                y=data['values'],
                name='Frequency',
                marker=dict(
                    color='#FFCC80',
                    line=dict(color='grey', width=2)  # Set border color and width
                ),
                text=data['values'],
                textposition='auto',
                width=1.0,
                yaxis='y1'
            )
        )


        # Add line trace for cumulative percentage
        fig.add_trace(
            go.Scatter(
                x=data['categories'],
                y=data['cumulative'],
                name='Cumulative Percentage',
                mode='lines+markers+text',
                marker=dict(color='black'),
                text=[f"{val:.0f}%" for val in data['cumulative']], 
                textposition='top left',
                line=dict(shape='linear'),
                yaxis='y2'
            )
        )

        # Update layout to adjust dual y-axis
        fig.update_layout(
            title='Pareto Chart with Dynamic Left Y-Axis and Fixed Right Y-Axis',
            title_x=0.2,
            xaxis=dict(
                # title='Categories',
                # showline=True,  # Show the x-axis line
                linecolor='black',  # Set the x-axis line color to black
                linewidth=2,  # Set the x-axis line width
                zeroline = True,
            ),
            yaxis=dict(
                title='Occurance in Minutes',
                side='left',  # Place on the left side of the plot
                showline=True,  # Show the x-axis line
                linecolor='black',  # Set the x-axis line color to black
                linewidth=2, 
                ticklen=0,
                # zeroline=True,
                # Dynamically adjust range based on the bar values
                range=[0,(360*1.1)]#data['values'][0]*5]  # Ensures the y-axis starts at 0
            ),
            yaxis2=dict(
                title='Cumulative Percentage',
                overlaying='y',  # Overlay the right axis with the left one
                side='right',  # Place on the right side of the plot
                range=[0, 110],  # Fixed range for cumulative percentage
                showline=True,  # Show the x-axis line
                linecolor='black',  # Set the x-axis line color to black
                linewidth=2, 
                # zeroline=True,
                ticklen=0,
            ),
            legend=dict(orientation="h", yanchor="middle", y=-0.2, xanchor="right", x=0.7),
            bargap=0.2,
            width=1000,  # Set canvas width
            height=1000*.4 ,
            paper_bgcolor='white',  # Set the background color
            plot_bgcolor='white',  # Ensure plot area has the same background
        )
        return fig
        
        def _run(self):
            self._pareto(self.categories, self.values)
            return "plotted successfully"



# st.title("Pareto Chart Example")
# st.plotly_chart(pareto(categories, values))
