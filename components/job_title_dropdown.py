from dash import html, dcc, Output, Input

def render(app, data):
    all_job_titles = data['job_title'].unique() #to have an array of allavailable years

    @app.callback(
        Output("title-dropdown", "value"),
        Input("select-title-button", "n_clicks")
    )

    def select_all_job_titles(n):  #n is number of clicks
        return all_job_titles
    dropdown = html.Div(
        [
            html.H6("Select job titles to compare average salary"),
            dcc.Dropdown(
                options = [{"label":title, "value":title} for title in all_job_titles],
                multi=True,
                id = "title-dropdown"
            ),
            html.Button(
                ["Select All"],
                n_clicks=0,
                id="select-title-button"
            )
        ]
    )
    return dropdown