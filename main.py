import requests, json, pymongo, random
from PIL import Image, ImageDraw, ImageFont
from textwrap import wrap
from instapy_cli import client

def toImage(quoteText, quoteAuthor):

	font = ImageFont.truetype('RougeScript.ttf', 70)
	im = Image.new("RGB", (1080, 1080), '#0d0f11') #resolution of 1080x1080
	draw = ImageDraw.Draw(im)
	quoteText = wrap(quoteText, 35)
	quoteAuthor = '-' + quoteAuthor

	#quoteText
	upper_half = quoteText[: len(quoteText)//2]	#upper half of the text
	y = len(upper_half)
	for line in upper_half:
	    draw.text( (540-(font.getsize(line)[0]/2), 540-81*y), line, fill="#eeeeee", font=font)
	    y -= 1

	lower_half = quoteText[len(quoteText)//2 :]	#lower half of the text
	y = 0
	for line in lower_half:
	    draw.text((540-(font.getsize(line)[0]/2), 540+81*y), line, fill="#eeeeee", font=font)
	    y += 1

	#quoteAuthor
	draw.text((540-(font.getsize(quoteAuthor)[0]/2)+100, 540+81*y), quoteAuthor, fill='#eeeeee', font=font)

	#tag
	font = ImageFont.truetype('RougeScript.ttf', 30)
	draw.text((900, 1040), "@quotes.princebot", fill='grey', font=font)

	im.save("quote_image.png", quality=95)	#saving the image

	return "quote_image.png"

def getQuote():

# 	url = '*8*****8*'
# database url to get the quotes (from mongo cloud storage)
	client = pymongo.MongoClient(url)

	db = client["quotes"]
	categories = ["success", "love", "humor", "motivational", "inspirational",
	 "truth", "life-lessons", "science", "happiness", "relationships"]

	collections = db[random.choice(categories)]

	data = collections.find_one({"is_posted" : False})
	_id = data.get("_id")
	collections.update_one({"_id" : _id}, {"$set" : {"is_posted" : True}})

	return data.get("quoteText"), data.get("quoteAuthor")
