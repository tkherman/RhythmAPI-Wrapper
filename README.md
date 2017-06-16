# RhythmAPI-Wrapper
This API wrapper allow you to use python to interact with the Gracenote Rhythm
API to create a playlist for a radio station. It allows you to create a radio
playlist for up to 25 titles based on track, artist, mood, era and genre.

### Usage
To create a station, you must first need to get a Gracenote Client ID.
Go to https://developer.gracenote.com to get one. Before creating a station, you
must use you Client ID to register a user. This can be done using the register
function in register.py:

```python
from register import register

sampleClientID = "1234567-8DF1BF67913711DA38B26DA852B26D1A"
userID = register(sampleClientID)
```

The userID should be saved as it is needed for creating a station and further
query. The next step is to import the Radio class and initilize the clientID and
userID

```python
from radio import Radio

yourRadio = Radio(sampleClientID, userID)
```

Now, you can create a radio, send feedbacks and receive a playlist containing
metadata of the music in json

```
Functions: 
    Radio.create(seeds)
        - seeds is a list(max 5) of tuples(sized 2)
        - first entry of tuples is can be artist, track, genre, era or mood
        - second entry is the corresponding value
        - all entries have to be string
        - return a json containing metadata of the playlist

    Radio.event(actions, radioID)
        - actions is a list of tuples(sized 2)
        - first entry of tuples can be a string of "track_played", "track_skipped", 
          "track_like", "track_dislike", "artist_like", or "artist_dislike"
        - second entry is the corresponding GNID
        - RadioID ID of radio which can be found in the json returned by radio.create(seeds)
        - return a json containing metadata of the updated playlist

    Radio.lookahead(radioID)
        - return the current playlist as json
    
    Radio.listfields(attribute)
        - attribute can be genre, mood or era
        - return a list of string of possible genre, mood or era
```
