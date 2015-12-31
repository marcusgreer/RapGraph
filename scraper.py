# Marcus Greer+ Section P + TP1.py
####################
#Python Data Scraper
####################
import requests
from bs4 import BeautifulSoup
import time
from django.utils.encoding import smart_str, smart_unicode


def getMetroURL(artist):
    #uses the format from MetroLyrics to turn the string of an artist's name
    #into a URL.
    artist = artist.replace(' ','-').lower()
    url = 'http://www.metrolyrics.com/'+artist+'-lyrics.html'
    return url

def cleanedLyrics(lyrics):
    #This function removes all confusing and unnecessary characters from lyrics.
    result = ''
    for x in lyrics:
        if x=='\n': x = ' '
        if x.isalpha() or x == ' ':
            result += x
    return result
        
def getMetroLyrics(artist):
    # This function takes in an artists name and from it gathers his or her
    # lyrics from MetroLyrics and writes it to a local text file.
    url = getMetroURL(artist)
    r = requests.get(url)
    soup = BeautifulSoup(r.content)
    lyricData = ''
    print 'Getting Lyric Data For '+artist+'....',
    for item in soup.find_all('table',{'class':'songs-table compact'}):
        for link in item('a'):
            try:
                if lyricData.count(' ') < 20000:
                    req = requests.get(link.get('href'))
                    lyricSoup = BeautifulSoup(req.content)
                    newlyrics = smart_str(lyricSoup.find_all('p',{'class':'verse'})[0].text)
                    lyricData += (' '+newlyrics)
                else: 
                    break
            except:
                print 'Problem Occurred. Quit NOW!'
                time.sleep(5)
                pass
    lyrics = cleanedLyrics(lyricData).lower()
    with open('RapLyrics.txt','a') as fileOut: fileOut.write(artist+','+lyrics+'\n')
    print 'Done!'



def createRapLyricDatabase():
    #creates a textfile of rappers and their lyrics.
    with open('RapLyrics.txt','wt') as fileOut: fileOut.write('Rapper,Lyrics\n')
    rapList2 = ['Kendrick Lamar','Kanye West','Wu-Tang Clan','DMX','Aesop Rock',
                'ASAP Rocky', 'Blackalicious','Drake', '2pac', 'Lil Wayne', 
                'Outkast', 'Wale','Nas','Dr Dre','Mos Def','Common','Jay Z',
                'Rakim','GZA','Tech N9ne']
    for rapper in rapList2:
        getMetroLyrics(rapper)
        time.sleep(2)
    print 'Done'
    return

#createRapLyricDatabase()