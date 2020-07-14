from apscheduler.schedulers.blocking import BlockingScheduler
import main, os, json
from instapy_cli import client

schedule = BlockingScheduler()
@schedule.scheduled_job('interval', seconds=3)
def two_minute_job():
	# quote = main.getQuote()
	# image = main.toImage(quote[0], quote[1])
	# print("started")

	username = "quotes.princebot"
	password = "QUOTE.bot"
	# with open("USERNAME_ig.json", "r") as f:
	# 	cookie = json.loads(f.read())
	# 	f.close()
	cookie = '{"uuid": "cbc0359c-7801-11ea-8513-a86bad6c7cdf", "device_id": "android-4eb22ad58b6111e9", "ad_id": "6636790d-369b-2ad4-22a1-f17d0f99cfc5", "session_id": "cbc0359d-7801-11ea-8513-a86bad6c7cdf", "cookie": {"__class__": "bytes", "__value__": "gAN9cQBYDgAAAC5pbnN0YWdyYW0uY29tcQF9cQJYAQAAAC9xA31xBChYCQAAAGNzcmZ0b2tlbnEF\nY2h0dHAuY29va2llamFyCkNvb2tpZQpxBimBcQd9cQgoWAcAAAB2ZXJzaW9ucQlLAFgEAAAAbmFt\nZXEKWAkAAABjc3JmdG9rZW5xC1gFAAAAdmFsdWVxDFggAAAAQVI4SnVzaFJqUEpaT2Q5N1NuMEx1\nUmxXaThMYWo2ZlNxDVgEAAAAcG9ydHEOTlgOAAAAcG9ydF9zcGVjaWZpZWRxD4lYBgAAAGRvbWFp\nbnEQWA4AAAAuaW5zdGFncmFtLmNvbXERWBAAAABkb21haW5fc3BlY2lmaWVkcRKIWBIAAABkb21h\naW5faW5pdGlhbF9kb3RxE4hYBAAAAHBhdGhxFGgDWA4AAABwYXRoX3NwZWNpZmllZHEViFgGAAAA\nc2VjdXJlcRaIWAcAAABleHBpcmVzcRdK4wFrYFgHAAAAZGlzY2FyZHEYiVgHAAAAY29tbWVudHEZ\nTlgLAAAAY29tbWVudF91cmxxGk5YBwAAAHJmYzIxMDlxG4lYBQAAAF9yZXN0cRx9cR11YlgDAAAA\ncnVycR5oBimBcR99cSAoaAlLAGgKWAMAAABydXJxIWgMWAMAAABQUk5xImgOTmgPiWgQWA4AAAAu\naW5zdGFncmFtLmNvbXEjaBKIaBOIaBRoA2gViGgWiGgXTmgYiGgZTmgaTmgbiWgcfXEkWAgAAABI\ndHRwT25seXElTnN1YlgDAAAAbWlkcSZoBimBcSd9cSgoaAlLAGgKaCZoDFgcAAAAWG9zZjRRQUJB\nQUZ0Sk1mQ2pQWXdyMExVR2IzU3EpaA5OaA+JaBBYDgAAAC5pbnN0YWdyYW0uY29tcSpoEohoE4ho\nFGgDaBWIaBaIaBdK4iJXcWgYiWgZTmgaTmgbiWgcfXErdWJYBwAAAGRzX3VzZXJxLGgGKYFxLX1x\nLihoCUsAaApoLGgMWBAAAABxdW90ZXMucHJpbmNlYm90cS9oDk5oD4loEFgOAAAALmluc3RhZ3Jh\nbS5jb21xMGgSiGgTiGgUaANoFYhoFohoF0rjxgFfaBiJaBlOaBpOaBuJaBx9cTFYCAAAAEh0dHBP\nbmx5cTJOc3ViWAUAAABzaGJpZHEzaAYpgXE0fXE1KGgJSwBoCmgzaAxYBQAAADExMzkycTZoDk5o\nD4loEFgOAAAALmluc3RhZ3JhbS5jb21xN2gSiGgTiGgUaANoFYhoFohoF0pjWpReaBiJaBlOaBpO\naBuJaBx9cThYCAAAAEh0dHBPbmx5cTlOc3ViWAUAAABzaGJ0c3E6aAYpgXE7fXE8KGgJSwBoCmg6\naAxYEgAAADE1ODYxNzU5NzEuNzIyMzA5OHE9aA5OaA+JaBBYDgAAAC5pbnN0YWdyYW0uY29tcT5o\nEohoE4hoFGgDaBWIaBaIaBdKY1qUXmgYiWgZTmgaTmgbiWgcfXE/WAgAAABIdHRwT25seXFATnN1\nYlgKAAAAZHNfdXNlcl9pZHFBaAYpgXFCfXFDKGgJSwBoCmhBaAxYCwAAADE0MzUxODM2Mjk2cURo\nDk5oD4loEFgOAAAALmluc3RhZ3JhbS5jb21xRWgSiGgTiGgUaANoFYhoFohoF0rjxgFfaBiJaBlO\naBpOaBuJaBx9cUZ1YlgGAAAAdXJsZ2VucUdoBimBcUh9cUkoaAlLAGgKaEdoDFg9AAAAIntcIjEx\nNy4yMTMuOTguOFwiOiA5ODI5fToxakxRcFA6Rks4c3pJNFBSZ29NeU1STVVkdEI2eDJ1eHFNInFK\naA5OaA+JaBBYDgAAAC5pbnN0YWdyYW0uY29tcUtoEohoE4hoFGgDaBWIaBaIaBdOaBiIaBlOaBpO\naBuJaBx9cUxYCAAAAEh0dHBPbmx5cU1Oc3ViWAkAAABzZXNzaW9uaWRxTmgGKYFxT31xUChoCUsA\naApoTmgMWCEAAAAxNDM1MTgzNjI5NiUzQXZod2NpY2ZhVkJhZ3c4JTNBMTZxUWgOTmgPiWgQWA4A\nAAAuaW5zdGFncmFtLmNvbXFSaBKIaBOIaBRoA2gViGgWiGgXSmNTbGBoGIloGU5oGk5oG4loHH1x\nU1gIAAAASHR0cE9ubHlxVE5zdWJ1c3Mu\n"}, "created_ts": 1586175971}'
	hashtags = '#love #instagram #like4like #followme #picoftheday #follow #instadaily #instagood #motivation #instacool #inspirational #dailyquotes #successquotes #quotes #quoteoftheday #instaquotes'
	caption = 'Hourly quotes. \nfollow for more \n\n@quotes.princebot \n\n' + hashtags

	with client(username, password, cookie=cookie) as cli:
		cli.upload("up.png", caption)
		# cli.client.logout()
	# os.system("rm " + image)

schedule.start()
