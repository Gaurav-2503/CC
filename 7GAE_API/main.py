import webapp2
import urllib
import json
import os
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler):
    def get(self):
        temp={}
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path,temp))

    def post(self):
        pincode=self.request.get('pincode')
        url="https://api.postalpincode.in/pincode/"+ pincode
        data=urllib.urlopen(url).read()
        data=json.loads(data)
        print(data)
        status=data[0]['Status']

        if status=="Success":
            name=data[0]['PostOffice'][0]['Name']
            region=data[0]['PostOffice'][0]['Region']
            temp={"name":name,"region":region}
            path = os.path.join(os.path.dirname(__file__), 'result.html')
            self.response.out.write(template.render(path,temp))
        if status=="Error":
            temp={"data":data[0]['Message']}
            path = os.path.join(os.path.dirname(__file__), 'error.html')
        self.response.out.write(template.render(path,temp))
app=webapp2.WSGIApplication([('/',MainPage)])
