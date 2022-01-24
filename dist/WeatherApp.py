import tkinter
import requests
from tkinter import *
from PIL import Image, ImageTk
# from yahoo_weather.weather import YahooWeather
# from yahoo_weather.config.units import Unit

HEIGHT = 750
WIDTH = 750

unit_cel = '(°C)'
unit_far = '(°F)'

# api.openweathermap.org/data/2.5/weather?q={city name},{country code}
# api key: 8c7bce9575359167d87d3a46d74cefc6

# app id: pmaQw17c
# client id: dj0yJmk9UkloMXE5RGUweU5NJnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PTZm
# client secret: 85546866091b2cab7133de1072b8b3f9ed003bc9


def onFrameConfigure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))


def callback(event):
    entry.delete(0, "end")
    return None


def get_weather(place):
    key = '8c7bce9575359167d87d3a46d74cefc6'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    # data = YahooWeather(APP_ID="pmaQw17c",
    #                     api_key="dj0yJmk9UkloMXE5RGUweU5NJnM9Y29uc3VtZXJzZWNyZXQmc3Y9MCZ4PTZm",
    #                     api_secret="85546866091b2cab7133de1072b8b3f9ed003bc9")

    if Tempvar.get() == 1:
        params = {'APPID': key, 'q': place, 'units': 'metric'}
    else:
        params = {'APPID': key, 'q': place, 'units': 'imperial'}

    if Comvar.get() == 1:

        response = requests.get(url, params=params)
        weather = response.json()
        label['text'] = "Open weather map:\n\n" + fix_response(weather)
        icon = weather['weather'][0]['icon']
        get_image(icon)
    else:

        response = requests.get(url, params=params)
        weather = response.json()
        print("TEST PRINT!!!!\t")
        print(weather)
        label['text'] = fix_response(weather)
        icon = weather['weather'][0]['icon']
        get_image(icon)


def get_weather_five_day(place):
    key = '8c7bce9575359167d87d3a46d74cefc6'
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    if Tempvar.get() == 1:
        params = {'APPID': key, 'q': place, 'units': 'metric'}
    else:
        params = {'APPID': key, 'q': place, 'units': 'imperial'}

    response = requests.get(url, params=params)
    weather = response.json()
    label['text'] = format_response_five_day(weather)


def get_image(icon):
    size = int(resultFrame.winfo_height()*0.25)
    image = ImageTk.PhotoImage(Image.open(
        './img/'+icon+'.png').resize((size, size)))
    weather_pic.delete("all")
    weather_pic.create_image(0, 0, anchor='nw', image=image)
    weather_pic.image = image


# def yahoo_response(place, data):
#     data.get_yahoo_weather_by_city(place, Unit.celsius)

#     try:
#         city = data.location.city
#         con = data.condition.text
#         temp = data.condition.temperature

#         if(Tempvar.get() == 0):
#             faren = (((temp * 9)/5) + 32)

#             yahoo_str = 'City: %s \nConditions: %s \nCurrent temp: %.2f %s \n' % (
#                 city, con, faren, unit_far)
#         else:
#             yahoo_str = 'City: %s \nConditions: %s \nCurrent temp: %.2f %s \n' % (
#                 city, con, temp, unit_cel)

#     except:
#         yahoo_str = 'Was not able to find yahoo weather'
#     return yahoo_str


def fix_response(weather):
    # print(weather)
    try:
        name = weather['name']
        descrip = weather['weather'][0]['description']
        curr_temp = weather['main']['temp']
        #min_temp = weather['main']['temp_min']
        if Tempvar.get() == 0:
            final_str = 'City: %s \nConditions: %s \nCurrent temp: %s %s ' % (
                name, descrip, curr_temp, unit_far)
        else:
            final_str = 'City: %s \nConditions: %s \nCurrent temp: %s %s ' % (
                name, descrip, curr_temp, unit_cel)
    except:
        final_str = 'Could not get the city entered'

    return final_str


