#main.py
#Coursera Discuss API
#Author: Mingzhe Du

from libmain import doRender

import webapp2
import logging


class MainPageHandler(webapp2.RequestHandler):
    
    
    
    def get(self):
        values = dict()
        values['testarea'] = "this is a test string"       
        values['css'] = ['/static/css/main.css']
        values['javascript'] = ['']
        
        doRender(self, 'index.html', values)
        
    def post(self):
        pass

class TestHandler(webapp2.RequestHandler):
    
    def get(self):
        self.response.out.write({'status':'success'})


        
app = webapp2.WSGIApplication([
                                          ('/main', MainPageHandler),
                                          ('/test', TestHandler),
                                          ('/.*', MainPageHandler)
                                          ],debug = True)
    

