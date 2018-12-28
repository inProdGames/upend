# -*- coding: utf-8 -*-

from google.appengine.ext import ndb

class Game(ndb.Model):
	id = ndb.StringProperty()
	type = ndb.StringProperty(repeated=True)
	title = ndb.StringProperty()
	description = ndb.TextProperty()
	embedCode = ndb.TextProperty()
	embed_code = ndb.TextProperty()
	releaseDate = ndb.StringProperty()
	release_date = ndb.StringProperty()
	version = ndb.StringProperty()
	status = ndb.StringProperty()
	credits = ndb.TextProperty()
	changelog = ndb.TextProperty()
	
	icon = ndb.BlobProperty()
	thumbnails = ndb.BlobProperty(repeated=True)
	screenshots = ndb.BlobProperty(repeated=True)
	
	facebook_url = ndb.StringProperty()
	gplus_url = ndb.StringProperty()
	instagram_url = ndb.StringProperty()
	twitter_url = ndb.StringProperty()
	
	visible = ndb.BooleanProperty()
	feature_rank = ndb.IntegerProperty()
