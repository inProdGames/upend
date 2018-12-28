# -*- coding: utf-8 -*-

from google.appengine.ext import db

class Game(db.Model):
	id = db.StringProperty()
	title = db.StringProperty()
	description = db.TextProperty()
	embedCode = db.TextProperty()
	releaseDate = db.StringProperty()
	version = db.StringProperty()
	status = db.StringProperty()
	credits = db.TextProperty()
	changelog = db.TextProperty()
	type = db.StringProperty()
	
	facebook_url = db.StringProperty()
	gplus_url = db.StringProperty()
	instagram_url = db.StringProperty()
	twitter_url = db.StringProperty()
	
	visible = db.BooleanProperty()
	feature_rank = db.IntegerProperty()
