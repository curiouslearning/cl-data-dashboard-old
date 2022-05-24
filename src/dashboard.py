
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df = pd.read_csv(
    'complete_count.csv')

fig = px.scatter(df, x="date", y="count")
fig.update_traces(mode='lines+markers')
fig.update_xaxes(showgrid=False)
fig.update_yaxes(showgrid=False, type='linear')

app.layout = html.Div([
    html.Div(
        className="app-header",
        children=[
            html.Div('Curious Learning Dashboard', className="app-header--title")
        ]
    ),
    html.H1('Completed Assessments'),
    html.H1(df['count'].sum()),
    dcc.Graph(
        id='Assessments Completed',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port=int("8050"), debug=False)
