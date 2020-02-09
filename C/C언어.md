## C언어

[열형강의 C 언어 본색](https://freelec.co.kr/lecture/c-%EC%96%B8%EC%96%B4%EC%9D%98-%EB%B3%B8%EC%A7%88%EC%9D%84-%ED%8C%8C%ED%97%A4%EC%B9%98%EB%8B%A4/)

#### 프로그램 작성 방법

- 프로젝트 만들기: 파일 - 새로만들기 - 프로젝트 -win32콘솔응용어플리케이션 - 빈프로젝트
- 소스파일 만들기(.c): 프로젝트폴더 - 소스파일 우클릭 - 추가 - 새 항목 - 코드 - C++파일 - 이름.c쓰기
- 오브젝트파일 만들기(.obj): 빌드 - 컴파일
- 실행파일 만들기(.exe): 빌드 - 솔루션빌드 - 링크
- 실행: 디버그 - 디버그하지않고 실행
- 디버깅: 소스코드에서 원하는 라인 우클릭 중단점 삽입 - 디버그 - 디버깅 시작





#### 기본 구조

```c
/* 
파일명: Hello.c
내용: Hello World 테스트
*/

#include<shdio.h>

int main(void)
{
    int age;
    printf("What is your age?");
    scanf("%d", &age);
    printf("Are you %d years old? \n",age)
        
    return 0;
}
```



```c
/* 
파일명: Hello.c
내용: Hello World 테스트
*/
/* 여러 줄 주석은? 이렇게! */
// 한 줄 주석은? 이렇게!

#include<shdio.h>
//전처리기와 헤더파일
/* 
#: 전처리기, 먼저 처리하는 기호(컴파일 수행하기 전에 처리)
include: 포함하다, 전처리를 지시
stdio: standard input output (표준 입출력)
.h: header file, 확장자.h를 가지는 헤더 파일
	- stdio.h: 헤더 파일안에 표준 입출력 함수들이 있음
*/
// '전처리기가 포함한다 표준입출력을 가진 헤더 파일을'로 해석
// 표준 라이브러리 함수와 헤더파일은 프로그래밍을 편하게 함

int main(void)
{
    int age;
    printf("What is your age?");
    scanf("%d", &age);
    printf("Are you %d years old? \n",age)
        
    return 0;
}
// main() 함수
/* 
운영체제에 의해 맨 처음 호출되고 맨 나중에 종료되는 함수
	- 운영체제: 프로그램과 기계 간 연결해주는 인터페이스
int: 출력 형태 ex) 커피
main: 함수 이름 ex) 자판기
(void): 입력 형태, void는 빈공간 ex) 동전
{ .. }: 함수의 기능
printf: 모니터에 출력
scanf: 데이터 입력
세미콜론(;): 문장의 끝을 의미하는 마침표 역할
return: 반환(출력)과 종료의 의미, 출력 형태가 있는 경우 return문을 꼭 써줌
*/
// 출력형태 함수이름(입력형태) {함수내용; return;}
// 진행 순서: 입력 -> 함수 이름 -> 함수의 기능 -> 출력
// main함수는 한 프로젝트 안에서 하나만 있어야 됨
```





#### stdio.h

```C
#include<stdio.h>
int main(void)
{
	//모니터에 출력하는 함수 printf()
    
    printf("Hello, World! \n"); 
    /*
    \n: 줄바꾸기, 개행
    \t: 탭
    \a: 실행 시 경고음 소리
    \': 작은 따옴표 출력
    \": 큰 따옴표 출력
    \\: \ 출력
    */
        
    printf("%d 더하기 %d는 %d입니다.",2,3,2+3);
    /* 
    %d: 10진수 정수
    %x: 16진수 정수
    %o: 8진수 정수
    %f, %lf: 10진수 실수
    %e, %le: e표기법
    %u: 10진수 양의 정수, %d의 두배값까지 표현 가능(4294967295)
    %c: 아스키코드 값의 문자로 표현 (0~127로 문자 표현)
    %%: % 표현
    */
    
    printf("Hello, %s %c","world","!");
    /* 
    %c: 문자 하나
    %s: 문자열
    */
    
    //-----------------------------------------------------------
    
    //키보드로부터 데이터 입력받는 함수 scanf()
    
    scanf("%d",&a);
    // scanf(입력 서식 문자, 입력을 저장하는 변수)
    /*
    %d: 데이터를 %d 형식으로 입력 받음
    &a: 입력받은 데이터를 변수 a에 저장 (a: 변수명)
    */ 
    
}
```





#### 변수 선언

```c
#include<stdio.h>
int main(void)
{
    int 정수★;
    short 짧은정수;
    long 긴정수;
    float 실수;
    double 중간실수★;
    long double 긴실수;
    char 문자;
    
    int a,b; // int a; int b;와 같음
    int c=0; // c값은 0, 변수에 저장된 데이터는 변경될 수 있음
    c = c+10 // c=10이 됨
}

// 순차적으로 선언되며 메모리에선 스택으로 쌓임
// &변수명: 변수의 시작 주소, 먼저 만든 변수의 주소값이 더 큼
```

- 변서 선언은 함수 맨 위쪽에서만 작성
- 변수 명은 의미있게 짓기
- 대,소문자를 구분함





#### 상수

- 리터럴 상수: 글자 그대로 의미가 있음

  - 아스키 코드(ASCII code)

  - 정수형 / 실수형 / 문자 / 문자열
  - 0x숫자: 16진수 / 0숫자: 8진수

- 심볼릭 상수: 상수를 기호화하여 변수처럼 이름이 있음

  - const / #define

  ```c
  #include<stdio.h>
  
  #define PI 3.14 //PI를 3.14로 상수 정의
  
  int main(void)
  {
      const int ten = 10; // ten을 10으로 상수 정의
      
      printf("%d", ten);
      printf("%d", PI);
      
      return 0;
  }
  ```





#### 연산자

- 복합 연산자 가능: +=, -=, *=, /=, %=

- 증감 연산자: ++a(선증가 후연산), a++(선연산 후증가), --a, a--

  ```c
  int num1=10, num2=10;
  
  printf("%d", ++num1); //11
  printf("%d", num1); //11
  
  printf("%d", num2++); //10
  printf("%d", num2); //11
  ```

- 관계 연산자: 0(False), 1(True)

- 논리 연산자: &&(and), ||(or), !(not)

- 조건 연산자: 조건식 ? 식1 : 식2 ; (조건식이 True면 식1, False면 식2 수행)

- 비트: 2진수 값 하나를 저장할 수 있는 최소 메모리 공간
  - 데이터를 비트 단위로 처리하는 연산자
  - 비트 연산자: &(and), |(or), ^(xor), ~(not, 1의 보수로 만든 후 1을 더함, 가장 앞은 부호 0(+),1(-)), <<n(n자리만큼 이동)





#### 자료형

- 정수형
  - 언더플로우 / 오버플로우: 범위를 벗어나면 순환 형식으로 표현됨 ex) char a=-129 -> a=127

