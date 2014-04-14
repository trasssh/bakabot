#!/usr/bin/python

import ch
import time
import feedparser

class TestBot(ch.RoomManager):

     def onInit(self):
         self.setNameColor("F9F")
         self.setFontColor("F33")
         self.setFontFace("1")
         self.setFontSize(10)
         self.enableBg()
         self.enableRecording()
         
     def check(self, room):
                 feed = feedparser.parse('http://bakaforum.info/bakanewposts.php?type=atom1.0')
                 xml = feed.entries[0] 
                 lastupdated = xml['updated']
                 time.sleep(3)
                 feed = feedparser.parse('http://bakaforum.info/bakanewposts.php?type=atom1.0')
                 xml = feed.entries[0] 
                 updated = xml['updated']
                 author = xml['author']
                 title = xml['title']
                 link = xml['id'] 
                 if(lastupdated==updated):
                   print "same"
                 else:
                   print "postando"
                   mesg = ' postou no tópico '.decode("utf8")
                   room.message(author+mesg+title+' '+link)
                   
     def onConnect(self, room):
              self.setInterval(3, self.check, room)
              
testbot = TestBot()
roomList = ["ugtforumanime"]
usePM = False          

testbot.easy_start(roomList, "teste300194", "fe300194")
