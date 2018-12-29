# -*- coding: utf-8 -*-

import os

import webapp2

from google.appengine.api import images

from models import Game


def get_content_type(image_data, ext):
	image = images.Image(image_data=image_data)
	
	if image.format == images.GIF:
		return 'image/gif'
	elif image.format == images.JPEG:
		return 'image/jpeg'
	elif image.format == images.PNG:
		return 'image/png'
	
	return ''


class SingleImageHandler(webapp2.RequestHandler):
	def get(self, game_id, type, ext):
		game = Game.query(Game.id == game_id).get()
		
		if type == 'icon':
			# Check that the requested image exists for the game.
			if not game.icon:
				self.response.write('Icon not found for game ' + game_id + '.')
				self.error(404)
				return
			
			# Output the icon.
			self.response.headers['Content-Type'] = get_content_type(game.icon, ext)
			self.response.write(game.icon)
			
		elif type == 'thumbstrip':
			# Check that the requested image exists for the game.
			if not game.thumbstrip:
				self.response.write('Thumbnail strip not found for game ' + game_id + '.')
				self.error(404)
				return
			
			# Output the thumbnail strip.
			self.response.headers['Content-Type'] = get_content_type(game.thumbstrip, ext)
			self.response.write(game.thumbstrip)
			
		else:
			self.error(404)

class ListImageHandler(webapp2.RequestHandler):
	def get(self, game_id, type, num, ext):
		game = Game.query(Game.id == game_id).get()
		
		try:
			num = int(num)
		except:
			self.response.write('Invalid ' + type + ' number.')
			self.error(404)
			return
		
		if type == 'screenshot':
			# Check that the requested image exists for the game.
			if (not game.screenshots) or (len(game.screenshots) <= num):
				self.response.write('Screenshot ' + `num` + ' not found for game ' + game_id + '.')
				self.error(404)
				return
			
			# Output the screenshot.
			self.response.headers['Content-Type'] = get_content_type(game.screenshots[num], ext)
			self.response.write(game.screenshots[num])
			
		elif type == 'thumbnail':
			# Check that the requested image exists for the game.
			if (not game.thumbnails) or int(num) >= (len(game.thumbnails)):
				self.response.write('Thumbnail ' + `num` + ' not found for game ' + game_id + '.')
				self.error(404)
				return
			
			# Output the thumbnail.
			self.response.headers['Content-Type'] = get_content_type(game.thumbnails[num], ext)
			self.response.write(game.thumbnails[num])
			
		else:
			self.error(404)

site = webapp2.WSGIApplication([
	('/game_assets/([a-z0-9]+)/(icon|thumbstrip)\.(gif|jpg|png)', SingleImageHandler),
	('/game_assets/([a-z0-9]+)/(screenshot|thumbnail)([0-9]+)\.(gif|jpg|png)', ListImageHandler)
])