| 정수형          | 메모리 크기     | 데이터 표현 범위                    |
| --------------- | --------------- | ----------------------------------- |
| char            | 1바이트(8비트)  | -128 ~ 127                          |
| short           | 2바이트(16비트) | -32768 ~ 32767                      |
| int             | 4바이트(32비트) | -2147483648 ~ 2147483647            |
| long            | 4바이트(32비트) | -2147483648 ~ 2147483647            |
| unsigned [type] | [type] 크기     | 양수 데이터로 데이터 범위 두배 표현 |

- 문자형

  - 문자는 작은따옴표(''), 문자열은 큰따옴표("")로 정의

  ```c
  char val1; //문자
  int val2; //숫자
  
  printf('%d',val1); //val1의 아스키코드 숫자값
  printf('%c',val2); //val2값의 아스키코드 문자
  ```

- 자료형 변환

  - 자동형 변환: 컴파일러가 자동으로 해줌

    - 산술 연산의 경우, 작은형에서 큰형으로 자동 변환 ex)정수+실수 -> 실수

    - char < int < long < float < double < long double

    - 대입 연산의 경우, 오른쪽에서 왼쪽으로 자동 형변환(데이터 변화 문제 발생)

      ```c
      char num1 = 130; //-126 (오버플로우)
      int num2 = 3.14; //3 (0.14 손실)
      double num3 = 3; //3.00000 (작은형에서 큰형일 경우 손실x)
      ```

  - 강제형 변환: 프로그래머가 강제로 해줌

    - 괄호 연산자 사용

      ```c
      int num1=5, num2=2;
      double result;
      //큰 형으로 바뀜
      result = num1/num2; //2.000000 (정수/정수)
      result = (double)num1/num2; //2.500000 (실수/정수)
      result = num1/(double)num2; //2.500000 (정수/실수)
      result = (double)num1/(double)num2; //2.500000 (실수/실수)
      ```

