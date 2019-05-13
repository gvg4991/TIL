# import os
# import requests
# import csv

# datas=[]
# movie=[]

# #영진위
# url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
# res = requests.get(url,params={'key': os.getenv('5c917109455707da2a0a1254b5e389f0'),'targetDt':20190512,'weekGb':'0'})

# for i in range(10):
#     data = {
#       'movieCd':res.json()['boxOfficeResult']['weeklyBoxOfficeList'][i]['movieCd'],
#       'movieNm':res.json()['boxOfficeResult']['weeklyBoxOfficeList'][i]['movieNm'],
#       'audiAcc':res.json()['boxOfficeResult']['weeklyBoxOfficeList'][i]['audiAcc'],
#       'showRange':res.json()['boxOfficeResult']['showRange']
#     }
  
# if not data['movieCd'] in movie:
#     movie.append(data['movieCd'])
#     datas.append(data)

# print(datas)


# import json
# json.stdin = open('datas.json')
# print('yo')

# import json

# with open('datas.json') as data_file:    
#     data = json.load(data_file)

# print(data)