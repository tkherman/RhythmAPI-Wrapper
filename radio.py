#!/bin/usr/env python2.7

import requests

class Radio(object):
    """ Allow user to create a radio station using the Gracenote API
    
    Functions: 
        radio.create(seeds)
            - seeds is a list(max 5) of tuples(sized 2)
            - first entry of tuples is can be artist, track, genre, era or mood
            - second entry is the corresponding value
            - all entries have to be string
            - return a json containing metadata of the playlist

        radio.event(actions, radioID)
            - actions is a list of tuples(sized 2)
            - first entry of tuples can be a string of "track_played", "track_skipped", 
              "track_like", "track_dislike", "artist_like", or "artist_dislike"
            - second entry is the corresponding GNID
            - radioID ID of radio which can be found in the json returned by radio.create(seeds)
            - return a json containing metadata of the updated playlist

        radio.lookahead(radioID)
            - return the current playlist as json
        
        radio.listfields(attribute)
            - attribute can be genre, mood or era
            - return a list of string of possible genre, mood or era
    
    """

    def __init__(self, client, userID):
        self.client = client
        self.clientID = client.split("-")[0]
        self.clientTag = client.split("-")[1]
        self.userID = userID
        self.baseURL = "https://c" + self.clientID + ".web.cddbp.net/webapi/json/1.0/radio/"

    def create(self, seeds):
        createURL = self.baseURL + "create?client=" + self.client + "&user=" + self.userID
        while len(seeds) > 0:
            seed = seeds.pop()
            if seed[0] == "artist":
                name = seed[1].strip().replace(' ', '+').lower()
                createURL += "&artist_name=" + name
            elif seed[0] == "track":
                name = seed[1].strip().replace(' ', '+').lower()
                createURL += "&track_title=" + name
            elif seed[0] == "genre":
                for genre in self.fieldsJSON("genre")["RESPONSE"][0]["GENRE"]:
                    if genre["VALUE"] == seed[1]:
                        createURL += "&genre=" + genre["ID"]
                        break
            elif seed[0] == "mood":
                for mood in self.fieldsJSON("mood")["RESPONSE"][0]["MOOD"]:
                    if mood["VALUE"] == seed[1]:
                        createURL += "&mood=" + mood["ID"]
                        break
            elif seed[0] == "era":
                for era in self.fieldsJSON("era")["RESPONSE"][0]["ERA"]:
                    if era["VALUE"] == seed[1]:
                        createURL += "&era=" + era["ID"]
                        break
        playlist = requests.get(createURL)
        return playlist.json()

    
    
    
    
    def event(self, actions, radioID):
        eventURL = self.baseURL + "event?client=" + self.client + "&user=" + self.userID + "&radio_id=" + radioID
        while len(actions) > 0:
            action = actions.pop()
            eventType = action[0] + "_" + action[1]
            eventURL += "&event=" + eventType

        playlist = requests.get(eventURL)
        return playlist.json()

    
    
    
    
    def lookahead(self, radioID):
        lookaheadURL = self.baseURL + "lookahead?client=" + self.client + "&user=" + self.userID + "&radio_id=" + radioID
        playlist = requests.get(lookaheadURL)
        return playlist.json()

                
    
    
    
    
    
    def fieldsJSON(self, attribute):
        fieldsURL = self.baseURL + "fieldvalues?client=" + self.client + "&user=" + self.userID + "&fieldname="
        if attribute == "genre":
            fieldsURL = fieldsURL + "RADIOGENRE"
            genreR = requests.get(fieldsURL)
            return genreR.json()

        elif attribute == "mood":
            fieldsURL = fieldsURL + "RADIOMOOD"
            moodR = requests.get(fieldsURL)
            return moodR.json()

        elif attribute == "era":
            fieldsURL = fieldsURL + "RADIOERA"
            eraR = requests.get(fieldsURL)
            return eraR.json()


    def listfields(self, attribute):
        returnList = []
        if attribute == "genre":
            for genre in self.fieldsJSON("genre")['RESPONSE'][0]['GENRE']:
                returnList.append(genre['VALUE'])

        elif attribute == "mood":
            for mood in self.fieldsJSON("mood")['RESPONSE'][0]['MOOD']:
                returnList.append(mood['VALUE'])
        
        elif attribute == "era":
            for era in self.fieldsJSON("era")['RESPONSE'][0]['ERA']:
                returnList.append(era['VALUE'])
        else:
            return ["Error", "Incorrect attribute names, please enter 'genre, mood or era'"]
        
        return returnList
