import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        n =  8 
        fibonacci_numbers = [0, 1]

        for _ in range(2, n):
            next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
            fibonacci_numbers.append(next_number)

        self.response.write('<br>'.join(str(num) for num in fibonacci_numbers))

app = webapp2.WSGIApplication([('/', MainPage)])
