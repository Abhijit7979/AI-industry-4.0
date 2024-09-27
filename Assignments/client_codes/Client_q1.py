import requests
url="http://64.227.147.221:5000/api/messages"
data={
    "message":"Abhijit"
}
response=requests.post(url,json=data)
print(response.text)