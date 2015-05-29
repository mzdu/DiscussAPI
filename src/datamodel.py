#Database models used for storing the data from CourseraDiscuss

from google.appengine.ext import db

class Message(db.Model):
    
#     Data Model of Message is:
#     {
#         "Course1":
#         {
#             'Lecture1':[
#                     {'time1': 'msg1'},
#                     {'time2': 'msg2'}
#                      ],
#             'Lecture2':[
#                     {'timea': 'msga'},
#                     {'timeb': 'msgb'}
#                     ]
#         }
#         "Course2":
#         {
#             'Lecture1':[
#                     {'time1': 'msg1'},
#                     {'time2': 'msg2'}
#                      ],
#             'Lecture2':[
#                     {'timea': 'msga'},
#                     {'timeb': 'msgb'}
#                     ]
#         }
#     }
    courseName = db.StringProperty()
    lectureName = db.StringProperty()
    url = db.StringProperty()
    messageBody = db.StringProperty()
    messageDateTime = db.DateTimeProperty()
