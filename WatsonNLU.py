import csv
import json
import watson_developer_cloud
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features

'''
This code has been adapted from IBM Watson's Github page (https://github.com/watson-developer-cloud/python-sdk)
and modified to be used with our application.
This program performs Sentiment Analysis on every review from the input
data file which is recorded. Once a file is completed, an overall review
is generated which is then used as an input to the Conversation service.
'''


def sentimentMining():
    score = 0
    totalCount = 0
    negativeCount = 0
    positiveCount = 0
    inputText = ''

    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2017-04-14',
        username='83fc8084-8ff7-414c-8da4-e695d58f41d4',
        password='me0TMIZmusLz')

    # the input file to be used for sentiment analysis
    inputFile = ''
    with open(inputFile,'r') as f:
        reader = csv.reader(f)
        cnt = 0
        for row in reader:
            # skipping the first row which is the heading
            if cnt == 0:
                cnt+=1
            else:
                if len(row) == 0:
                    pass
                    # if empty review
                else:
                    inputText = row[0]
                    cnt+=1
                    totalCount +=1
                    # sentiment analysis of every review
                    response = natural_language_understanding.analyze(
                        text = inputText,
                        features=[features.Sentiment(), features.Emotion()], language = 'en')
                    print(totalCount)

                    # counting the number of positive and negative review with the score
                    if response["sentiment"]["document"]["label"] =='positive':
                        positiveCount +=1
                        score += response["sentiment"]["document"]["score"]
                    elif response["sentiment"]["document"]["label"] =='negative':
                        negativeCount +=1
                        score += response["sentiment"]["document"]["score"]
    return positiveCount, negativeCount, score, totalCount

def main():
    posCount, negCount, score, totCount = sentimentMining()
    print('Positive Count', posCount)
    print('Negative Count', negCount)
    print('Final Score', score)
    print('Total Count', totCount)


if __name__=='__main__':
    main()