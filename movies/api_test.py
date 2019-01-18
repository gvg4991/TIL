import os
import requests

# #영진위
# url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
# res = requests.get(url,params={'key': os.getenv('KOBIS_KEY'),'targetDt':'20190113','weekGb':'0'})
# print(res.json())

#네이버
naver_url = 'https://openapi.naver.com/v1/search/movie.json'
headers = {
    'X-Naver-Client-Id': os.getenv('NAVER_ID'),
    'X-Naver-Client-Secret': os.getenv('NAVER_SECRET')
}
naver_res = requests.get(naver_url,params={'query':'말모이'}, headers=headers)
print(naver_res.json())

# data = {
#     'title':'말모이',
#     'director':'엄유나'
# }

# #csv 저장하기
# import csv
# with open('test.csv','w',newline='', encoding='utf8') as f: #옵션에 따라 파일이 없어도 새로 생성하고 열 수 있음
#     writer = csv.DictWriter(f,fieldnames=['title','director']) #data 넣은것을 기반으로 
#     writer.writeheader() #헤드를 작성해줌
#     writer.writerow(data) #한줄씩 작성, 위에 설정한 data에서 가지고 오기

# #image 저장하기
# image_url = 'https://ssl.pstatic.net/imgmovie/mdi/mit110/1676/167699_P40_175859.jpg'
# image_file = requests.get(image_url)
# with open('test.jpg','wb') as f:
#     f.write(image_file.content)

# #csv 읽어오기
# with open('test.csv','r',newline='', encoding='utf8') as f: 
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row['title'],row['director'])