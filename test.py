import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

#Get the user name from terminal
username = sys.argv[1]
playlistid = sys.argv[2]
#username ID: pedrojpx

#Erase cache and prompt for user permission... Erase cache?
try:
    token = util.prompt_for_user_token(username)
except:
    os.remove(f".cache-{username}")
    token = util.prompt_for_user_token

#Create spotifyObject
spotifyObject = spotipy.Spotify(auth=token)

user = spotifyObject.current_user()

displayName = user['display_name']
followers = user['followers']['total']

#print(json.dumps(user, sort_keys=True, indent=4))
playlist = spotifyObject.playlist("4mKsMyOuYluG5XiUSpNClb")
print(json.dumps(playlist, sort_keys=True, indent=4))

while True:
    print()
    print(">>> Welcome to Spotipy " + displayName + "!")
    print(">>> You have " + str(followers) + " followers.")
    print()
    print()
    print("0 - Search for an artist")
    print("1 - Search for playlist")
    print("2 - exit")
    print()
    choice = input("Your choice: ")

    #search for artist
    if choice == "0":
        print()
        searchQuery = input("Ok, what's their name? ")
        print()

        searchResults = spotifyObject.search(searchQuery,1,0,"artist")
        spotifyObject.playlist
        print(json.dumps(searchResults, sort_keys=True, indent=4))

    
    #end
    if choice == "1":
        break
