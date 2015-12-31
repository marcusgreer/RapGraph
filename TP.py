# Marcus Greer+ Section P + TP1.py
#colorcombos.com
# Imports:
import random
import math
import os
import csv
import eventBasedAnimation
import tkSimpleDialog

def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

#####################
#Rapper Data
#####################
class Rapper(object):
    def __init__(self, name, lyrics, twitterData = None):
        #This method takes in a rapper's name and lyrics, and from that
        #initializes a class of the rapper's attributes
        self.name = name
        self.twitterData = 0
        self.rawLyrics = lyrics
        self.lyrics = set(lyrics.split())
        self.color = rgbString(random.randint(50,255),random.randint(0,100),
                                random.randint(50,255))
        #for visual components:
        self.numUniqueWords = 0
        self.r = 15
        self.clicked = False
        

    def __eq__(self,other):
        # This method defines the equality parameters for the rapper class
        if type(other) == Rapper:
            return self.name == other.name
        else:
            return self.name == other

    def __repr__(self):
        #this method defines the repr parameters for the rapper class
        return self.name

    def draw(self,canvas,cx,cy,r):
        # This function takes in a location on the grid and a draws the circle
        # on the corresponding location.
        self.x = cx
        self.y = cy
        canvas.create_oval(cx-r,cy-r,cx+r,cy+r,outline='red',width = 3,
            fill = 'yellow')
        canvas.create_text(cx,cy+(r+7),text=self.name,font='Helvetica 12 bold')

    def uniqueLyrics(self,rapList):
        #This function checks through the list of rapper objects, and compares
        #the lyrics of the rapper being analyzed with every other rapper's
        #lyrics to find the individual words used.
        self.unique = self.lyrics
        for rapperObject in rapList:
            if self == rapperObject:
                continue
            else:
                self.unique = self.unique - rapperObject.lyrics
            return self.unique

    def mostInCommon(self,rapList):
        #this method, given a list of rapper objects returns the artist with which
        # the rapper has the most lyrics in common.
        mostCommonWords = set()
        save = None
        for rapperObject in rapList:
            commonWords = self.lyrics-(self.lyrics - rapperObject.lyrics)
            if self == rapperObject:
                continue
            elif len(commonWords) > len(mostCommonWords):
                save = rapperObject
                mostCommonWords = commonWords
        return save

    def onClick(self,x,y,phase):
        if ((self.x-x)**2+(self.y-y)**2)**0.5 < self.r:
            return True


#########
#Display
#########

