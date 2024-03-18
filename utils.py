# this contains utility functions for sentiment inference

import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax

# Load the model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("model")
tokenizer = AutoTokenizer.from_pretrained("model")


def sentiment_scores(text):
    '''
    predict sentiment score using roberta model on torch
    '''

    encoded_text = tokenizer(text, return_tensors='pt')
    output = model(**encoded_text)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)

    # #gpu code
    # encoded_text = tokenizer(text, return_tensors='pt').to(device)
    # with torch.no_grad():
    #     output = model(**encoded_text)
    # scores = output.logits[0].cpu().numpy()
    # scores = softmax(scores)
    scores_dict = {
        'neg' : scores[0],
        'neu' : scores[1],
        'pos' : scores[2]
    }
    return scores_dict


def overall_sentiment_score(res): #res is the result scores of sentiment on data
    '''
    takes dict of individual sentiment results to calculate overall sentiment score
    '''
    if len(res) == 0:
        return None
        
    else:
        sum_pos = 0
        sum_neg = 0

        # Iterate over the values in the dictionary
        for key, value in res.items():
            
            sum_pos += float(value['pos'])
            sum_neg += float(value['neg'])

        # Calculate overall sentiment score
        overall_sentiment = (sum_pos - sum_neg)/len(res)
    
    return overall_sentiment


def no_of_pos_neg_reviews(res):

    positive_reviews = 0
    negative_reviews = 0

    for value in res.values():

        pos_score = float(value['pos'])
        neg_score = float(value['neg'])
        
        #positive review
        if pos_score > neg_score:
            positive_reviews += 1
            
        #negative review
        elif neg_score > pos_score:
            negative_reviews += 1

    return (positive_reviews, negative_reviews)


if __name__ == '__main__':
    text = 'checking function for the dummy text'
    print(sentiment_scores(text))


    