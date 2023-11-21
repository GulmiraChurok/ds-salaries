from dash import html
import dash_bootstrap_components as dbc
from components import job_title_dropdown, bar_chart, job_title_dropdown2, bar_chart_experience, pie_chart, bar_chart_size

def create_layout(app, data):
    return dbc.Container(
        [
           dbc.Row(dbc.Col(html.H2("Data Science Salary Project"))),
           dbc.Row(
                   [
                       dbc.Col([
                            job_title_dropdown.render(app,data), 
                       ],lg=4),
                       dbc.Col(bar_chart.render(app,data),lg=8)
                   ]
                   ),
              dbc.Row(
            [
                job_title_dropdown2.render(app,data)
            ]
                ,className="mt-4"),
            dbc.Row(
                   [
                        dbc.Col([
                            bar_chart_experience.render(app,data), 
                       ],lg=4),
                        dbc.Col(pie_chart.render(app,data),lg=4),
                        dbc.Col(bar_chart_size.render(app,data),lg=4),
                   ]
                   )
        ]
    )