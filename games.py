# -*- coding: utf-8 -*-

import os

import jinja2
import webapp2

from models import Game

JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates/')),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)

class GamePage(webapp2.RequestHandler):
	def get(self, id):
		if id[-11:] == '/index.html':
			id = id[:-11]
		
		if id != id.lower():
			# If the ID has caps in it, convert it to lowercase.
			self.redirect('/games/' + id.lower())
			return
		
		game = Game.query(Game.id == id).get()
		
		if not game:
			# If an alternate ID was used, redirect to that page.
			game = Game.query(Game.alt_ids == id).get()
			self.redirect('/games/' + game.id)
			return
		
		template = JINJA_ENVIRONMENT.get_template('head.html')
		self.response.write(template.render({
			'title': game.title,
			'description': game.description,
			'styles': 'game'
		}))
		if game != None:
			template = JINJA_ENVIRONMENT.get_template('game.html')
			self.response.write(template.render({
				'game': game
			}))
		else:
			template = JINJA_ENVIRONMENT.get_template('404.html')
			self.response.write(template.render({}))
		template = JINJA_ENVIRONMENT.get_template('foot.html')
		self.response.write(template.render({}))

class GamesList(webapp2.RequestHandler):
	def get(self):
		templateVars = {
			'title':'Games',
			'description':'Games and other productions by Inverted Productions',
			'styles': 'productions'
		}
		
		template = JINJA_ENVIRONMENT.get_template('head.html')
		self.response.write(template.render(templateVars))
		template = JINJA_ENVIRONMENT.get_template('productions.html')
		self.response.write(template.render({}))
		template = JINJA_ENVIRONMENT.get_template('foot.html')
		self.response.write(template.render({}))

site = webapp2.WSGIApplication([
	('/games/(.+)', GamePage),
	('/games/?', GamesList)
])
