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

class FootprintOutput(webapp2.RequestHandler):
    def post(self):
        electricity = self.request.get('electricity')
        electricityCO = calculations.electricityCalc(electricity)

        natural_gas = self.request.get('natural_gas')
        natural_gasCO = calculations.naturalGasCalc(natural_gas)

        heating_oil = self.request.get('heating_oil')
        heating_oilCO = calculations.heatingOilCalc(heating_oil)

        miles_driven = self.request.get('miles_driven')
        miles_drivenCO = calculations.milesDrivenCalc(miles_driven)

        miles_flown = self.request.get('miles_flown')
        miles_flownCO = calculations.milesFlownCalc(miles_flown)

        miles_train = self.request.get('miles_train')
        miles_trainCO = calculations.milesTrainCalc(miles_train)

        miles_bus = self.request.get('miles_bus')
        miles_busCO = calculations.milesBusCalc(miles_bus)

        hotel_nights = self.request.get('hotel_nights')
        hotel_nightsCO = calculations.hotelNightsCalc(hotel_nights)

        totalCO = calculations.FootprintTotal(electricity, natural_gas, heating_oil, miles_driven, miles_flown, miles_train, miles_bus, hotel_nights)

        rating = "Very Good"
        if totalCO > 35:
            rating = "Very Poor"
        elif totalCO < 40 and totalCO > 35:
            rating = "Poor"
        elif totalCO < 30 and totalCO > 20:
            rating = "Fair"
        elif totalCO < 20 and totalCO > 15:
            rating = "Good"



        template_vars = {
            "rating": rating,
            "electricityCO": electricityCO,
            "natural_gasCO": natural_gasCO,
            "heating_oilCO": heating_oilCO,
            "miles_drivenCO": miles_drivenCO,
            "miles_flownCO": miles_flownCO,
            "miles_trainCO": miles_trainCO,
            "miles_busCO": miles_busCO,
            "hotel_nightsCO": hotel_nightsCO,
            "totalCO": totalCO,
        }

        template = the_jinja_environment.get_template('templates/output.html')
        self.response.write(template.render(template_vars))


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
