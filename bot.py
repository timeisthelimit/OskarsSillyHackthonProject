import json
import http.client
from PIL import Image, ImageDraw, ImageFont
import requests
from random_word import RandomWords

conn = http.client.HTTPSConnection("bing-image-search1.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "4f645e9e29mshbe70fd37d7ad79ep1bbf0djsna010a9f253e9",
    'x-rapidapi-host': "bing-image-search1.p.rapidapi.com"
    }

r = RandomWords()

a = r.get_random_word()
b = r.get_random_word()
c = r.get_random_word()

url = f"/images/search?q={a}%20{b}&mkt=en-CA"

print(url)

conn.request("GET", url, headers=headers)

res = conn.getresponse()
data = res.read()

json_object = json.loads(data.decode("utf-8"))

res_img = requests.get(json_object["value"][0]["contentUrl"])

file = open("memige", "wb")
file.write(res_img.content)
file.close()



meme_img = Image.open("memige")

draw = ImageDraw.Draw(meme_img)

font_impact = ImageFont.truetype("impact.ttf", 36)

draw.text((10, 10), "Remote work tip:", font=font_impact)

meme_img.show()