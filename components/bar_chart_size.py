import plotly.express as px
from dash import dcc, html, Input, Output

def render(app,data):
    @app.callback(
        Output("bar_chart_size", "children"),
        [
            Input("title-dropdown2", "value")
        ]
                )

    def update_bar_chart(titles):   #levels
        mean_salary = data.groupby(["job_title","company_size"])[["salary_in_usd"]].mean().round(2)
        mean_salary.reset_index(inplace=True)
        mean_salary["mean_salary"]=mean_salary["salary_in_usd"]
        mean_salary.drop("salary_in_usd",axis=1,inplace=True)
        filtered_data = mean_salary.query("job_title in @titles")    
        if filtered_data.shape[0] == 0:
            return html.Div("No data selected", id="bar_chart_size")
        fig = px.bar(filtered_data, 
                    x="company_size",
                    y="mean_salary",
                    color="company_size",
                    title="Mean salary by company size",
                    category_orders={"company_size": ["S", "M", "L"]}
                    )
        return html.Div(dcc.Graph(figure=fig), id="bar_chart_size")
    return html.Div(id="bar_chart_size")