import  tkinter as tk
from tkinter import  font
import requests

HEIGHT= 500
WIDTH= 600

#8fe82164ffe0c3ec7bb0524762873f50
#api.openweathermap.org/data/2.5/forecast?q={city name}&appid={your api key}

def format_response(wether):
    try:
        name = wether['name']
        desc = wether['weather'][0]['description']
        temp = wether['main']['temp']

        final_str= 'City: %s\n Conditions: %s\nTemperature(in Celcius):%s' %(name,desc,temp)
    except:
        final_str='There was a problem retrieving that information'

    return final_str

def test_function(entry):
    print("this is the entry",entry)

def get_weather(city):
    weather_key = '8fe82164ffe0c3ec7bb0524762873f50'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key,'q':city,'units': 'metric'}
    response = requests.get(url,params=params)
    wether = response.json()

    label['text'] =format_response(wether)

root= tk.Tk()
canvas= tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

background_image= tk.PhotoImage(file='landscape.png')
background_label= tk.Label(root, image=background_image)
background_label.place(relwidth=1,relheight=1)

frame = tk.Frame(root,bg='#80c1ff',bd=5)
frame.place(relx=0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

entry=tk.Entry(frame,font=('Courier',13))
entry.place(relwidth=0.65,relheight=1)

button=tk.Button(frame,text="Get weather",font=('Courier',12),command=lambda : get_weather(entry.get()))
button.place(relx=0.7,relheight=1,relwidth=0.3)

lower_frame = tk.Frame(root,bg='#80c1ff',bd=5)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.6,anchor='n')

label=tk.Label(lower_frame,font=('Courier',12),anchor='nw',justify='left',bd=4)
label.place(relwidth=1,relheight=1)


root.mainloop()