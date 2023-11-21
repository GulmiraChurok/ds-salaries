import plotly.express as px
from dash import dcc, html, Input, Output

def render(app,data):
    @app.callback(
        Output("bar_chart_experience", "children"),
        [
            Input("title-dropdown2", "value")
        ]
                )

    def update_bar_chart(titles):   #levels
        mean_salary = data.groupby(["job_title","experience_level"])[["salary_in_usd"]].mean().round(2)
        mean_salary.reset_index(inplace=True)
        mean_salary["mean_salary"]=mean_salary["salary_in_usd"]
        mean_salary.drop("salary_in_usd",axis=1,inplace=True)
        filtered_data = mean_salary.query("job_title in @titles")    
        if filtered_data.shape[0] == 0:
            return html.Div("No data selected", id="bar_chart_experience")
        fig = px.bar(filtered_data, 
                    x="experience_level",
                    y="mean_salary",
                    color="experience_level",
                    title="Mean salary by experience level",
                    labels={"mean_salary":"Mean salary",
                            "experience_level":"Experience level",
                            },
                    category_orders={"experience_level":["EN", "MI", "SE", "EX"]}
                    )
        return html.Div(dcc.Graph(figure=fig), id="bar_chart_experience")
    return html.Div(id="bar_chart_experience")




# "EN":"Entry", "MI":"Mid", "SE":"Senior", "EX":"Executive"