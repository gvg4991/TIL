import os
import requests
import csv

movie=[]

with open('movie_naver.csv','r',newline='', encoding='utf8') as f: 
    reader = csv.DictReader(f)
    for row in reader:

        url = 'https://openapi.naver.com/v1/search/movie.json'
        headers = {
            'X-Naver-Client-Id': os.getenv('NAVER_ID'),
            'X-Naver-Client-Secret': os.getenv('NAVER_SECRET')
        }
        res = requests.get(url,params={'query':row['movieNm']}, headers=headers)

        data={
            'movieCd':row['movieCd'],
            'image':res.json()['items'][0]['image']
            }
        movie.append(data)

        for result in movie:
            writer.writerow(result) 

            image_url = result['image']
            image_file = requests.get(image_url)
            with open(result['movieCd'].jpg,'wb') as f:
                f.write(image_file.content)