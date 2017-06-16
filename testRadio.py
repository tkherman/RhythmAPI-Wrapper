#!/usr/bin/env python2.7

from radio import Radio
from register import register

client = "222845652-5A37A2193E592F6B2F6C6C7D7ED98425"


haha = Radio(client, register(client))

seeds = [("artist", "the chainsmokers")]

playlist = haha.create(seeds)

print playlist

radioID = playlist["RESPONSE"][0]["RADIO"][0]["ID"]

firstGNID = playlist["RESPONSE"][0]["ALBUM"][0]["GN_ID"]

action = [("track_like", firstGNID)]

playlist = haha.event(action, radioID)

print playlist

playlist = haha.lookahead(radioID)

print playlist
