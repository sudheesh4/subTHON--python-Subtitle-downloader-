
'''
API: http://thesubdb.com/api/

API Description: The API uses an unique hash, calculated from the video file to match a subtitle. This way,
we cannot only guarantee that the subtitle fits the intended video but improve the search speed while we keep the API
as simple as it can be.

Algorithm: 1) Check if the file given is video file or not using python magic. If video file continue otherwise display
              the error and exit the program.
           2) Compose hash by taking first and last 64 KB of video file, putting all together and generating
              md5 of the resulting data (128 KB).
           3) Send request to the API along with the hash of the video to search the english subtitle.
           4) a) If subtitle found, send request to API with video hash and the language code(en) and action=download.
              b) If subtitle not found, display "Subtitle not found error message to user" and exit the program.
'''

import os
import hashlib
import requests


URL = 'http://api.thesubdb.com/'
HEADERS = {'User-Agent': 'SubDB/1.0 (subTHON/1.3; https://github.com/sudheesh4)'}


class Subdown:
    def __init__(self, name):
        self.name = name


    def get_hash(self,name):
        readsize = 64 * 1024
        with open(name, 'rb') as f:
            size = os.path.getsize(name)
            data = f.read(readsize)
            f.seek(-readsize, os.SEEK_END)
            data += f.read(readsize)
        return hashlib.md5(data).hexdigest()

    def down_load(self):
        print(self.name)
        req = {'action': 'download', 'hash': self.get_hash(self.name), 'language': 'en'}
        return requests.get(URL, params=req, headers=HEADERS)