def format_response_five_day(weather):
    try:
        city = weather['city']['name']
        country = weather['city']['country']

        day_one_date = (weather['list'][2]['dt_txt'])[:10]
        day_one_weather = weather['list'][2]['weather'][0]['description']
        day_one_temp_max = weather['list'][2]['main']['temp_max']
        day_one_temp_min = weather['list'][2]['main']['temp_min']
        icon = weather['weather'][2]['icon']
        get_image(icon)

        day_two_date = (weather['list'][10]['dt_txt'])[:10]
        day_two_weather = weather['list'][10]['weather'][0]['description']
        day_two_temp_max = weather['list'][10]['main']['temp_max']
        day_two_temp_min = weather['list'][10]['main']['temp_min']
        icon = weather['weather'][10]['icon']
        get_image(icon)

        day_three_date = (weather['list'][18]['dt_txt'])[:10]
        day_three_weather = weather['list'][18]['weather'][0]['description']
        day_three_temp_max = weather['list'][18]['main']['temp_max']
        day_three_temp_min = weather['list'][18]['main']['temp_min']
        icon = weather['weather'][18]['icon']
        get_image(icon)

        day_four_date = (weather['list'][26]['dt_txt'])[:10]
        day_four_weather = weather['list'][26]['weather'][0]['description']
        day_four_temp_max = weather['list'][26]['main']['temp_max']
        day_four_temp_min = weather['list'][26]['main']['temp_min']
        icon = weather['weather'][26]['icon']
        get_image(icon)

        day_five_date = (weather['list'][34]['dt_txt'])[:10]
        day_five_weather = weather['list'][34]['weather'][0]['description']
        day_five_temp_max = weather['list'][34]['main']['temp_max']
        day_five_temp_min = weather['list'][34]['main']['temp_min']
        icon = weather['weather'][34]['icon']
        get_image(icon)

        if Comvar.get() == 1:
            final_str = 'Please uncheck the [compare with yahoo] box as that is not a function for the 5-day forecast'

        elif Tempvar.get() == 1:
            final_str = 'City: %s, %s \n\nForecast: \nDate: %s \nSky: %s \nHigh: %s %s \nLow: %s %s \n\nDate: %s \nSky: %s \nHigh: %s %s \nLow: %s %s \n\nDate: %s \nSky: %s \nHigh: %s %s \nLow: %s %s \n\nDate: %s \nSky: %s \nHigh: %s %s \nLow: %s %s \n\nDate: %s \nSky: %s \nHigh: %s %s \nLow: %s %s' % (
                city, country, day_one_date, day_one_weather, day_one_temp_max, unit_cel, day_one_temp_min, unit_cel, day_two_date, day_two_weather, day_two_temp_max, unit_cel, day_two_temp_min, unit_cel, day_three_date, day_three_weather, day_three_temp_max, unit_cel, day_three_temp_min, unit_cel, day_four_date, day_four_weather, day_four_temp_max, unit_cel, day_four_temp_min, unit_cel, day_five_date, day_five_weather, day_five_temp_max, unit_cel, day_five_temp_min, unit_cel)
        else:
            final_str = 'City: %s, %s \n\nForecast: \nDate: %s \nSky: %s \nHigh: %s %s \nLow: %s %s \n\nDate: %s \nSky: %s \nHigh: %s %s \nLow: %s %s \n\nDate: %s \nSky: %s \nHigh: %s %s \nLow: %s %s \n\nDate: %s \nSky: %s \nHigh: %s %s \nLow: %s %s \n\nDate: %s \nSky: %s \nHigh: %s %s \nLow: %s %s' % (
                city, country, day_one_date, day_one_weather, day_one_temp_max, unit_far, day_one_temp_min, unit_far, day_two_date, day_two_weather, day_two_temp_max, unit_far, day_two_temp_min, unit_far, day_three_date, day_three_weather, day_three_temp_max, unit_far, day_three_temp_min, unit_far, day_four_date, day_four_weather, day_four_temp_max, unit_far, day_four_temp_min, unit_far, day_five_date, day_five_weather, day_five_temp_max, unit_far, day_five_temp_min, unit_far)

    except:
        final_str = 'There was a problem retrieving that information'

    return final_str


