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