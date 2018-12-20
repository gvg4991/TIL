ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scrapying": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "classes": {
        "gm":  {
            "lecturer": "junwoo",
            "manager": "pro-gm",
            "class president": "엄윤주",
            "groups": {
                "1조": ["강대현", "권민재", "서민수", "이규진"],
                "2조": ["박재형", "서민호", "윤종원", "이지현"],
                "3조": ["김미진", "김영훈", "엄윤주", "여성우"],
                "4조": ["김교훈", "김유림", "송현우", "이현수", "진민재", "하창언"],
            }
        },
        "gj": {
            "lecturer": "change",
            "manager": "pro-gj"
        }
    }
}

"""
난이도* 1. 지역(location)은 몇개 있나요? : list length
출력예시)
4
"""
print(len(ssafy['location']))


"""
난이도** 2. python standard library에 'requests'가 있나요? : 접근 및 list in
출력예시)
false
"""
if 'requests' in ssafy['language']['python']['python standard library'] : # in: 안에 있는지 확인
    print('true')
else:
    print('false')

library = ssafy['language']['python']['python standard library']
print('requests' in library) #true / false로 출력


"""
난이도** 3. gm반의 반장의 이름을 출력하세요. : depth 있는 접근
출력예시)
엄윤주
"""
print(ssafy['classes']['gm']['class president'])


"""
난이도*** 4. ssafy에서 배우는 언어들을 출력하세요. : dictionary.keys() 반복
출력 예시)
python
web
"""
language = ssafy['language']
for key in language.keys(): # for key in ssafy['language'].keys()과 같음
    print(key) # python, web


"""
난이도*** 5 ssafy gj반의 강사와 매니저의 이름을 출력하세요. dictionary.values() 반복
출력 예시)
change
pro-gj
"""
for name in ssafy['classes']['gj'].values(): #dict_values(['change', 'pro-gj']) -> change ; pro-gj 따로
    print(name)

"""
난이도***** 6. framework들의 이름과 설명을 다음과 같이 출력하세요. : dictionary 반복 및 string interpolation
출력 예시)
flask는 micro이다.
django는 full-functioning이다.
"""
for fw_key, fw_value in ssafy['language']['python']['frameworks'].items():
    print(f'{fw_key}는 {fw_value}이다.')
#for item in ssafy['language']['python']['frameworks'].items():
#    print(f'{item[0]}는 {item[1]}이다.') -위에거와 같음



"""
난이도***** 7. 오늘 당번을 뽑기 위해 groups의 4조 중에 한명을 랜덤으로 뽑아주세요. : depth 있는 접근 + list 가지고 와서 random.
출력예시)
오늘의 당번은 하창언
"""
import random
a = ssafy['classes']['gm']['groups']['4조']
print(f'오늘의 당번은 {random.choice(a)} 입니다.')