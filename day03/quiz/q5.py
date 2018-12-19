'''
문제 5.
표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다.
입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요.
# 입력 예시: 300000;20000;10000
'''

prices = input('물품 가격을 입력하세요: ')
# 아래에 코드를 작성해 주세요. 

#mylist=prices.split(";")

#mylist=[]
#mylist.append(int(prices))
#mylist.sort()

#buble=[]
#for s in mylist:
#    mylist.append(int(s))

#mylist.sort()
#print(mylist)

#--------------------------------------------------------------------------------------------------------------------------------------

#input : 10;2;3
# .split() 이용
prices = prices.split(';') #['10','2','3']사전 순으로 나옴

#비어있는 리스트 생성
int_price=[]

# 1.반복을 통한 item들 int() 이용
for i in prices: #i='10'
    int_price.append(int(i)) #i=10, i=2, i=3 -> int_price=[10,2,3]
# 2.map함수 쓰기
#int_price = list(map(int,prices)) #[int('10'),int('2'),int('3')] -> [10,2,3]

# .sort() 정렬
int_price.sort() #[2,3,10]
# .reverse() 뒤집기
int_price.reverse() #[10,3,2]
# 한줄로 만들기
#1) sorted_price=reversed(sorted(int_price))
#2) int_price.sort(reverse=True)

# 출력
for i in int_price:
    print(i)
    #10
    #3
    #2
