import requests
city_name = input("Enter city name: ")
api_key = "4fc14dfef5401f140b3c3e78aad8e042"
base_url= f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={api_key}"


response = requests.get(base_url)
data = response.json()
print(data)


