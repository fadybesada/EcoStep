import jinja2
import os
import webapp2
import calculations
import random

the_jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_environment.get_template('templates/mainpage.html')
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(template.render())

    def post(self):
        scary_facts = ["Average global sea level is expected to rise 7 – 23 inches before the end of this century", "More than a million species face potential extinction as a result of disappearing habitats, changing ecosystems, and acidifying oceans", \
        "The Arctic region may have its first completely ice-free summer by 2040", "99.84% of the land in the state of California is suffering from drought", \
        "From 1979 to 2003, excessive heat exposure contributed to more than 8,000 premature deaths in the United States", \
        "The concentration of carbon dioxide (CO2)​​​​​​​ in our atmosphere, as of 2018, is the highest it has been in 3 million years.", \
        "Eleven percent of the world’s population is currently vulnerable to climate change impacts such as droughts, floods, heat waves, extreme weather events and sea-level rise.", \
        "Indonesia is moving its capital city as its current capital is sinking.", "Average wildlife populations have dropped by 60 percent in just over 40 years.", \
        "Two-thirds of extreme weather events in the last 20 years were influenced by humans", "Every single minute, the equivalent of 30 football pitches of tropical forests are being lost." \
        "If major change does not very soon, the damages of climate change will be irreversible by 2030.", "We are using more of Earth's resources than it could possibly renew."]

        scary_facts_select = random.choice(scary_facts)

        template = the_jinja_environment.get_template('templates/mainpage.html')
        self.response.write(template.render(scary_facts_select))

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
