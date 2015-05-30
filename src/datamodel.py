#Database models used for storing the data from CourseraDiscuss

from google.appengine.ext import db

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

class Message(db.Model):

    messageBody = db.TextProperty()
    messageTime = db.IntegerProperty()
    lectureName = db.StringProperty()
    courseName = db.StringProperty()
