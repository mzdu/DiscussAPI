#main.py
#Coursera Discuss API
#Author: Mingzhe Du

import webapp2
import logging
import json
import datamodel

from google.appengine.ext import db
from libmain import doRender

class MainPageHandler(webapp2.RequestHandler):
    
    def get(self):
        values = dict()
        values['testarea'] = "this is a test string"       
        values['css'] = ['/static/css/main.css']
        values['javascript'] = ['']
        
        currentUrl = self.request.url
        currentUrl = currentUrl.strip()
        
        urlList = currentUrl.split('/')
        
        courseName = ""
        lectureName = ""
        
        for i in range(len(urlList)):
            try:
                if urlList[i] == "learn" and urlList[i+2] == "lecture" and urlList[i+3] != None and urlList[i+4] != None:
                    courseName = urlList[i+1]
                    lectureName = urlList[i+3] + urlList[i+4]
                    break
                
            except IndexError:
                self.error(400)
                
        else:
            self.error(400)

        logging.error(urlList)
        logging.error(courseName + ":" + lectureName)
        
        messages = db.Query(datamodel.Message).filter('courseName =', courseName).filter('lectureName =', lectureName).order('messageTime').fetch(limit=None)
        
        // now could get messages list 05/30/2015
        logging.error(messages)
        
         
        self.response.write('ok')
        
    def post(self):
        
        passToken = self.request.get('passToken')
        
        if passToken != "MingzheDu":
            self.error(401)
            return
        
        courseName = self.request.get('courseName').strip().lower()
        lectureName = self.request.get('lectureName').strip()
        messageBody = self.request.get('messageBody').strip()
        
        # convert messageTime from "2342" to 2342
        messageTime = self.request.get('messageTime')
#         logging.error(courseName)
#         logging.error(lectureName)
        
        try:
            messageTime = int(messageTime)
        except ValueError:
            self.error(400)
         
        message = datamodel.Message(courseName = courseName,
                                    lectureName = lectureName,
                                    messageBody = messageBody,
                                    messageTime = messageTime,
                                    )
        messageKey = message.put()
        if messageKey:
            self.response.headers['Content-Type'] = 'application/json'
            self.response.out.write(json.dumps({"status": "saved" }))
        else:
            self.error(400)
        
class TestHandler(webapp2.RequestHandler):
    
    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps({'status':'success'}))


        
app = webapp2.WSGIApplication([
                                  ('/main', MainPageHandler),
                                  ('/test', TestHandler),
                                  ('/.*', MainPageHandler)
                                  ],debug = True)
    