- typedef : 기본 자료형에 새로운 이름을 붙임

  ```c
  typedef int mytype;
  
  int main(void)
  {
      mytype num1=3000;
  }
  // mytype으로 int 정의
  ```





#### 반복문

- while문

```c
// wihle문
int main(void){
    int num = 0; //초기값
    while(num<3){ //조건값
        printf("반복내용: %d",num);
        num++; //증감값
    }
 return 0;
}
/*
반복내용: 0
반복내용: 1
반복내용: 2
*/

// while문 무한루프
int main(void){
    int num = 0;
    while(1){ //무한루프
        printf("반복내용: %d",num);
        num++;
        if(num>5)
            break;
    }
 return 0;
}

// 중첩 while문
int main(void){
    int num1=0, num2=0;
    while(num1<2){
        printf("큰 반복: %d",num);
        while(num2<2){
            printf("작은 반복: %d",num);
            num2++;
        }
        num1++;
        num2=0;
    }
 return 0;
}
/*
큰 반복: 0
작은 반복: 0
작은 반복: 1
큰 반복: 1
작은 반복: 0
작은 반복: 1
*/
```

- for문

```c
//for문
int main(void){
    int num;
    for(num=0;num<3;num++) //초기값,조건값,증감값
    {
        printf("반복내용: %d",num);
    }
return 0;
}
/*
반복내용: 0
반복내용: 1
반복내용: 2
*/

// for문 무한루프
int main(void){
    int num;
    for(num=0;num<3;num++) //초기값,조건값,증감값
    {
        printf("반복내용: %d",num);
    }
return 0;
}

// 중첩 for문

// for문 변형
int main(void){
    itn i=1, factorial=1;
    for(;i<=10;i++){ //초기값이 없는 경우
        factorial *= i
    }
	// 선언값이 초기값으로 됨
int main(void){
    itn i=1, factorial=1;
    for(i;;i++){ //조건값이 없는 경우
        factorial *= i
    }
	// 무한루프 -> ctrl+c로 나가기
}
```

- do~while문: 우선 실행하고 조건 반복

```c
num=0 //초기
do{
    num++ //증감
} while(num<3); //조건
```





#### 조건문

```c
#include <stdio.h>
int main(void){
    int num;
    printf("숫자 입력");
    scanf("%d",&num);
    
    // if문
    if(num>0)
        printf("양수");
    else if(num<0)
        printf("음수");
    else
        printf("0");
    
    
	// switch~case 문
    switch(num){
        case 1:
           	printf("1");
            break
        case 0:
            printf("0");
            break
        case -1:
            printf("-1");
            break
        default:
            printf("-1,0,1만 있습니다.")
    }
    
    return 0;
}
```





#### 함수

- 특정 작업을 수행하는 코드의 집합

- 표준 라이브러리 함수, 사용자 정의 라이브러리 함수

- '출력형태 함수이름(입력형태) {함수 기능}'의 형식

  ```c
  #include <stdio.h>
  int sum(int x, int y){ //x,y를 입력받아 sum함수를 수행하고 int형으로 출력
      int result;
      result = x + y;
      return result; //출력형태가 있으므로 return 필수
  }
  
  int main(void){ //입력값 없음, void작성 안해도 됨
      int answer = 0;
      answer = sum(3,4);
      printf("%d \n",answer);
      
      return 0; //출력형태가 있으므로 return 필수
  }
  
  void print(int x){ //출력값 없음
      int a = x;
      printf("%d",a);
      //return; 작성 안해도 됨
  }
  
  void output(void){ //입,출력값 없음
      printf("Hello World!");
  }
  ```

- 함수 적용 방법

  - 함수 정의(기능) - 함수 호출

  - 함수 선언 - 함수 호출 - 함수 정의(기능)

    ```c
    int sum(int x,int y); //위에서 함수 선언
    
    int main(void){
        int result = 0;
        result = sum(3,4);
    	printf("%d",result);
        return 0;
    }
    
    int sum(int x,int y){
        int answer = 0;
        answer = x+y;
        return answer;
    }
    ```

