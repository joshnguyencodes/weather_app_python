#import required modules
import requests
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


api_key = "61ef8fc4c490b06b0f2c87a9f145ffa6"
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'


# explicit function to get
# weather details
def get_weather( city ):
    result = requests.get( url.format( city, api_key ) )
    if result:
        json = result.json()
        print(json) # get students to have a look at the data we are given
        city = json['name']
        country = json['sys']['country']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        weather1 = json['weather'][0]['main']
        final = [city, country, temp_kelvin,
                 temp_celsius, weather1]
        return final
    else:
        print("NO Content Found")



# search city
def search( ):
    city = city_entry.get()
    weather = get_weather( city )

    if weather:
        location_lbl['text'] = '{} ,{}'.format( weather[0], weather[1] )
        temperature_label['text'] = str( round(weather[3],1) ) + " Degree Celsius"
        weather_l['text'] = weather[4]
    else:
        messagebox.showerror( 'Error', "Cannot find {}".format( city ) )


#UI

app = Tk()
# add title
app.title( "Weather App" )
# adjust window size
app.geometry( "300x300" )

title_lbl = Label( app, text="Weather", font='normal 36', fg='purple' )
title_lbl.pack()

# add labels, buttons and text
city_entry = Entry( app )
city_entry.pack()

Search_btn = Button( app, text="Search Weather",
                     width=12, command=search )
Search_btn.pack()

location_lbl = Label( app, text="Location", font={ 'bold', 20 } )
location_lbl.pack()

temperature_label = Label( app, )
temperature_label.pack()

weather_l = Label( app, text="" )
weather_l.pack()

weather_icon = Label( app )
weather_icon.pack()


app.mainloop()
