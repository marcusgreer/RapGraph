#Marcus Greer+ Section P + TP1.py
###################
#Twitter API
###################
#inspired by the code on the twitter API Tweepy's website, this code takes all
#texts that are related to 2pac and prints them.

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

ckey = 'bmz3jbgy6THJ5TD5I3xBxRaec'
csecret = 'OTxmfO2jNc6KqPJeiIcfIvnlmzQgjJS3oqLm6Nwuag9GnY6wID'
atoken = '61327408-6JWhryRxaGXfmTwXvKSnMH8MvnftMLcbqP70nI8QO'
asecret = 'CeBxRayK6tKLkjOtbZ5lhEX1j7eTMeJ9T552pd7v80SBz'

class listener(StreamListener):
    def on_data(self, data):
        try:
            tweet = data.split(',"text":"')[1].split('","source"')[0]
            retweetCount = data.split(',"retweet_count":')[1].split(',"favorite_count"')[0]
            favorite = data.split(',"favorite_count":')[1].split(',"entities"')[0]
            # print favorite
            # print count
            tweet = data.split(',"text":"')[1].split('","source"')[0]
            print tweet
            #the following code is not actually dead code, It's purpose is to 
            #save all tweets related to a certain topic in a text or csv file:

            # saveFile = open('Tupac.txt','a')
            # saveFile.write(tweet)
            # saveFile.write('\n')
            # saveFile.close()
            time.sleep(5)
            return True
        except BaseException, e:
            print 'failed on_data', str(e)
            time.sleep(5)

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
rapList2 = ['Kendrick Lamar','Kanye West','Wu-Tang Clan','DMX','Aesop Rock',
                'ASAP Rocky', 'Blackalicious','Drake', '2pac', 'Lil Wayne', 
                'Outkast', 'Wale','Nas','Dr Dre','Mos Def','Common','Jay Z',
                'Rakim','GZA','Tech N9ne']
# twitterStream.filter(track=rapList2)
################################################################################
#Temboo
################################################################################

from temboo.Library.Twitter.Search import Tweets
from temboo.core.session import TembooSession

def getTwitterData(artist):
    #Heavily inspired by the code on the temboo twitter api page
    print 'Getting Twitter Data For '+ artist + '...',
    # Create a session with your Temboo account details
    session = TembooSession("marcusgreer", "myFirstApp", "9d024f2abbdd4fc8980efcff1322200f")

    # Instantiate the Choreo
    tweetsChoreo = Tweets(session)

    # Get an InputSet object for the Choreo
    tweetsInputs = tweetsChoreo.new_input_set()

    # Set the Choreo inputs
    tweetsInputs.set_Count("200")
    tweetsInputs.set_AccessToken("61327408-6JWhryRxaGXfmTwXvKSnMH8MvnftMLcbqP70nI8QO")
    tweetsInputs.set_Query(artist)
    tweetsInputs.set_AccessTokenSecret("CeBxRayK6tKLkjOtbZ5lhEX1j7eTMeJ9T552pd7v80SBz")
    tweetsInputs.set_ConsumerSecret("OTxmfO2jNc6KqPJeiIcfIvnlmzQgjJS3oqLm6Nwuag9GnY6wID")
    tweetsInputs.set_ConsumerKey("bmz3jbgy6THJ5TD5I3xBxRaec")
    tweetsInputs.set_ResultType("popular")

    # Execute the Choreo
    tweetsResults = tweetsChoreo.execute_with_results(tweetsInputs)

    # Print the Choreo outputs
    summ = 0
    tweets = tweetsResults.get_Response()
    for status in tweets.split(',"retweet_count":')[1:]:
        summ += eval(status.split(',"favorite_count"')[0])
    with open('Popularity.txt','a') as fileOut: fileOut.write(artist+','+str(summ)+'\n')
    print 'Done!'

    # print("Response: " + tweetsResults.get_Response())
    # print("Limit: " + tweetsResults.get_Limit())
    # print("Remaining: " + tweetsResults.get_Remaining())
    # print("Reset: " + tweetsResults.get_Reset())


def createRapTweetDatabase():
    #creates a textfile of rappers and their lyrics.
    with open('Popularity.txt','wt') as fileOut: fileOut.write('Rapper,Twitter Data\n')
    rapList2 = ['Kendrick Lamar','Kanye West','Wu-Tang Clan','DMX','Aesop Rock',
                'ASAP Rocky', 'Blackalicious','Drake', '2pac', 'Lil Wayne', 
                'Outkast', 'Wale','Nas','Dr Dre','Mos Def','Common','Jay Z',
                'Rakim','GZA','Tech N9ne']
    for rapper in rapList2:
        getTwitterData(rapper)
        time.sleep(2)
    print 'Done'
    return

#createRapTweetDatabase()