- 변수의 종류

  ```c
  test.c
  int externnum = 60;
  ```

  ```c
  #include <stdio.h>
  int globalnum; //전역변수 선언, 초기화 하지 않아도 0 설정
  extern int externnum; //외부변수 선언, 외부 함수도 선언 및 호출 가능(외부 함수 선언은 extern 생략 가능, 외부에서 함수 다 만들 수 있음)
  void grow(void); //grow함수 선언
  
  int main(void){
      int localnum = 0 //지역변수 선언
      printf("global %d, local %d",globalnum,localnum);
      //global 0, local 0
      grow();
      printf("global %d, local %d",globalnum,localnum);
      //global 60, local 0
      printf("static %d",staticnum);
      //static 60
      printf("external %d",externnum);
      //external 60
      return 0;
  }
  
  void grow(void){
      int localnum = 60;
      static int staticnum = 60;
      globalnum=60;
  }
  ```

  - 지역변수: 함수{} 내부에서 사용, 매개변수(입력변수)로 사용
  - 전역변수: {} 위부에서 선언, 프로그램이 종료할 때 메모리 사라짐
  - **정적변수**: 자료형 앞에 static 붙임, {}내에서 선언 (지역+전역), 초기화를 한번만 해줌(처음 선언해줄때만!), 프로그램 종료 시 소멸, 외부변수로 접근 불가
  - 외부변수: 자료형 앞에 extern 붙임, 외부 파일의 전역 변수를 참조
  - 레지스터 변수: 자료형 앞에 resister 붙임, CPU 내부의 레지스터에 변수를 할당, 처리속도 fast

- 재귀 함수

  - 함수 내에서 자기 자신을 호출 하는 함수
  - static으로 선언하면 초기화 반복 막음





#### 1차원 배열

- 배열: 같은 자료형을 가진 연속된 메모리 공간, 많은 양 데이터 처리 시 유용

  ```c
  int array_name[10]; //자료형 배열이름[배열길이];
  
  int array1[3] = {1,2,3}; //{1,2,3}
  int array2[] = {1,2,3}; //{1,2,3}, 배열길이가 없으면 선언만큼 생김
  int array3[3] = {1}; //{1,0,0}, 선언하면서 바로 값 넣으면 0으로 채워짐
  
  int array4[3];
  array4 = {1,2,3}; //에러 발생
  array4[0] = 1;
  array4[1] = 2;
  array4[2] = 3;
  
  int a = 3;
  int array5[a]; //에러 발생, 배열 선언 시 길이는 변수로 들어가면 안됨, 선언 후 데이터를 다룰 때는 가능
  ```

- 주소와 값 참조

  - 배열의 주소: &배열요소의위치 ex) &array[2], array배열의 3번째 값 주소
  - 배열 이름의 주소는 배열의 시작 주소, &array == &array[0]
  - 배열 요소의 개별 주소는 배열의 시작 주소를 기준으로 차이가 남, &array[1] == array+1, &array[2] == array+2
  - '별'연산자: 메모리 공간에 저장된 값을 참조 ex)*&array[2] = 배열의 3번째 값,  *&array[2] == array[2]

  ```c
  int array[3] = {1,2,3};
  
  printf("%x %x %x \n", array+0, array+1, array+2);
  // array값들의 주소를 출력
  printf("%d %d %d \n", *(array+0), *(array+1), *(array+2));
  // array값들을 출력, array[n] == *(array+n) == *&array[n]★★★
  printf("%d %d \n", *(array+0), *array);
  // *array+3 != *(array+3)
  
  return 0;
  
  // 값참조는 array에 정확한 위치값을 선정하거나 주소앞에 *붙이기!
  ```

  



#### 다차원 배열

```c
//2차원 배열
int array_name[2][4]; //2행4열
//ㅁㅁㅁㅁ
//ㅁㅁㅁㅁ

int array[0][0] = 1;
int array[0][1] = 2;
...

int array[2][4] = {0,1,2,3,4,5,6,7}; //행단위로 채움
int array[2][4] = {0,1,2,3}; //나머지는 0으로 채움
int array[2][4] = {{0,1,2},{4}} //행단위 초기화
//0 1 2 0
//4 0 0 0

int array_name[][] = {1,2,3,4} //에러
int array_name[2][] = {1,2,3,4} //에러
int array_name[][2] = {1,2,3,4,5,6} //정상, 열의 길이는 반드시 설정
//1 2
//3 4
//5 6

//3차원 배열
int array_name[3][3][3] = {{1,2,3,4,5,6,7,8,9},{},{}}
```

- 2차원 배열의 주소와 값의 참조

```c
int array[2][2] = {10,20,30,40};

/*
주소 참조
&array[행][열] == array[행]+열 == *(array+행)+열

&array[0][0] == array[0] == *(array+0) == *array
&array[1][0] == array[1] == *(array+1)
array[n]은 n번째 열의 첫번째 주소를 의미
*/

/*
값 참조(주소 앞에 *붙이기)
*&array[행][열] == *(array[행]+열) == *(*(array+행)+열) == array[행][열]
*/
```





