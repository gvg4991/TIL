import os
import requests
import csv

url = 'https://openapi.naver.com/v1/search/movie.json'
headers = {
    'X-Naver-Client-Id': os.getenv('NAVER_ID'),
    'X-Naver-Client-Secret': os.getenv('NAVER_SECRET')
}

with open('movie_naver.csv','r',newline='', encoding='utf8') as f: 
    reader = csv.DictReader(f)
    for row in reader:
                
        image_url = row['image']
        image_file = requests.get(image_url)
        with open('./images/'+row['movieCd']+'.jpg','wb') as f:
            f.write(image_file.content)