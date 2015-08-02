import webapp2

class MainPage(webapp2.RequestHandler):
  def get(self):
    if self.request.path == '/diff':
      self.redirect('/s/diff.html')
      return
    self.redirect('/s/notepad.html')

app = webapp2.WSGIApplication([
  ('/.*', MainPage),
  ], debug=True)
