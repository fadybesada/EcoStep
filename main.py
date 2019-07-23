import jinja2
import os
import webapp2

the_jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_environment.get_template('templates/mainpage.html')
        the_variable_dict = {

        }
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render(the_variable_dict))

class FootprintInput(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_environment.get_template('templates/result.html')
        the_variable_dict = {

        }
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render(the_variable_dict))

class FootprintOutput(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_environment.get_template('templates/result.html')
        the_variable_dict = {

        }
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render(the_variable_dict))

class AboutUs(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_environment.get_template('templates/result.html')
        the_variable_dict = {

        }
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render(the_variable_dict))

app = webapp2.WSGIApplication([
    ('/', WelcomePage),
    ('/result', ResultPage),
    ('/signup', SignupPage),
], debug=True)
