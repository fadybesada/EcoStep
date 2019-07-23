import jinja2
import os
import webapp2
import calculations

the_jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_environment.get_template('templates/mainpage.html')

        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())

class FootprintInput(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_environment.get_template('templates/input.html')

        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())

    def post(self):
        electricity = self.request.get('electricity')
        electricityCalc = calculations.electricityCalculator(electricity)

        template = the_jinja_environment.get_template('templates/output.html')
        self.response.write(template.render())

class FootprintOutput(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_environment.get_template('templates/output.html')

        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())

class AboutUs(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_environment.get_template('templates/about.html')

        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/input', FootprintInput),
    ('/output', FootprintOutput),
    ('/about', AboutUs),
], debug=True)
