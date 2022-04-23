from turtle import pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import random
import statistics
import csv


df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
mean=statistics.mean(data)
print("reading time mean:-" ,mean)

def random_set_of_mean(counter):

    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    sampleMean=statistics.mean(dataset)
    return sampleMean

def setup():
    mean_list=[]
    for i in range(0 , 100):
        set_of_mean=random_set_of_mean(30)
        mean_list.append(set_of_mean)
    show_fig(mean_list)

def show_fig(mean_list):
    df=mean_list
    sampleMean=statistics.mean(df)
    fig=ff.create_distplot([df],["reading time"] ,show_hist=False)
    fig.add_trace(go.Scatter(x=[sampleMean,sampleMean],y=[0,1]))
    fig.show()

    sampleMean=statistics.mean(mean_list)
    print("sampling mean:-" ,sampleMean)

setup()    