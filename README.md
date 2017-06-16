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

The following is a sample JSON playlist:

```
{
        "RESPONSE":
        [
            {
                "STATUS" : "OK",
                "RADIO":
                [
                    {
                        "ID" : "55ab765309bef50222c40afa3d990018"
                    }
                ],
                "ALBUM":
                [
                    {
                        "ORD" : "1",
                        "GN_ID" : "703386050-8A796B4281280F60AF2C2B5EAE4B2292",
                        "TRACK_COUNT" : "15",
                        "ARTIST":
                        [
                            {
                                "VALUE" : "The Chainsmokers"
                            }
                        ],
                        "TITLE":
                        [
                            {
                                "VALUE" : "Memories...Do Not Open [Bonus Tracks]"
                            }
                        ],
                        "GENRE":
                        [
                            {
                                "NUM" : "61424",
                                "ID" : "25364",
                                "VALUE" : "Electronica Mainstream"
                            }
                        ],
                        "TRACK":
                        [
                            {
                                "TRACK_NUM" : "13",
                                "GN_ID" : "703386063-364483769E8AD65666CF0B6A1DEF15F5",
                                "ARTIST":
                                [
                                    {
                                        "VALUE" : "The Chainsmokers Feat. Halsey"
                                    }
                                ],
                                "TITLE":
                                [
                                    {
                                        "VALUE" : "Closer"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "ORD" : "2",
                        "GN_ID" : "520246786-0A4E4978F4E3F8FC1FF7FA3E22657A61",
                        "TRACK_COUNT" : "11",
                        "ARTIST":
                        [
                            {
                                "VALUE" : "Zedd"
                            }
                        ],
                        "TITLE":
                        [
                            {
                                "VALUE" : "True Colors"
                            }
                        ],
                        "GENRE":
                        [
                            {
                                "NUM" : "177012",
                                "ID" : "65034",
                                "VALUE" : "House"
                            }
                        ],
                        "TRACK":
                        [
                            {
                                "TRACK_NUM" : "6",
                                "GN_ID" : "520246792-1C6261161C550C56BBE5D363FB00F837",
                                "ARTIST":
                                [
                                    {
                                        "VALUE" : "Zedd"
                                    }
                                ],
                                "TITLE":
                                [
                                    {
                                        "VALUE" : "True Colors"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "ORD" : "3",
                        "GN_ID" : "685646477-374FAF0BFCAE49EE251A551554C611F9",
                        "TRACK_COUNT" : "1",
                        "ARTIST":
                        [
                            {
                                "VALUE" : "R3hab Feat. V\u00e9rit\u00e9"
                            }
                        ],
                        "TITLE":
                        [
                            {
                                "VALUE" : "Trouble"
                            }
                        ],
                        "GENRE":
                        [
                            {
                                "NUM" : "177012",
                                "ID" : "65034",
                                "VALUE" : "House"
                            }
                        ],
                        "TRACK":
                        [
                            {
                                "TRACK_NUM" : "1",
                                "GN_ID" : "685646478-930484655FC61D2203570F4F4DB13832",
                                "ARTIST":
                                [
                                    {
                                        "VALUE" : "R3hab Feat. V\u00e9rit\u00e9"
                                    }
                                ],
                                "TITLE":
                                [
                                    {
                                        "VALUE" : "Trouble"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "ORD" : "4",
                        "GN_ID" : "631337901-47F27B590D1F565C229876113E677049",
                        "TRACK_COUNT" : "6",
                        "ARTIST":
                        [
                            {
                                "VALUE" : "Krewella"
                            }
                        ],
                        "TITLE":
                        [
                            {
                                "VALUE" : "Ammunition [EP]"
                            }
                        ],
                        "GENRE":
                        [
                            {
                                "NUM" : "212236",
                                "ID" : "70814",
                                "VALUE" : "Dubstep"
                            }
                        ],
                        "TRACK":
                        [
                            {
                                "TRACK_NUM" : "2",
                                "GN_ID" : "631337903-D69C5A51EA5D7BEC502407C85E91BA8E",
                                "ARTIST":
                                [
                                    {
                                        "VALUE" : "Krewella"
                                    }
                                ],
                                "TITLE":
                                [
                                    {
                                        "VALUE" : "Broken Record"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "ORD" : "5",
                        "GN_ID" : "604968730-6943E599E199A485ABD21564A614E858",
                        "TRACK_COUNT" : "2",
                        "ARTIST":
                        [
                            {
                                "VALUE" : "Afrojack & Hardwell"
                            }
                        ],
                        "TITLE":
                        [
                            {
                                "VALUE" : "Hollywood [Single]"
                            }
                        ],
                        "GENRE":
                        [
                            {
                                "NUM" : "177012",
                                "ID" : "65034",
                                "VALUE" : "House"
                            }
                        ],
                        "TRACK":
                        [
                            {
                                "TRACK_NUM" : "1",
                                "GN_ID" : "604968731-8EAB99A0377193B8AD33EB56DA8EB920",
                                "ARTIST":
                                [
                                    {
                                        "VALUE" : "Afrojack & Hardwell"
                                    }
                                ],
                                "TITLE":
                                [
                                    {
                                        "VALUE" : "Hollywood (Extended Mix)"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ]
}


```
