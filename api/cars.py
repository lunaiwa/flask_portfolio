from flask import Blueprint, request, jsonify
import requests
from flask_restful import Api, Resource

# Creating a Flask blueprint and API routing
cars_api = Blueprint('cars_api', __name__ ,
                    url_prefix='/api/cars')

# API instance from flask_restful
api = Api(cars_api)

import requests

url = "https://car-data.p.rapidapi.com/cars"

querystring = {"limit":"10","page":"0"}

headers = {
	"X-RapidAPI-Key": "3ed9e61dfbmshf4204c64a95df10p1b411bjsn032842b8e1d4",
	"X-RapidAPI-Host": "car-data.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

import requests

url = "https://car-data.p.rapidapi.com/cars/types"

headers = {
	"X-RapidAPI-Key": "3ed9e61dfbmshf4204c64a95df10p1b411bjsn032842b8e1d4",
	"X-RapidAPI-Host": "car-data.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)

import requests

url = "https://car-data.p.rapidapi.com/cars/makes"

headers = {
	"X-RapidAPI-Key": "3ed9e61dfbmshf4204c64a95df10p1b411bjsn032842b8e1d4",
	"X-RapidAPI-Host": "car-data.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)

import requests

url = "https://car-data.p.rapidapi.com/cars/years"

headers = {
	"X-RapidAPI-Key": "3ed9e61dfbmshf4204c64a95df10p1b411bjsn032842b8e1d4",
	"X-RapidAPI-Host": "car-data.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)