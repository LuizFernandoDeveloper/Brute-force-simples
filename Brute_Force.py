import requests 
import json



loginUrl = "http://192.168.5.108:9080/login_endpoint.php"

arquivo = "wl.txt"
usuario = "admin"

wordList = open(arquivo, "r")

def request(user, password):
    body = {"user":user, "password":password }
    r = request.post(loginUrl, data = json.dumps(body))
    print(r)

request("aa","aa")
