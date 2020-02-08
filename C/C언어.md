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

