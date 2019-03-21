# 1. Create account in https://openweathermap.org/api
# 2. Get API access key
# 3. Make a multi-threaded program to connect to API
# 3a. Locations to be monitored should be placed in configuration file
# 3b. configruation file should have refresh frequency (for free api, you should not make more than 60 per minute.. so make not more than 5 per minute..)
# 4. One thread to download 5 days/3 hour forecast
# 5. One thread to download 16 days/daily forecast
# 6. One thread to download weather maps
# 7. All data should be stored in database (mongodb) as seperate collections/table
# 8. One thread to open the latest weather map and display the map in window (should show last image as per last time stamp)
# 9. Forecast threads should print out alerts if there is rain/snow or freeezing temperatures (2 def farenheit) in any of forecast period
# 10, See if you use graph API to display forecast/previous 10 day data from database as a graph (prebuilt libraries are there to do this)

"""
***************************************************************************************************
																								
Please take note that the program is barely functional and has to be refactored. I spent only around
two hours on this. This is just to give you an idea of my approach towards the problem.

***************************************************************************************************
"""


#Importing the list of required dependecies(libraries)
import requests
import json
from threading import Thread
import pymongo as py

#API_KEY is the api key to access openweather api service
API_KEY = "bb37c42082d7dd124cc06fb540af2fc8"
api_base_url = "https://api.openweathermap.org/"
city_dict = {"Orlando":4167147, "Irvine": 535977}


#Function to connect to MondoDB database
def connectMongo():
	client = py.MongoClient("mongodb+srv://neeraj:weather@weathertrack-vczxo.mongodb.net/test?retryWrites=true")
	return client

#Function to store the daily forecast of a city in mongodb
def daily_forecast():
	url = "http://api.openweathermap.org/data/2.5/forecast/daily"
	response = requests.get(url, params = parameters)
	print(response.status_code)

#Function to display a list of cities
def display_cities():    
    print("The available list of cities to track hourly forecast are:")
    for k, v in city_dict.items():
		print k ,"-", v

#Function to send the api request to openweatherapi. Returns the response and the city id of selected city
def send_api_request():
	city_id = input("Enter the city ID for which you want to track hourly forecast:")
	url = "http://api.openweathermap.org/data/2.5/forecast"
	parameters = {"id":city_id,"APPID":API_KEY}
	response = requests.get(url, params = parameters)
	data = response.json()
	return city_id, data

#Function to display the output values obtained from the API request
def display_output_values(city_id, data):
	print("City name: " + list(city_dict.keys())[list(city_dict.values()).index(city_id)])
	
	description = data['list'][0]['weather'][0]['description']
	humidity = data['list'][0]['main']['humidity']
	pressure = data['list'][0]['main']['pressure']
	wind_speed = data['list'][0]['wind']['speed']
	
	descriptors = ["Description:", "Humidity:", "Pressure:", "Wind Speed(meters/sec):"]
	descriptor_vals = [description, humidity, pressure, wind_speed]
	
	zipped_vals = zip(descriptors, descriptor_vals)
	for k, v in zipped_vals:
		print k, v

#Function to get the hourly forecast of the selected city from the 5hours/3 days api endpoint
def hourly_forecast():
	display_cities()
	city_id, data = send_api_request()
	zipped_vals = display_output_values(city_id, data)
	insert_values_mongodb(zipped_vals)

#Function to insert the obtained forecast values into MongoDB
def insert_values_mongodb(zipped_vals):
	client = connectMongo()
	db = client["test"]
	collection = db["hourly_forecast"]
	collection.insert(zipped_vals)

#Function to download weather maps from the weather maps API endpoint
def download_weather_maps():
	url = "https://tile.openweathermap.org/map/clouds_new/.png?"
	paramters = {"APPID":API_KEY}
	response = requests.get(url, params = parameters)


if __name__ == "__main__":

	# t1 = Thread(target = daily_forecast, name = "t1")
	# t2 = Thread(target = hourly_forecast, name = "t2")
	# t3 = Thread(target = download_weather_maps, name = "t3")
	hourly_forecast()
	# t1.setDaemon(True)
	# t2.setDaemon(True)
	# t3.setDaemon(True)

	# t1.start()
	# t2.start()
	# t2.run()
	# t3.start()