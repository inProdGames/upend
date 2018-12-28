# -*- coding: utf-8 -*-

from google.appengine.ext import ndb

class Game(ndb.Model):
	id = ndb.StringProperty()
	platforms = ndb.StringProperty(repeated=True)
	tech = ndb.StringProperty(repeated=True)
	title = ndb.StringProperty()
	abbr_title = ndb.StringProperty()
	description = ndb.TextProperty()
	embed_code = ndb.TextProperty()
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
