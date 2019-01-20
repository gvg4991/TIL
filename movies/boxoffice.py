import os
import requests
import csv

total_time=[20190113, 20190106, 20181230, 20181223, 20181216, 20181209, 20181202, 20181125, 20181118, 20181111]
datas=[]
movie=[]

for date_time in total_time:
#영진위
  url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
  res = requests.get(url,params={'key': os.getenv('KOBIS_KEY'),'targetDt':date_time,'weekGb':'0'})

  for i in range(10):
    data = {
      'movieCd':res.json()['boxOfficeResult']['weeklyBoxOfficeList'][i]['movieCd'],
      'movieNm':res.json()['boxOfficeResult']['weeklyBoxOfficeList'][i]['movieNm'],
      'audiAcc':res.json()['boxOfficeResult']['weeklyBoxOfficeList'][i]['audiAcc'],
      'showRange':res.json()['boxOfficeResult']['showRange']
    }
  
    if not data['movieCd'] in movie:
      movie.append(data['movieCd'])
      datas.append(data)

with open('boxoffice.csv','w',newline='', encoding='utf8') as f:
  writer = csv.DictWriter(f,fieldnames=['movieCd','movieNm','audiAcc','showRange'])
  writer.writeheader()
  for result in datas:
    writer.writerow(result) 