import os
import requests
import csv

movie=[]

with open('boxoffice.csv','r',newline='', encoding='utf8') as f: 
    reader = csv.DictReader(f)
    for row in reader:
    
        url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json'
        res = requests.get(url,params={'key': os.getenv('KOBIS_KEY'),'movieCd':row['movieCd']})

        data = {
            'movieCd':row['movieCd'],
            'movieNm':res.json()['movieInfoResult']['movieInfo']['movieNm'],
            'movieNmEn':res.json()['movieInfoResult']['movieInfo']['movieNmEn'],
            'movieNmOg':res.json()['movieInfoResult']['movieInfo']['movieNmOg'],
            'openDt':res.json()['movieInfoResult']['movieInfo']['openDt'],
            'showTm':res.json()['movieInfoResult']['movieInfo']['showTm'],
            'genreNm':res.json()['movieInfoResult']['movieInfo']['genres'][0]['genreNm'],
            'peopleNm':res.json()['movieInfoResult']['movieInfo']['directors'][0]['peopleNm'],
            'watchGradeNm':res.json()['movieInfoResult']['movieInfo']['audits'][0]['watchGradeNm'],
            # 'actors1':res.json()['movieInfoResult']['movieInfo']['actors'][0]['peopleNm'],
            # 'actors2':res.json()['movieInfoResult']['movieInfo']['actors'][1]['peopleNm'],
            # 'actors3':res.json()['movieInfoResult']['movieInfo']['actors'][2]['peopleNm']
            }
        
        movie.append(data)

    with open('movie.csv','w',newline='', encoding='utf8') as f:
        writer = csv.DictWriter(f,fieldnames=['movieCd','movieNm','movieNmEn','movieNmOg','openDt','showTm','genreNm','peopleNm','watchGradeNm'])
        writer.writeheader()
        for result in movie:
            writer.writerow(result) 