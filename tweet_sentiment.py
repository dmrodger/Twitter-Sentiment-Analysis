import sys
import json
import string
import re

# function creating dictionary of sentiment scores
def sentimentScores():
    afinnfile = open(r"C:\Users\Dylan\Desktop\datasci_course_materials\assignment1\AFINN-111.txt")
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores

def scoreTweets(): 
    # add each tweet's data from output to a list; includes non-English and deleted tweets
    data = [] 
    with open(r"C:\Users\Dylan\Desktop\datasci_course_materials\assignment1\output.txt") as f:
        for line in f:
            data.append(json.loads(line)) 
    
    # create scores dictionary for quicker reference
    scores = sentimentScores()
    # create list of  tweets that contain text (i.e. not deleted tweets) and are in English
    tweet = []
    for i in range(0,len(data)):
        if "text" in data[i] and data[i]["lang"] == "en":
            tweet.append(data[i]["text"]) 
            
    # creates copy of original tweet list to modify
    tweetWords = list(tweet)
    # cleans tweets and calculates sentiment score for each using scores dictionary
    for i in range(0,len(tweetWords)):
        # converts tweets from unicode to string
        tweetWords[i] = tweetWords[i].encode("utf-8")
        # removes punctuation of each tweet and splits each tweet into a list of individual words
        tweetWords[i] = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweetWords[i]).split() 
        # initialize sentiment score to 0
        sentiment = 0
        # score each tweet for every word found in scores dictionary
        for words in tweetWords[i]:
            if words in scores:
                sentiment += scores[words] 
        print sentiment
    
        
'''
def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
'''