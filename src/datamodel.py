#Database models used for storing the data from CourseraDiscuss

from google.appengine.ext import db

class Message(db.Model):
    
#     Data Model of Message is:
#     {
#         'url1',[
#                 {'time1': 'msg1'},
#                 {'time2': 'msg2'}
#                  ],
#         'url2',[
#                 {'timea': 'msga'},
#                 {'timeb': 'msgb'}
#                 ]
#     }

    url = db.ListProperty()
    messageBody = db.StringProperty()
    messageDateTime = db.DateTimeProperty()
