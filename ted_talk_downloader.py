import requests
import json
from bs4 import BeautifulSoup

# url = "https://www.ted.com/talks/jia_jiang_what_i_learned_from_100_days_of_rejection"
url = "https://www.ted.com/talks/ken_robinson_says_schools_kill_creativity"
r = requests.get(url)
print("Download about to start . . .")
result = ''

soup = BeautifulSoup(r.content, features='lxml')
next_data_script = soup.find(id="__NEXT_DATA__")
data_json = next_data_script.string
player_data = json.loads(data_json)['props']['pageProps']['videoData']['playerData']
url_player_content = json.loads(player_data)['resources']['h264'][0]['file']

mp4_response = requests.get(url_player_content)

file_name = 'ted_talk_video.mp4'
with open(file_name, 'wb') as f:
    f.write(mp4_response.content)