class rapGraph(eventBasedAnimation.Animation):
    #this is the general class that runs the whole Rap Graph Program.
    def onInit(self):
        #This method determines the values that initializes the rapGraph program
        from Tkinter import Tk, Frame, Canvas
        from PIL import ImageTk
        self.phase = 'Home'
        self.Ymargin = self.height/7
        self.Xmargin = self.width/10
        self.buttonWidth = self.width/4
        self.buttonHeight = self.height/8-10
        self.rappers = self.rapperObjects()
        self.applyTwitterData()
        self.rapImage = ImageTk.PhotoImage(file="cloud_large.png")
        self.squareSide = 50
        self.tagClick = []
        self.instructionText = self.returnInstructions()
        for rapper in self.rappers:
            rapper.numUniqueWords = len(rapper.uniqueLyrics(self.rappers))
        print self.rappers[0].rawLyrics

    def applyTwitterData(self):
        #This method applies twitter data to each of the rappers in an already
        #created list of rappers.
        filename = 'Popularity.txt'
        with open(filename,'rt') as infile:
            for row in csv.DictReader(infile):
                for rapper in self.rappers:
                    if row['Rapper'] == rapper:
                        rapper.twitterData = eval(row['Twitter Data'])

    def rapperObjects(self):
    #this function creates and returns a list of rapper Objects
        filename = 'RapLyrics.txt'
        with open(filename,'rt') as infile:
            rappers = []
            for row in csv.DictReader(infile):
                rappers.append(Rapper(row['Rapper'],row['Lyrics'],))
        return rappers

    def addNewArtist(self):
        #this method creates a new rapper object on the input of a user.
        from twitterData import getTwitterData
        from scraper import getMetroLyrics
        artist = tkSimpleDialog.askstring('Add New Artist',
                                        'Who do you want to compare?')
        if artist != None:
            getTwitterData(artist)
            getMetroLyrics(artist)
            self.rappers = self.rapperObjects()
            #rappers = rapperObjects()
            self.applyTwitterData()

    def onDraw(self,canvas):
        #this function controls the flow for drawing each of the phase screens.
        if self.phase == 'Home':
            self.drawHomeScreen(canvas)
        elif self.phase == 'Literal Diversity':
            self.drawLiteralDiversityScreen(canvas)
        elif self.phase == 'Influence':
            self.drawInfluenceScreen(canvas)
        elif self.phase == 'Tag Cloud':
            self.drawTagCloudScreen(canvas)
        elif self.phase == 'How To':
            self.drawHowToScreen(canvas)
        #this part of the method draws the constants that show up on all screens
        #regardless of phase (i.e. the home screen button and the add a rapper
        #button)
        canvas.create_rectangle(self.width-self.squareSide,0,
                                self.width,self.squareSide,
                                fill='red')
        canvas.create_text(self.width-self.squareSide/2,self.squareSide/2,
                            fill = 'white',
            text ='+', font ='Helvetica 50 bold')
        if self.phase != 'Home':
            canvas.create_rectangle(0,self.Ymargin-30,self.Xmargin-30,0,
                fill='yellow')

    def onKey(self,event):
        # This function controls the flow for the key functions of each of the 
        # phase screens.
        if self.phase == 'Home':
            self.keyHomeScreen(event)
        elif self.phase == 'Literal Diversity':
            self.keyLiteralDiversityScreen(event)
        elif self.phase == 'Influence':
            self.keyInfluenceScreen(event)
        elif self.phase == 'Tag Cloud':
            self.keyTagCloudScreen(event)
        elif self.phase == 'How To':
            self.keyHowToScreen(event)

    def onMouse(self,event):
        # This function controls the flow for the mouse functions of each of the 
        # phase screens.
        if self.phase == 'Home':
            self.mouseHomeScreen(event)
        elif self.phase == 'Literal Diversity':
            self.mouseLiteralDiversityScreen(event)
        elif self.phase == 'Influence':
            self.mouseInfluenceScreen(event)
        elif self.phase == 'Tag Cloud':
            self.mouseTagCloudScreen(event)
        elif self.phase == 'How To':
            self.mouseHowToScreen(event)
        if self.width>event.x>self.width-self.squareSide and self.squareSide>event.y>0:
            self.addNewArtist()
        if self.Xmargin - 30 > event.x > 0 and self.Ymargin - 30 > event.x > 0:
            self.phase = 'Home'
    
    #######
    #Home
    #######
    def drawHomeScreen(self,canvas):
        #This function draws the home screen
        canvas.create_rectangle(0,0,self.width,self.height,fill='black')
        canvas.create_text(self.width/2,self.height/4,fill = 'yellow',
            text ='Rap Graph', font ='Helvetica 75 bold')
        #Literal Diversity Button
        canvas.create_rectangle(\
            self.width/2-self.buttonWidth/2, 7*self.height/8-self.buttonHeight/2,
            self.width/2+self.buttonWidth/2, 7*self.height/8+self.buttonHeight/2,
            fill='yellow')
        canvas.create_text(self.width/2,7*self.height/8,text='Literal Diversity',
            font='Helvetica 35 bold')
        #Influence Graph Button:
        canvas.create_rectangle(\
            self.width/2-self.buttonWidth/2, 6*self.height/8-self.buttonHeight/2,
            self.width/2+self.buttonWidth/2, 6*self.height/8+self.buttonHeight/2,
            fill='yellow')
        canvas.create_text(self.width/2,6*self.height/8,text='Influence Graph',
            font='Helvetica 35 bold')
        #Tag Cloud Button:
        canvas.create_rectangle(\
            self.width/2-self.buttonWidth/2, 5*self.height/8-self.buttonHeight/2,
            self.width/2+self.buttonWidth/2, 5*self.height/8+self.buttonHeight/2,
            fill='yellow')
        canvas.create_text(self.width/2,5*self.height/8,text='Tag Cloud',
            font='Helvetica 35 bold')
        #Instruction Screen
        canvas.create_rectangle(\
            self.width/2-self.buttonWidth/2, 4*self.height/8-self.buttonHeight/2,
            self.width/2+self.buttonWidth/2, 4*self.height/8+self.buttonHeight/2,
            fill='yellow')
        canvas.create_text(self.width/2,4*self.height/8,text='Instructions',
            font='Helvetica 35 bold')

    def keyHomeScreen(self,event): pass

    def mouseHomeScreen(self,event):
        # This mouse function allows users to move from the home screen to any
        # of the other screeens.
        if self.width/2-self.buttonWidth/2<event.x<self.width/2+self.buttonWidth/2\
        and 7*self.height/8-self.buttonHeight/2<event.y<7*self.height/8+self.buttonHeight/2:
            self.phase = 'Literal Diversity'
        elif self.width/2-self.buttonWidth/2<event.x<self.width/2+self.buttonWidth/2 \
        and 6*self.height/8-self.buttonHeight/2<event.y<6*self.height/8+self.buttonHeight/2:
            self.phase = 'Influence'
        elif self.width/2-self.buttonWidth/2<event.x<self.width/2+self.buttonWidth/2 \
        and 5*self.height/8-self.buttonHeight/2<event.y<5*self.height/8+self.buttonHeight/2:
            self.phase = 'Tag Cloud'
        elif self.width/2-self.buttonWidth/2<event.x<self.width/2+self.buttonWidth/2 \
        and 4*self.height/8-self.buttonHeight/2<event.y<4*self.height/8+self.buttonHeight/2:
            self.phase = 'How To'

    ##################
    #Literal Diversity
    ##################

    def rapLiteralDiversity(self,canvas,rapList):
        # This method draws the rappers on the literal diversity screen and the
        # Average literal diversity/ Average twitter popularity axes.
        # import random
        uniqueWordNums = []
        twitterPopularity = []
        for rapper in rapList:
            uniqueWordNums.append(len(rapper.uniqueLyrics(self.rappers)))
            twitterPopularity.append(rapper.twitterData)
        maxTwit = max(twitterPopularity)
        minTwit = min(twitterPopularity)
        meanTwit = sum(twitterPopularity)/len(uniqueWordNums)
        maxLD = max(uniqueWordNums)
        minLD = min(uniqueWordNums)
        meanLD = sum(uniqueWordNums)/len(uniqueWordNums)
        meanX = (self.width-2*self.Xmargin)*((meanLD)\
                -minLD)/float((maxLD-minLD))+self.Xmargin
        meanY = self.height-((self.height-2*self.Ymargin)*((meanTwit)\
                -minTwit)/float((maxTwit-minTwit)))-self.Ymargin
        canvas.create_line(meanX,0,
                        meanX,self.height, dash = (2,4))
        canvas.create_line(0,meanY,
                        self.width,meanY, dash = (2,4))
        canvas.create_text(self.width/3,meanY-5,
            text='Average Popularity ('+str(meanTwit)+')',font= 'Helvetica 10 italic')
        canvas.create_text(meanX,self.height/5,
            text='Average Unique Words ('+str(meanLD)+' Words)',font= 'Helvetica 10 italic')
        for rapper in rapList:
            cy=self.height-((self.height-2*self.Ymargin)*((rapper.twitterData)\
                -minTwit)/float((maxTwit-minTwit)))-self.Ymargin
            cx=(self.width-2*self.Xmargin)*((len(rapper.uniqueLyrics(self.rappers))\
                -minLD)/float((maxLD-minLD)))+self.Xmargin
            r = 5
            rapper.draw(canvas,cx,cy,r)
            if rapper.clicked:
                self.drawInfo(canvas,rapper)

    def drawLiteralDiversityScreen(self,canvas):
        # draws the literal diversity screen's constant static elements:
        canvas.create_rectangle(0,0,self.width,self.height,
                                fill=rgbString(101, 153, 255))
        canvas.create_text(self.width/2,self.height/4,fill = 'white',
        text ='Literal Diversity',font ='Helvetica 75 bold')
        canvas.create_line(0,self.height-self.Ymargin+30,
                        self.width,self.height-self.Ymargin+30)
        canvas.create_line(self.Xmargin-30,self.height,
                        self.Xmargin-30,0)
        # Draws the literal diversity screen's dynamic elements
        self.rapLiteralDiversity(canvas,self.rappers)

    def keyLiteralDiversityScreen(self,event):
        pass

    def mouseLiteralDiversityScreen(self,event):
        # If a rapper is clicked his or her data is show and if a click occurs
        # outside of a rapper, then the data is hidden.
        rapperWasClicked = False
        for rapper in self.rappers:
            if rapper.onClick(event.x,event.y,self.phase):
                rapperWasClicked = True
                rapper.clicked = True
        if rapperWasClicked == False:
            for rapper in self.rappers:
                rapper.clicked = False
       
    ##################
    #Influence
    ##################
    def rapInfluences(self,canvas,rapList):
        # Draws rappers in a circle
        # import math
        cx,cy = self.width/2, self.height/2
        r = self.height/2.5
        length = len(rapList)
        for i in range(length):
            trans = 2* (math.pi)*(i)/length
            cx1 = cx+r*(math.cos(trans))
            cy1 = cy-r*(math.sin(trans))
            radius = 15
            rapList[i].draw(canvas,cx1,cy1,radius)

    def drawInfluenceScreen(self, canvas):
        colors=['red','orange','yellow','green','blue','light blue','violet']
        canvas.create_rectangle(0,0,self.width,self.height,
                                fill = rgbString(122, 186, 122))
        canvas.create_text(self.width/2,self.height/4, fill = 'white',
        text ='Influence Graph',font ='Helvetica 75 bold')
        self.rapInfluences(canvas,self.rappers)
        #connects the rappers with the rapper with whom they have the most lyrics
        #in common.
        for rapper in self.rappers:
            mostCommon = rapper.mostInCommon(self.rappers)
            canvas.create_line(rapper.x,rapper.y,
                                mostCommon.x,mostCommon.y,
                                fill= mostCommon.color, width = 2)
            if rapper.clicked:
                self.drawInfo(canvas,rapper)

    def drawInfo(self,canvas,rapper):
        # draws a little blurb about the twitter data and the Unique words
        # of the selected artist.
        if rapper.x > self.width/2: directX  = 1
        else: directX = -1
        canvas.create_polygon(rapper.x+10*directX,rapper.y, 
                                rapper.x+20*directX, rapper.y-10,
                                rapper.x+20*directX, rapper.y-20,
                                rapper.x+170*directX, rapper.y-20,
                                rapper.x+170*directX, rapper.y+20,
                                rapper.x+20*directX, rapper.y+20,
                                rapper.x+20*directX, rapper.y+10,
                                rapper.x+10*directX, rapper.y, fill = 'red')
        canvas.create_text(rapper.x+90*directX, rapper.y-5,
                            text = 'Unique Words: '+ str(rapper.numUniqueWords),
                            font = 'Helvetica 12 bold',fill = 'white',)
        canvas.create_text(rapper.x+90*directX, rapper.y+5,
                            text = 'Twitter Index: '+ str(rapper.twitterData),
                            font = 'Helvetica 12 bold',fill = 'white',)

    def keyInfluenceScreen(self, event): pass

    def mouseInfluenceScreen(self,event):
        # If a rapper is clicked his or her data is show and if a click occurs
        # outside of a rapper, then the data is hidden.
        rapperWasClicked = False
        for rapper in self.rappers:
            if rapper.onClick(event.x,event.y,self.phase):
                rapperWasClicked = True
                rapper.clicked = True
        if rapperWasClicked == False:
            for rapper in self.rappers:
                rapper.clicked = False

    ##################
    #Tag Cloud
    ##################
    def createTagCloud(self,rapper):
        #creates a tag cloud for the given artist.
        #For some reason these imports only work when placed in the function
        #but they do not if they are placed at the top of the document
        from pytagcloud import create_tag_image, make_tags
        from pytagcloud.lang.counter import get_tag_counts
        teststr = rapper.rawLyrics
        tags = make_tags(get_tag_counts(teststr), maxsize=100)
        tags = [a for a in tags if a['size'] > 20]
        create_tag_image(tags, 'cloud_large.png', size=(800, 400), 
            background=(239,101,85,255), fontname='PT Sans Regular')
        #Best: Neutron, Yanone Kaffeesatz, Droid Sans, Coustard
        # Nobile, Old Standard TT, Cantarell, Reenie Beanie, Cuprum, Molengo, 
        # Neucha, Philosopher, Yanone Kaffeesatz, Cardo, Neuton, Inconsolata, 
        # Crimson Text, Josefin Sans, Droid Sans, Lobster, IM Fell DW Pica, 
        # Vollkorn, Tangerine, Coustard, PT Sans Regular


    def drawTagCloudScreen(self, canvas):
        # draws the screen for the tag cloud option
        canvas.create_rectangle(0,0,self.width,self.height,
                                fill=rgbString(239,101,85))
        if len(self.tagClick)<1: tagArtist = ''
        else: tagArtist = self.tagClick[-1]
        canvas.create_text(int(2*self.width/3),self.height/4,fill = 'white',
        text ='Tag Cloud: '+tagArtist,font ='Helvetica 50 bold')
        canvas.create_image(int(2*self.width/3),int(2*self.height/3), 
                            image= self.rapImage)
        i = 0
        dx = 80
        dy = 50
        r = 15
        numOfRappers = len(self.rappers)
        for yVal in xrange(10):
            for xVal in xrange(3):
                if i < numOfRappers:
                    self.rappers[i].draw(canvas,self.Xmargin+dx*xVal,
                                                self.Ymargin+dy*yVal,r)
                i+=1

    def keyTagCloudScreen(self,event): pass

    def mouseTagCloudScreen(self,event):
        # makes a tag cloud for the clicked artist.
        #For some reason these imports only work when placed in the function
        #but they do not if they are placed at the top of the document
        from Tkinter import Tk, Frame, Canvas
        from PIL import ImageTk
        for rapper in reversed(self.rappers):
            if rapper.onClick(event.x, event.y, self.phase):
                self.tagClick.append(rapper.name)
                self.createTagCloud(rapper)
                self.rapImage = ImageTk.PhotoImage(file="cloud_large.png")
    
    ##################
    #How To Screen
    ##################
    def returnInstructions(self):
        #gets inscructions from instructions.txt
        text = ''
        fname = 'Instructions.txt'
        with open(fname,'rt') as infile:
            for row in infile:
                text += row
        return text
    def drawHowToScreen(self,canvas):
        # Draws the how to screen
        canvas.create_rectangle(0,0,self.width,self.height,fill = 'black')
        canvas.create_text(self.width/2,self.height/2,text= self.instructionText,
                            fill = 'white')

    def keyHowToScreen(self, event): pass
    def mouseHowToScreen(self, event): pass
    
rapGraph(width = 1250, height = 700).run()
