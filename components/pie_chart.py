import plotly.express as px
from dash import dcc, html, Input, Output

def render(app,data):
    @app.callback(
        Output("pie_chart", "children"),
        [
            Input("title-dropdown2", "value")
        ]
                )

    def update_pie_chart(titles):   #levels
        remote = data.groupby(["job_title","remote_ratio"])[["salary_in_usd"]].count()
        remote.reset_index(inplace=True)
        filtered_data = remote.query("job_title in @titles")    
        if filtered_data.shape[0] == 0:
            return html.Div("No data selected", id="pie_chart")
        fig = px.pie(filtered_data, 
                    values="salary_in_usd",
                    names="remote_ratio",
                    title="Remote work ratio"
                    )
        return html.Div(dcc.Graph(figure=fig), id="pie_chart")
    return html.Div(id="pie_chart")