#### 포인터

- 특징

  - 화살표, 변수, 주소저장 3가지 기억하기!

  - 주소를 저장하는 변수로 C언어 장점 중 하나

  - 메모리 주소를 참조해서 다양한 자료형 변수에 접근, 조작 가능

- 포인터 변수 선언

  - int* pointer=NULL;
  - 자료형* 포인터변수이름 = NULL포인터설정 ;
  - 선택한 자료형 주소를 저장하는 포인터 변수
  - 모든 포인터 변수는 4바이트!!!!

  ```c
  char c="A";
  char* cp=NuLL;
  cp=&c; //c의 주소 저장
  //같은 표현: char* cp=&c; 바로 선언
  
  printf("%x %c %c \n", &c, c, *&c); //c주소 A A
  printf("%x %x %x \n", &cp, cp, *&cp); //cp메모리주소 c주소 c주소
  /*
  &cp는 포인터변수를 저장하는 메모리 주소
  cp는 포인터변수가 저장하고 있는 값의 주소 == &c == *&cp
  */
  
  printf("%c \n",c); //직접 접근, c값
  printf("%c \n",*cp); //간접 접근, *c의주소 == c값
  // c == *&c == *cp
  ```

  ```c
  #include <stdio.h>
  int main(){
      int a=0, b=0, c=0;
      int* ip=NULL;
      
      ip=&a; //pointer에 a주소 저장
      *ip = 10; //ip값의 값(a값에 간접 접근)
      printf("%d %d %d %d",a,b,c,*ip);
      // 10 0 0 10
      
      ip=&b; //pointer에 b주소로 변경
      *ip = 20; //ip값의 값(b값에 간접 접근)
      printf("%d %d %d %d",a,b,c,*ip);
      // 10 20 0 20
      
      ip=&c; //pointer에 c주소로 변경
      *ip = 30; //ip값의 값(c값에 간접 접근)
      printf("%d %d %d %d",a,b,c,*ip);
      // 10 20 30 30
      
      return 0; 
  }
  ```

- 잘못된 포인터 사용

  ```c
  // 포인터변수에 주소를 저장하지 않음
  int* ip=NULL;
  *ip=10000;
  
  //포인터 변수에 이상한 주소 저장
  int* ip=123456789;
  *ip=1020;
  ```





#### 다차원 포인터

```c
int* p1=NULL; //1차원 포인터변수
int** p2=NULL; //2차원 포인터변수 (2차원 주소리스트)
int*** p3=NULL; //3차원 포인터변수 (3차원 주소리스트)
/*
파이썬에선
[[[0,0],[0,1],[0,2]],
 [[1,0],[1,1],[1,2]],
 [[2,0],[2,1],[2,2]]]
이런 느낌..
*/

/* 
동일한 의미를 가지는 표현
- pointer3 == &pointer2
- *pointer3 == pointer2 == &pointer1
- **pointer3 == *pointer2 == pointer1 == &num1
- ***pointer3 == **pointer2 == *pointer1 == num1 == 4(데이터값)
*/
```

- 동일한 주소를 참조하는 값을 변경하면 참조값들 모두 바뀜





#### 주소의 가감산

- 포인터 주소는 4바이트 간격으로 가감
- 자료형 주소는 자료형 별 바이트 간격으로 가감(char: 1byte, int: 4byte, ...)

```c
int array[3] = {1,2,3};
int* ip=NULL;
int** ipp=NULL;
ip=array;
ipp=&ip;

/*
1 == array[0] == *(ip+0) == *(*ipp+0)
2 == array[1] == *(ip+1) == *(*ipp+1)
3 == array[2] == *(ip+2) == *(*ipp+2)
*/
```





#### 함수 포인터

```c
void add(double num1, double num2); //포인팅 대상 함수
void (*pointer) (int, int); //함수 포인터 선언
pointer = add; //함수 포인터에 함수 시작 주소 저장
/* void (*add) (int,int); 한줄로 가능하나 pointer변수명으로 여러 조건 처리하기 위해 쩌렇게 하면 좋아! */
pointer(3.1,5.1); //함수 포인터를 이용한 함수 호출

//예시
int x,z;
char c;
void (*pointer) (int,int);
scanf("%d %c %d",&x, &c, &x);

if(c=='+')
    pointer=add;
else if(c=='-')
    pointer=subtract;

pointer(x,z);
```

- 일반적인 함수 호출보다 빠른 처리 속도
- 컴파일러, 인터프리터, 게임프로그래밍 등 시스템 프로그래밍 분야에 이용