root = Tk()
Tempvar = IntVar()
Comvar = IntVar()
"""
vscroll = AutoScrollbar(root)
vscroll.grid(row=0,column=1,sticky=N+S)
hscroll = AutoScrollbar(root, orient=HORIZONTAL)
hscroll.grid(row=1, column=0, sticky=E+W)

canvas = Canvas(root,
	            yscrollcommand=vscroll.set,
                xscrollcommand=hscroll.set)
canvas.grid(row=0, column=0, sticky=N+S+E+W)

vscroll.config(command=canvas.yview)
hscroll.config(command=canvas.xview)

root.grid_rowconfigure(0,weight=1)
root.grid_columnconfigure(0,weight=1)

resultFrame = Frame(canvas)
resultFrame.rowconfigure(0,weight=1)
resultFrame.columnconfigure(0,weight=1)

canvas.create_window(0, 0, anchor=NW, window=resultFrame)

resultFrame.update_idletasks()

canvas.config(scrollregion=canvas.bbox("all"))

"""
canvas = Canvas(root, bg='#a1c7f4', height=HEIGHT,
                width=WIDTH, scrollregion=(0, 0, HEIGHT, 900))
resultFrame = Frame(canvas, bg='#3e4a59', bd=10)
scrolly = Scrollbar(root, command=canvas.yview)
scrolly.pack(side=LEFT, fill='y')
canvas.configure(yscrollcommand=scrolly.set)

scrolly.pack(side="right", fill="y")
canvas.pack(fill="both", expand=True)
canvas.create_window((6, 6), window=resultFrame)
resultFrame.bind("<Configure>", lambda event,
                 canvas=canvas: onFrameConfigure(canvas))

frame = Frame(root, bg='#3e4a59', bd=4)
entry = Entry(frame, font=('Arabic Transparent', 15), bg='#f4f6f7')
button = Button(frame, text="Today's weather", font=('Arabic Transparent', 10),
                bg='white', fg='#0c0c0c', command=lambda: get_weather(entry.get()))
fivebutton = Button(frame, text='5-day weather', font=('Arabic Transparent', 10),
                    bg='white', fg='#0c0c0c', command=lambda: get_weather_five_day(entry.get()))
cel = Checkbutton(root, bg='#a1c7f4', font=('Arabic Transparent', 10),
                  text='Celsius', variable=Tempvar, onvalue=1, offvalue=0)
# compare = Checkbutton(root, bg='#a1c7f4', font=('Arabic Transparent', 10),
#                       text='Compare with Yahoo weather', variable=Comvar, onvalue=1, offvalue=0)

"""imgPath = r"moon3.png"
background_image = PhotoImage(file=imgPath)
background = Label(canvas, image=background_image)
background.place(relheight = 1, relwidth = 1)"""

label = Label(resultFrame, font=('Arabic Transparent', 11),
              anchor='nw', justify='left', bd=4)
weather_pic = Canvas(label)

entry.insert(0, 'City or Zipcode, Country intials')
entry.place(relwidth=0.65, relheight=1)
entry.bind("<Button-1>", callback)

frame.place(relx=0.5, rely=0.05, relwidth=.85, relheight=.07, anchor='n')
button.place(relx=0.7, relwidth=0.3, relheight=0.5)
fivebutton.place(relx=0.7, rely=0.5, relwidth=0.3, relheight=0.5)
cel.place(relx=.08, rely=0.14)
# compare.place(relx=0.08, rely=0.18)
resultFrame.place(relx=0.5, rely=0.25, relwidth=0.85,
                  relheight=0.7, anchor='n')
label.place(relwidth=1, relheight=1)
weather_pic.place(relx=0.75, rely=0, relwidth=1, relheight=0.5)

root.mainloop()
