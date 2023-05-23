import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        response_text = ""
        for i in range(1,11):
            response_text+="5 X {} = {}".format(i,i*10)
            response_text+="<br>"

        self.response.write(response_text)



app = webapp2.WSGIApplication([("/", MainPage)])
