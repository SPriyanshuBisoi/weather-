import requests
import tkinter as tk
from tkinter import font
from PIL import Image,ImageTk

root=tk.Tk()

root.resizable(0,0)
root.title("weather")


WIDTH=500
HEIGHT=620

def get_weather(city):
    weather_key="79de5817a4d223b536ce61a0f630a4b4"
    url='https://api.openweathermap.org/data/2.5/weather'
    params={'appid':weather_key, 'q':city, 'units':'Metric'}
    response=requests.get(url,params=params)
    report=response.json()
    
    label['text']=show_weather_report(report)


def show_weather_report(report):
    try:
        city_name= report['name']
        weather_condition= report['weather'][0]['description']
        temp= report['main']['temp']
        output= 'City: %s \nCondition: %s \nTemperature(°C): %s' %(city_name,weather_condition,temp)
    except:
        output='There was a problem\n while retrieving that information'
    return output


canvas=tk.Canvas(root,width=WIDTH,height=HEIGHT)
canvas.create_rectangle(0, 0, WIDTH, HEIGHT, fill="#46295d")
canvas.pack()


frame=tk.Frame(root,bg='#e9d1d1',bd=5)
frame.place(relx=0.5,rely=0.1,relheight=0.1,relwidth=0.75,anchor='n')

entry=tk.Entry(frame,font=('times new roman',20),bg='#966c8b')
entry.place(relheight=1,relwidth=0.7)

btn=tk.Button(frame,text="Get Weather",relief='raised',bg="#989bb0",font=('times new roman',12),command=lambda: get_weather(entry.get()))
btn.place(relx=0.72,relheight=1,relwidth=0.28)

low_frame=tk.Frame(root,bg='#e9d1d1',bd=5)
low_frame.place(relx=0.5,rely=0.25,relheight=0.65,relwidth=0.75,anchor='n')

bg_color='#966c8b'
label=tk.Label(low_frame,font=('times new roman',20),justify='center',bd=4)
label.config(font=40,bg=bg_color)
label.place(relheight=1,relwidth=1)

'''
weather_icon=tk.Canvas(label,bg=bg_color,bd=0,highlightthickness=0)
weather_icon.place(relx=0.75,rely=0,relwidth=1,relheight=0.5)
'''


root.mainloop()
