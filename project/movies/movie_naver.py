import os
import requests
import csv

movie=[]

with open('movie.csv','r',newline='', encoding='utf8') as f: 
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
            'image':res.json()['items'][0]['image'],
            'link':res.json()['items'][0]['link'],
            'userRating':res.json()['items'][0]['userRating']
            }
        movie.append(data)

    with open('movie_naver.csv','w',newline='', encoding='utf8') as f:
        writer = csv.DictWriter(f,fieldnames=['movieCd','image','link','userRating'])
        writer.writeheader()
        for result in movie:
            writer.writerow(result) 