import speech_recognition as sr
import os
import webbrowser
import time

# path = os.getenv('PATH')
# print("Path is: %s" % (path,))
# print("shutil_which gives location: %s" % (sr.shutil_which('flac')))
      
def say(text):
    os.system(f"say {text}")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
       r.pause_threshold = 0.6
       audio = r.listen(source)
       try:
          query = r.recognize_google(audio, language="en-in")
          print(f"User said: {query}")
          return query
       except Exception as e:
           return "Some error occured. Sorry from Iri"
       
if __name__ == '__main__':
    say("Hello I am Iri A.I.")
    while True:
        print('listening')
        query = takeCommand()
        sites = [["youtube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["google","https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir")
                webbrowser.open(site[1])

# while True:           
#     query = takeCommand().lower()
#     print(query)
#     if 'song please' in query or 'play some song' in query or 'could you play some song' in query:
#         say('Sir what song should i play...')
#         song = takeCommand()
#         webbrowser.open(f'https://open.spotify.com/search/{song}')
#         time.sleep(13)
#         say('Playing' + song)

#     elif 'play' in query or 'can you play' in query or 'please play' in query:
#         say("OK! here you go!!")
#         query = query.replace("play", "")
#         query = query.replace("could you play", "")
#         query = query.replace("please play", "")
#         webbrowser.open(f'https://open.spotify.com/search/{query}')
#         time.sleep(19)
#         say("Enjoy Sir!!")


# import spotipy
# from spotipy.oauth2 import SpotifyOAuth

# # Initialize Spotify client
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='90b857cbf7ea4a98aac9f62b9ed9b224',
#                                                client_secret='5f1f05e822ed427a898ebe463af59709',
#                                                redirect_uri='statso.io',
#                                                scope='user-library-read user-modify-playback-state user-read-playback-state'))

# # Example: Play a track by name
# def play_track(track_name):
#     results = sp.search(q=f'track:{track_name}', type='track', limit=1)
#     if results['tracks']['items']:
#         track_uri = results['tracks']['items'][0]['uri']
#         sp.start_playback(uris=[track_uri])

# # Example usage
# play_track('Shape of You')
