import requests
import urllib.parse

# -------- SEARCH API --------
query = "javascript tutorial"
search_url = f"https://dns-ruby.vercel.app/search?query={urllib.parse.quote(query)}"

search_response = requests.get(search_url)
print("SEARCH RESULT:")
print(search_response.json())


# -------- YOUTUBE TO MP3 --------
video_url = "https://www.youtube.com/watch?v=abc123"
mp3_url = f"https://dens-audio.vercel.app/api/ytmp3?url={urllib.parse.quote(video_url)}"

mp3_response = requests.get(mp3_url)
print("\nMP3 RESULT:")
print(mp3_response.json())
