import requests

url = "https://the-giving-lab-thegivinglab.p.rapidapi.com/charities/%7Bname%20or%20filter%7D"

headers = {
    'x-rapidapi-host': "the-giving-lab-thegivinglab.p.rapidapi.com",
    'x-rapidapi-key': "SIGN-UP-FOR-KEY"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)