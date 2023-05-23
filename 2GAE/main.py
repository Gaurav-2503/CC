import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        response_text = ""
        for _ in range(5):
            response_text+="Akhilesh Ingole<br>"
            response_text+="T190058582<br>"
            response_text+="IT<br>"
            response_text+="<br>"

        self.response.write(response_text)



app = webapp2.WSGIApplication([("/", MainPage)])
