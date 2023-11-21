import plotly.express as px
from dash import dcc, html, Input, Output

def render(app,data):
    @app.callback(
        Output("bar_chart", "children"),
        [
            Input("title-dropdown", "value")
        ]
                )

    def update_bar_chart(titles):   #levels
        mean_salary = data.groupby(["job_title"])[["salary_in_usd"]].mean().round(2)
        mean_salary.reset_index(inplace=True)
        mean_salary["mean_salary"]=mean_salary["salary_in_usd"]
        mean_salary.drop("salary_in_usd",axis=1,inplace=True)
        filtered_data = mean_salary.query("job_title in @titles")    #and experience_level in @levels
        if filtered_data.shape[0] == 0:
            return html.Div("No data selected", id="bar_chart")
        fig = px.bar(filtered_data, 
                    x="job_title",
                    y="mean_salary",
                    text_auto='.2s',
                    labels={"mean_salary":"Mean salary", "job_title":"Job title"}
                    )
        fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
        return html.Div(dcc.Graph(figure=fig), id="bar_chart")
    return html.Div(id="bar_chart")