# 1.딕셔너리 만들기
lunch={
    '중국집':'1111', # ,필요
    '양식집':'2222',
    '한식집':'3333'
}
dinner = dict(중국집='1111',양식집='2222',한식집='3333')

# 2. 딕셔너리에 내용 추가하기
lunch['분식집']='4444'

# 3. 딕셔너리 내용 가져오기
lunch['중국집'] #키만 가지고오면 뒤에 벨류값이 나옴 -> '1111'

idol = {
    'bts':{ # 딕셔너리 복수 설정
        '지민':24,
        'RM':25
    }
}
idol['bts'] #{'지민':24,'RM':25}
idol['bts']['RM'] #{25}

# 딕셔너리 출력
print(lunch)
print(lunch['중국집'])
print(dinner)

# 4. 딕셔너리 반복문 활용
for key in lunch: #key말고 다른거 사용해도 되지만 명확하게 알기쉬우려고 key라고 지정
    print(key) #key값 나옴 (하나씩 돌려서 하나씩 나옴)
    print(lunch[key]) #value값 나옴

for key in lunch.keys(): #key만 가지고오는 명령어: .keys()
    print(key) #key만 가지고 오기

for value in lunch.values(): #value만 가지고오는 명령어: .values() !!!!!!!!!!!!!!!!!!!!!
    print(value) #value만 가지고 오기

for item in lunch.items(): #(key,value)로 가지고오는 명령어: .item()
    print(item) #(key,value)로 가지고 오기
    print(item[0],item[1])
    print(key,value) #print(item[0],item[1])와 같음

# 2개 = 자료형(list, tuple ...) 길이2
a,b,c=(1,2,3)
print(a)
print(b)

# 문제 1번
score = {
    '수학':80,
    '국어':90,
    '음악':100
}
total_score1 = 0
for subject_score in score.values():
    #total_score1=total_score1 + subject_score
    total_score1 += subject_score
avg_score1 = total_score1 / len(score)
print(avg_score1)

total_score2 = 0
total_score2=sum(score.values())
avg_score2 = total_score2 / len(score)
print(avg_score2)

# 문제 2번
score = {
    'a':{
        '수학':70,
        '국어':80,
        '음악':90
    },
    'b':{
        '수학':70,
        '국어':80,
        '음악':90
    }
}

total_scores1 = 0
total_scores1=sum(score['a'].values())+sum(score['b'].values())
len_scores1=len(score['a'])+len(score['b'])
avg_scores1 = total_scores1 / len_scores1
print(avg_scores1)

num=0
total_ea_scores = 0
for ea_scores in score.values():
    for subject_ea_scores in ea_scores.values():
        total_ea_scores += subject_ea_scores
        #len_ea_scores += len(ea_scores.values())
        num=num+1
avg_ea_scores = total_ea_scores/num
#avg_ea_scores = total_ea_scores/len_ea_scores
print(avg_ea_scores)
#print(total_ea_scores)


#    total_score1=total_score1 + subject_score
#avg_score1 = total_score1 / len(score)
#print(avg_score1)