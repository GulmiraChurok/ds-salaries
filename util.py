import pandas as pd

def get_data(PATH):
    df = pd.read_csv(PATH)
    df2 = df.loc[df['job_title'].isin(["Data Engineer","Data Scientist","Data Analyst",
                                       "Machine Learning Engineer","Applied Scientist",
                                       "Research Scientist","Analytics Engineer","Data Architect",
                                       "Business Intelligence Engineer","Data Manager","Research Engineer",
                                       "Data Science Manager"])]
    us = df2[df2['employee_residence']=="US"]
    us.reset_index(inplace=True)
   
    return us