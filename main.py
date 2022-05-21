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

def send_404_page(handler):
	templateVars = {'title':'Error 404'}
	
	games = Game.gql('').fetch(11)
	shuffle(games)
	
	template = JINJA_ENVIRONMENT.get_template('head.html')
	handler.response.write(template.render(templateVars))
	template = JINJA_ENVIRONMENT.get_template('404.html')
	handler.response.write(template.render({'game':games[0]}))
	template = JINJA_ENVIRONMENT.get_template('foot.html')
	handler.response.write(template.render({}))
	
	handler.response.set_status(404)


class HomePage(webapp2.RequestHandler):
	def get(self):
		templateVars = {
			'description':'We make video games that offer a completely new experiences or new perspectives on familiar ones, including TetrEscape, Workshop Scramble, and Legitimate Tower Defense.',
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
			'The Inverted Productions website and games do not collect or store any personal information unless stated otherwise.\n\n' +
			'The Inverted Productions website uses Google Analytics (see policies.google.com/privacy to inquire about their policies).  You can opt out of Google Analytics using Google\'s opt-out browser add-on (support.google.com/analytics/answer/181881).\n\n' +
			'The Flash version of Legitimate Tower Defense includes ads from The Game Center (see www.thegamescenter.com to inquire about their policies).\n\n' +
			'The Android version of Workshop Scramble will access your profile and device identifier if you enable achievements and leaderboards, however Inverted Productions does not store or otherwise use that information.\n\n' +
			'The web version of TetrEscape uses Google Analytics and includes ads from Google AdSense; the Android version of TetrEscape includes ads from Google AdMob (see policies.google.com/privacy to inquire about their policies).  You can opt out of Google Analytics using Google\'s opt-out browser add-on (support.google.com/analytics/answer/181881).')

class RobotsTxtPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write('User-agent: *\nDisallow:')

class AdsTxtPage(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write('google.com, pub-9563245442880944, DIRECT, f08c47fec0942fa0')

class NotFoundPage(webapp2.RequestHandler):
	def get(self):
		send_404_page(self)

site = webapp2.WSGIApplication([
	('/', HomePage),
	('/news', NewsPage),
	('/people', PeoplePage),
	('/productions(/.*)?', ProductionsRedirect),
	('/privacy', PrivacyPolicyPage),
	('/robots\.txt', RobotsTxtPage),
	('/ads\.txt', AdsTxtPage),
	('/app-ads\.txt', AdsTxtPage),
	('/.*', NotFoundPage)
])
