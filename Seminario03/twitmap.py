#Grupo 21
#Sistemas Distribuidos
#Manuel Francisco
#Jose Manuel Vidal

import twitter
from flask import Flask, render_template
from flask.ext.googlemaps import GoogleMaps
from flask.ext.googlemaps import Map

app = Flask(__name__)
GoogleMaps(app)

@app.route("/")
def geolocalizar():
	return render_template('index.html')

@app.route("/<latitud>,<longitud>")
def mapview(latitud, longitud):
	CONSUMER_KEY       = 'Q1KbqKGsKNtc7dtzinZRPt7T0'
	CONSUMER_SECRET    = 'vs3LksLHHa3bfB8spz9mxWBs8HKRQa0rBeWtY11UIK1Ao9FXrU'
	OAUTH_TOKEN        = '3110468098-O5e4abCiUFbAkoOljaMc1v3s69GeEgDDQKhn1T8'
	OAUTH_TOKEN_SECRET = 'PZWoVSjxtw8h55SkBTBsw7FMmzG9Y6pUyXf17iiQggaEH'

	auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
	twitter_api = twitter.Twitter(auth=auth)
	datos = twitter_api.search.tweets(count=100, geocode="36.538027,-6.201887,10km", result_type='recent')

	puntos = {}
	lista  = []
	for twit in datos["statuses"]:
		if twit["coordinates"] is not None:
			puntos.update({twit["user"]["profile_image_url_https"] : [(twit["coordinates"]["coordinates"][1], twit["coordinates"]["coordinates"][0])]})
			lista += [{'imagen':twit["user"]["profile_image_url_https"], 'texto':twit['text']}]

	twitmap = Map(
		identifier="view-side",
		lat=latitud,
		lng=longitud,
		markers=puntos,
		style="width:100%;height:100%"
	)

	return render_template('twits.html', twitmap=twitmap, lista=lista)

if __name__ == "__main__":
	app.run(debug=True)
