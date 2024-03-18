from flask import Flask, request, render_template
from scrapper import get_reviews, extract_product_name
from utils import sentiment_scores, no_of_pos_neg_reviews, overall_sentiment_score

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home_page():
    
    return render_template('home.html')

@app.route('/output', methods=['POST']) 
def output():
    dataset = []
    reviews = []
    pos, neg, overall_score, overall_rating = 0, 0, 0, 0
    product = ''

    if request.method == 'POST':
        url = request.form.get('url')
        product = extract_product_name(url)
        
        dataset = get_reviews(url) 
        res = {}
        for i in range(1, len(dataset)):
            try:
                text = dataset[i]['review']
                result = sentiment_scores(text)
                res[f'score_review_{i}'] = result
                
            except Exception:
                continue
            
        pos, neg = no_of_pos_neg_reviews(res)
        overall_score = overall_sentiment_score(res=res)
        if len(dataset) > 1:
            overall_rating = dataset[0]['overall_rating']
            reviews = dataset[1:]

    return render_template('output.html', dataset=reviews, product=product, 
                           overall_rating=overall_rating, no_pos_revs=pos, 
                           no_neg_revs=neg, score=overall_score)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
