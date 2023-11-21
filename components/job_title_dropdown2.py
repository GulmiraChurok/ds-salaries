from dash import html, dcc, Output, Input

def render(app, data):
    all_job_titles = data['job_title'].unique() 

    @app.callback(
        Output("title-dropdown2", "value"),
        Input("select-title-button2", "n_clicks")
    )

    def select_all_job_titles(n): 
        return all_job_titles
    dropdown = html.Div(
        [
            html.H6("Select a single job title for more information about that position"),
            dcc.Dropdown(
                options = [{"label":title, "value":title} for title in all_job_titles],
                multi=False,
                id = "title-dropdown2"
            ),
            html.Button(
                ["Select a job title"],
                n_clicks=0,
                id="select-title-button2"
            )
        ]
    )
    return dropdown