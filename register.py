#!/usr/bin/env python2.7

import requests
import sys

def register(client):
    clientID = client.split("-")[0]
    clientTag = client.split("-")[1]

    registerURL = "https://c" + clientTag + ".web.cddbp.net/webapi/json/1.0/register?client=" + client
    
    register = requests.get(registerURL)
    if register.json()["RESPONSE"][0]["STATUS"] == "OK":
        return register.json()["RESPONSE"][0]["USER"][0]["VALUE"]
    else:
        return "ERROR: " + register.json()["MESSAGE"][0]["VALUE"]
