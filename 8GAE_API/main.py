import webapp2
import urllib
import json
import os
from google.appengine.ext.webapp import template

class MainWebPage(webapp2.RequestHandler):
    def get(self):
        temp = {}
        # path = os.path.join(os.path.dirname(__file__), 'index.html')
        # self.response.out.write(template.render(path,temp))
        path = os.path.join(os.path.dirname(__file__), 'template/index.html')
        self.response.out.write(template.render(path,temp))

    
    def post(self):
        lat = self.request.get('lat')
        longi = self.request.get('longi')
        url = 'https://api.open-meteo.com/v1/forecast?latitude={}&longitude={}&current_weather=true'.format(lat,longi)
        data = urllib.urlopen(url).read()
        data = json.loads(data)

        if "error" in data:
            template_values={"data": data['reason']}
            path = os.path.join(os.path.dirname(__file__), 'error.html')
            self.response.out.write(template.render(path,template_values))

        else:
            temperature=data["current_weather"]["temperature"]
            windspeed=data["current_weather"]["windspeed"]
            template_values={"temperature":temperature,"windspeed":windspeed}
            path = os.path.join(os.path.dirname(__file__), 'result.html')
            self.response.write(template.render(path,template_values))

app = webapp2.WSGIApplication([('/',MainWebPage)])