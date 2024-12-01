import plotly.graph_objects as go
import pandas as pd

# Data for the Pareto chart
categories = ['A', 'B', 'C', 'D', 'E', 'F']
values = [50, 30, 15, 10, 5, 2]  # Example values

# Sort values and calculate cumulative percentage
data = pd.DataFrame({'categories': categories, 'values': values}).sort_values(by='values', ascending=False)
data['cumulative'] = data['values'].cumsum() / data['values'].sum() * 100

# Set canvas dimensions
canvas_width = 1000
canvas_height = int(canvas_width * 0.3)

# Create the Pareto chart
fig = go.Figure()

# Add bar trace for frequency (left y-axis)
fig.add_trace(
    go.Bar(
        x=data['categories'],
        y=data['values'],
        name='Frequency',
        marker=dict(
            color='#FFCC80',  # Light orange color
            line=dict(color='black', width=1.5)
        ),
        text=data['values'],  # Data labels
        textposition='outside',  # Position text above the bars
        yaxis='y1'  # Assign to left y-axis (default)
    )
)

# Add line trace for cumulative percentage (right y-axis)
fig.add_trace(
    go.Scatter(
        x=data['categories'],
        y=data['cumulative'],
        name='Cumulative Percentage',
        mode='lines+markers+text',  # Add text to line points
        marker=dict(color='red'),
        line=dict(shape='linear'),
        text=[f"{val:.1f}%" for val in data['cumulative']],  # Data labels
        textposition='top center',  # Position text above points
        yaxis='y2'  # Assign to right y-axis
    )
)

# Update layout with a border and background settings
fig.update_layout(
    title='Pareto Chart with Black Canvas Border',
    xaxis_title='Categories',
    yaxis=dict(
        title='Frequency',
        side='left',  # Place on the left side of the plot
        rangemode='tozero'  # Ensures the y-axis starts at 0
    ),
    yaxis2=dict(
        title='Cumulative Percentage',
        overlaying='y',  # Overlay the right axis with the left one
        side='right',  # Place on the right side of the plot
        range=[0, 100],  # Fixed range for cumulative percentage
    ),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
    bargap=0.2,
    width=canvas_width,  # Set canvas width
    height=canvas_height,  # Set canvas height
    paper_bgcolor='white',  # Set the background color
    plot_bgcolor='white',  # Ensure plot area has the same background
)

# Add a black border using annotations
fig.update_layout(
    margin=dict(l=10, r=10, t=10, b=10),  # Minimal margins
    annotations=[
        dict(
            x=900*.5,
            y=900,
            xref="paper",
            yref="paper",
            showarrow=False,
            text="",
            xanchor="center",
            yanchor="middle",
            font=dict(size=1),
            bordercolor="black",
            borderwidth=2,
        )
    ],
)

# Show the plot
fig.show()
