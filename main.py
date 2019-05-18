# -*- coding: utf-8 -*-

import os

import jinja2
import webapp2

from random import shuffle

from models import Game

JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates/')),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)

class HomePage(webapp2.RequestHandler):
	def get(self):
		templateVars = {
			'description':'The homepage of Inverted Productions, featuring video games that offer a completely new gaming experiences or new perspectives on familiar games.',
			'styles': 'home'
		}
		
		template = JINJA_ENVIRONMENT.get_template('head.html')
		self.response.write(template.render(templateVars))
		template = JINJA_ENVIRONMENT.get_template('home.html')
		self.response.write(template.render({}))
		template = JINJA_ENVIRONMENT.get_template('foot.html')
		self.response.write(template.render({}))

class NewsPage(webapp2.RequestHandler):
	def get(self):
		templateVars = {
			'title': 'News',
			'description': 'The latest news at Inverted Productions',
			'styles': 'news'
		}
		
		template = JINJA_ENVIRONMENT.get_template('head.html')
		self.response.write(template.render(templateVars))
		template = JINJA_ENVIRONMENT.get_template('news.html')
		self.response.write(template.render({}))
		template = JINJA_ENVIRONMENT.get_template('foot.html')
		self.response.write(template.render({}))

class PeoplePage(webapp2.RequestHandler):
	def get(self):
		templateVars = {'title':'People','description':'The people who work on our inverted productions'}
		
		template = JINJA_ENVIRONMENT.get_template('head.html')
		self.response.write(template.render(templateVars))
		template = JINJA_ENVIRONMENT.get_template('people.html')
		self.response.write(template.render({}))
		template = JINJA_ENVIRONMENT.get_template('foot.html')
		self.response.write(template.render({}))

class ProductionsRedirect(webapp2.RequestHandler):
	def get(self, path):
		self.redirect('/games' + path);

class PrivacyPolicyPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write(
			'Privacy Policy\n\n' +
			'The Inverted Productions website and games do not collect or store any personal information until stated otherwise.\n\n' +
			'The Flash version of Legitimate Tower Defense includes ads from The Game Center (see www.thegamescenter.com to inquire about their policies).\n\n' +
			'The Android version of Workshop Scramble will access your profile and device identifier if you enable achievements and leaderboards, however Inverted Productions does not store or otherwise use that information.')

class NotFoundPage(webapp2.RequestHandler):
	def get(self):
		templateVars = {'title':'Error 404'}
		
		games = Game.gql('').fetch(8)
		shuffle(games)
		
		template = JINJA_ENVIRONMENT.get_template('head.html')
		self.response.write(template.render(templateVars))
		template = JINJA_ENVIRONMENT.get_template('404.html')
		self.response.write(template.render({'game':games[0]}))
		template = JINJA_ENVIRONMENT.get_template('foot.html')
		self.response.write(template.render({}))
		
		self.response.set_status(404)

site = webapp2.WSGIApplication([
	('/', HomePage),
	('/news', NewsPage),
	('/people', PeoplePage),
	('/productions(/.*)?', ProductionsRedirect),
	('/privacy', PrivacyPolicyPage),
	('/.*', NotFoundPage)
])
