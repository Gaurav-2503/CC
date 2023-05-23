import webapp2

class MainWebpage(webapp2.RequestHandler):
    def get(self):
        response_content = ""
        for _ in range(10):
            response_content += "Akhilesh Ingole<br>"
            response_content += "T190058582<br>"
            response_content += "IT<br>"
            response_content += "<br>"

        self.response.write(response_content)

app = webapp2.WSGIApplication([('/',MainWebpage)])