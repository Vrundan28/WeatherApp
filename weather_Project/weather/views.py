from django.shortcuts import render
import requests,json
def index(request):
    base_url = 'http://api.openweathermap.org/data/2.5/weather?'

    api_key = "ac6c3795b73218ed3b3d80bdc96146c6"
    if request.method == 'POST':
        city_name = request.POST.get('city')
        complete_url = base_url+"appid="+api_key+"&q="+city_name
        response = requests.get(complete_url)
        x=response.json()

        if x["cod"] != "404":
            y=x["main"]
            current_temperature = y["temp"] 
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]  
            z = x["weather"]
            icon = z[0]["icon"]
            weather_description = z[0]["description"] 
            print(city_name)
            print(current_temperature)
            print(current_pressure)
            weather_data = {
                'city_name':city_name,
                'current_temperature':current_temperature,
                'current_pressure':current_pressure,
                'current_humidity':current_humidiy,
                'weather_description':weather_description,
                'icon':icon
            }
            
            return render(request, 'show.html' , {'weather_data':weather_data})
        else: 
            return render(request,'index.html',{'error': "City Not Found"})
    else:
        return render(request,'index.html')
    # cities = City.objects.all()
    # # city_weather = requests.get(url.format(city)).json()
    
    # if request.method == 'POST': # only true if form is submitted
    #     form = CityForm(request.POST) # add actual request data to form for processing
    #     form.save()
    
    # form = CityForm()
    # weather_data = []

    # for city in cities:

    #     city_weather = requests.get(url.format(city)).json() 

    #     weather = {
    #         'city' : city,
    #         'temperature' : city_weather['main']['temp'],
    #         'description' : city_weather['weather'][0]['description'],
    #         'icon' : city_weather['weather'][0]['icon']
    #     }

    #     weather_data.append(weather)

    