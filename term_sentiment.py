import sys
import json
import string
import re


# function creating dictionary of sentiment scores
def sentimentScores():
    #afinnfile = open(r"C:\Users\Dylan\Desktop\datasci_course_materials\assignment1\AFINN-111.txt")
    afinnfile = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores

def scoreTweets(): 
    # add each tweet's data from output to a list; includes non-English and deleted tweets
    data = [] 
    #with open(r"C:\Users\Dylan\Desktop\datasci_course_materials\assignment1\output.txt") as f:
    with open(sys.argv[2]) as f:
        for line in f:
            data.append(json.loads(line)) 
    
    # create scores dictionary for quicker reference
    scores = sentimentScores()
    # create list of  tweets that contain text (i.e. not deleted tweets)
    tweet = []
    for i in range(0,len(data)):
        if "text" in data[i] and data[i]["lang"] == "en":
            tweet.append(data[i]["text"]) 

    # creates copy of original tweet list to modify
    tweetWords = list(tweet)
    # creates empty list to store scores for each tweet
    tweetScores = []
    # initialize empty dictionary for words not in scores dictionary
    newWords = {}
    # cleans tweets and calculates sentiment score for each using scores dictionary
    for i in range(0,len(tweetWords)):
        # converts tweets from unicode to string
        tweetWords[i] = tweetWords[i].encode("utf-8")
        # removes punctuation of each tweet and splits each tweet into a list of individual words
        tweetWords[i] = str.lower(tweetWords[i])
        tweetWords[i] = re.compile("[^\w']|_").sub(" ",tweetWords[i]).split() 
        # initialize sentiment score to 0
        sentiment = 0
        # score each tweet for every word found in scores dictionary
        for words in tweetWords[i]:
            if words in scores:
                sentiment += scores[words]
            elif words not in scores:
                newWords[words] = 0
        # append a list of scores for each tweet
        tweetScores.append(sentiment)
        # for words not in the sentiment dictionary, assign them a sentiment value based on sentiments of the tweet(s) found in
        for words in tweetWords[i]:
            if words in newWords:
                newWords[words] += tweetScores[i]
    for i in range(0, len(newWords)):
        print newWords.keys()[i], newWords.values()[i]
        
        
scoreTweets()
        


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