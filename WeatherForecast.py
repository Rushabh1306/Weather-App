import tkinter as tk
from PIL import ImageTk, Image
import PIL
import requests

def display(info):
    try:
        temp = info['main']['temp']# in celsius
        desc = info['weather'][0]['description']
        pressure = info['main']['pressure']
        humid = info['main']['humidity']
        wind_speed = info['wind']['speed']

        country_code = info['sys']['country']
        identity = info['id']

        final = 'ID :'+str(identity)+'\n'+'Country Code :'+str(country_code)+'\n'+'Temperature :'+str(temp)+'°C'+'\n'+'Description :'+str(desc).upper()+'\n'+'Pressure :'+str(pressure)+'hPa'+'\n'+'Humidity :'+str(humid)+'%'+'\n'+'Wind Speed :'+str(wind_speed)+'m/sec'+'\n'
    except:
        final = 'No results'
    return final
def get_info(city):
        key = 'YOUR_API_KEY'
        url = 'http://api.openweathermap.org/data/2.5/weather?'
        prms = {'appid': key,'q': city,'units':'metric'}
        response = requests.get(url,params=prms)
        info = response.json()
        label2['text'] = display(info)


def on_click(event):
    entry.configure(state=NORMAL)
    entry.delete(0, END)
    entry.unbind('<Button-1>', on_click_id)

    
#DESIGN
root = tk.Tk()
root.geometry("600x400")
root.title('Ur-Weather')

img = ImageTk.PhotoImage(Image.open("sunny.png"))
panel = tk.Label(image = img)
panel.place(relwidth=1,relheight=1)



frame = tk.Frame(root,bg='#80c1ff',bd=4)
frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.2)

entry=tk.Entry(frame,font=50)
entry.insert(0, "Enter City Name")
entry.configure(state=DISABLED)
on_click_id = entry.bind('<Button-1>', on_click)
entry.place(relx=0.01,relwidth=0.98,relheight=0.3)


button = tk.Button(frame,text="Weather!",command = lambda:get_info(entry.get()))
button.place(relx=0.4,rely=0.4,relwidth=0.2,relheight=0.4)

frame2 = tk.Frame(root,bg='#80c1ff',bd=4)
frame2.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.6)

label2 = tk.Label(frame2,text='summary',font=('Courier',16),justify='left',bd=4)
label2.place(relwidth=1,relheight=1)

root.mainloop()
