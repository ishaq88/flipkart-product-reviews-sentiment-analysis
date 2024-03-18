from bs4 import BeautifulSoup
import requests
import re

def get_reviews(url):
    '''
    This is the scrapping function to get ratings and reviews from flipkart
    '''
    
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
    
        review_containers = soup.find_all('div', class_=['col _2wzgFH K0kLPL', 'col _2wzgFH K0kLPL _1QgsS5'])

        dataset = []
        
        
        #upon research, flipkart has two different pages style for product reviews thus different classes for reviews
        
        overall_rating = soup.find('div', class_=["_2d4LTz", "_3LWZlK _12yO4d"]).text
        dataset.append({'overall_rating' : overall_rating})
        
        for container in review_containers:
            # Check if the container has only second class
            if 'col' in container['class'] and '_2wzgFH' in container['class'] and 'K0kLPL' in container['class'] and '_1QgsS5' in container['class']:
                sub_row = container.find_all('div', class_='row')
                
                
                rating_regex = r'^\d+'
                
                review = sub_row[0].find('div').text.strip()
                review = review.replace('READ MORE' , '')
                
                
                rating = re.match(rating_regex, review).group()
                review = re.sub(rating_regex, '', review).strip()
                
                
                dataset.append({'rating' : rating, 'review': review})
                
            # Check if the container has only the first class
            elif 'col' in container['class'] and '_2wzgFH' in container['class'] and 'K0kLPL' in container['class']:
                sub_row = container.find_all('div', class_='row')
                
                rating = sub_row[0].find('div').text.strip()
                
                review = sub_row[1].find('div').text.strip()
                review = review.replace('READ MORE' , '')
                
                dataset.append({'rating': rating, 'review': review}) 


        return dataset

    except Exception as e:
        print(f"Error: {e}")
        return []


def extract_product_name(url):

    pattern = r'\/([a-zA-Z0-9-]+)\/product-reviews'
    match = re.search(pattern, url)
    
    if match:
        return match.group(1)
    else:
        return None

if __name__ == '__main__':
    # url = 'https://www.flipkart.com/xiaomi-14-jade-green-512-gb/product-reviews/itm617acb7cd715d?pid=MOBGYGCMYEJTGEPF&lid=LSTMOBGYGCMYEJTGEPFUFDBXT&marketplace=FLIPKART'
    # data = get_reviews(url)
    
    # print(data)


#target example url
#url = 'https://www.flipkart.com/xiaomi-14-jade-green-512-gb/product-reviews/itm617acb7cd715d?pid=MOBGYGCMYEJTGEPF&lid=LSTMOBGYGCMYEJTGEPFUFDBXT&marketplace=FLIPKART'
#url = 'https://www.flipkart.com/samsung-galaxy-f15-5g-jazzy-green-128-gb/product-reviews/itm1357d201bcb0a?pid=MOBGYBAVT967G37V&lid=LSTMOBGYBAVT967G37VWBN6IA&marketplace=FLIPKART'


#############################################


    'class="_2d4LTz"' #overall rating class gives out of 5 ratings

    #parent classes for reviews  
    'class="col _2wzgFH K0kLPL"' 
    'class="col _2wzgFH K0kLPL _1QgsS5"'



###############################################