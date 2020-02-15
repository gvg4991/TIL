# Oracle

- oracle 관련 인강

[생활코딩]: https://www.youtube.com/watchv=RK7BMNxi9OM&amp;list=PLuHgQVnccGMB5q5uJIDhLlcC2V6tyXhY6&amp;index=4	"오라클"
[프리렉]: https://www.youtube.com/watch?v=Q0rt3b2bMII&amp;list=PL7mmuO705dG0d1Z_6AoWJk_vdLgJnv-L3	"오라클 교과서"
[프리렉 열혈강의]: https://freelec.co.kr/lecture/%ec%97%b4%ed%98%88%ea%b0%95%ec%9d%98-%ec%98%a4%eb%9d%bc%ed%81%b4-sql-pl-sql/	"오라클 SQL&PL,SQL"



#### 데이터베이스

- 정의
  - 통합된 데이터: 중복 최소화, 동시공유
  - 저장된 데이터: 실시간 접근가능
  - 운영 데이터: 실질적 사용, 지속적인 변화
  - 공용 데이터: 데이터의 집합, 내용참조
- 기본 용어
  - 테이블: 데이터를 저장하는 단위로, 필드와 레코드로 구분
  - 필드: 데이터의 새로 열, 데이터의 속성
  - 레코드: 데이터의 가로 행, 독립적으로 저장

- DBMS

  - DB관리 시스템: 데이터의 조작, 저장, 관리를 프로그램과 분리
  - 장점
    - 데이터의 중복 최소화, 데이터의 공통 사용
    - 데이터의 일관성, 무결성
    - 보안성, 표준화 가능, 요구사항 파악
  - 종류
    - 계층형 DBMS: 계층형 모델 ex) 조직도
    - 망형 DBMS: 네트워크 모델
    - 관계형 DBMS: 관계형 모델, 2차원의 필드와 레코드로 구성됨
    - 객체형 DBMS: 객체지향 모델

- DB 설계

  - DB 설계 개념

    현실세계 - 정보 모형화 - 개념세계(정보 구조) - 자료 모형화 - 논리적 자료구조 - 자료 구조화 - 데이터베이스(물리적 구조) - 일치성 - 현실세계

  - 설계 과정

    시스템 요구 분석 - 자료분석/ 엔티티 도출 - 개념적 DB 설계 - ERD(관계 설정)작성 - 논리적 DB 설계 - 자료사전을 통해 표준화 - 물리적 DB 설계 - DB 모델링 점검(오류 점검) - DB 구축 - 완료

- DB 모델링

  - 개념

    - 요구를 분석하여 <u>논리 모델 구성</u>, 물리 모델을 사용해 DB에 반영

    - 기본요소: 엔티티(테이블), 속성(필드), 관계(키와, 참조키, 두개의 엔티티 간의 상호관계)
    - 관계: 1:1, 1:다, 다:다, 재귀 관계

  - 정규화

    - 제1정규화(1NF)
      - 엔티티 내의 모든 속성은 하나의 값을 가짐
      - 컬럼내에 반복되는 형태 존재x -> 반복내용 별도의 엔티티로 만들기
    - 제2정규화(2NF, 기본키 검증)
      - 모든 속성은 반드시 식별자(기본키, 하나의 레코드를 대표) 전부에 종속
      - 식별자 일부에만 종속되어선 안됨
    - 제3정규화(3NF)
      - 식별자가 아닌 모든 속성간에는 서로 종속 될 수 없음
      - 식별자에 종속되지 않은 필드 제거, 모든 속성은 식별자에 종속
    - 제4정규화(BCNF)
      - 하나의 엔티티는 다 대 다 관계를 가질 수 없음
      - 관계에서 다 대 다의 관계를 제거
      - 다대다 관계 해소용 새로운 엔티티가 발생



#### 오라클

- 오라클 아키텍처
  - 파일저장 부분: 데이터가 직접적으로 저장됨
  - 프로세스 부분: 사용자와 작업이 동작됨
  - 메모리 부분: 프로세스와 저장을 연결해줌, 캐시

- 파일 저장 부분
  - 물리적 구조
    - 데이터 파일: DB의 실제 데이터가 포함된 파일
    - 리두 로그 파일: 데이터의 변경 사항을 기록
    - 컨트롤 파일: 데이터베이스 무결성을 관리, 데이터 파일과 리두로그 파일을 제어
  - 논리적 구조
    - 크기별 구분: 데이터 블록 < 익스텐트 < 세그먼트 < 테이블 스페이스
- 메모리 부분
  - 시스템 공유 영역(SGA)
  - 프로그램 공유 영역(PGA)
- 프로세스 부분
  - 오라클 프로세스: 사용자 프로세스 + 서버 프로세스 + 백그라운드 프로세스
  - 주요 프로세스
- 오라클 구동 원리(백업, 복구와 연관 됨)
  - 시작: shutdown - nomount - mount - open
    - 1단계: oracle instance startup
      - SGA 할당 + 백그라운드 프로세스 기동
      - 주로 컨트롤 파일 손상, DB를 새로 만들 때 사용
      - 명령: startup nomount
    - 2단계: Database mounted
      - 인스턴스와 DB 연결
      - 데이터 파일 위치나 이름을 변경 / 온라인 리두 로그 파일을 추가 / 아카이브 옵션 활성화나 비활성화 할 때 / 전체 DB 복구 작업 수행할 때 사용
      - 명령: startup mount
    - 3단계: Database opend
      - 사용자 접속이 가능하게 온라인 로그 파일과 데이터 파일을 연다
      - 명령: alter database open
  - 종료: open - mount - nomount - shutdown
    - 1단계: Database closed
      - 오라클에 더 이상의 접속이 안됨
      - 모든 사용자가 정상 종료하면 DB에 쓰기를 수행
    - 2단계: Database dismounted
      - 인스턴스와 DB를 분리하고 컨트롤 파일을 닫음
    - 3단계: oracle instance shutdown
      - SGA가 반환되고 백그라운드 프로세스 종료
- 오라클 설치
  - 오라클 회원 가입
  - 오라클 받기
  - 오라클 설치
  - 오라클 삭제
- 접속 관련 파일 확인
  - listener.ora: 서버 리스너의 설정과 관련된 파일
  - tnsnames.ora: 클라이언트가 서버와 접속을 하려 할 때 필요한 정보를 설정하는 파일
- 리스너 동작 확인
  - cmd로 커맨드 창 실행
  - lsnrctl로 리스너 관리창 접속
  - status로 리스너 상태 확인
  - exit로 나가기



#### 오라클 접속

- 접속계정 바꾸기

  - SQL*PLUS를 이용해 시스템 계정 접속

  - 위의 계정 바꾸기 명령을 이용해 HR계정 활성화

  - DISC 명령을 이용한 시스템 계정 접속 해제

  - HR 계정으로 재접속

  - 명령: conn system/암호 (접속)

    ​	  alter user hr

    ​	  identified by hr

    ​	  account unlock; (user변경)

    ​	  disc (종료)

    ​	  conn hr/hr (설정 uer로 재접속)

- 오라클 유틸리티

  - SQL*PLUS: 기본으로 제공되는 프로그램
  - TOAD: 대표적인 오라클 유틸리티
  - ORACLE SQL DEVELOPER: 오라클에서 제공하는 무료 유틸리티
  - WinSQL: ODBC를 이용한 데이터베이스 유틸리티



#### 데이터 객체

- TOAD로 본 데이터 객체
  - database - schema browser
  - browser style 변경
    - dropdown
    - tabbed
    - tabbed
    - treeview
  - TOAD관리 데이터 객체
- SQL Developoer로 본 데이터 객체



#### 자료형

- 기본 문법

  - 자료형 선언

    CREATE TABLE 테이블명(변수명 자료형(크기[단위]));

  - 자료형의 자료 등록

    INSERT INTO 테이블명(변수명[,변수명,...])

    VALUES (값[,값,...]);

  - 자료형의 자료 조회

    SELECT 변수명[, 변수명,...]

    FROM 테이블명;

- 문자 자료형

  - 크기를 따로 지정하지 않으면 영어와 한글 구분없이 2BYTE 단위로 저장됨 (원래 영어:1BYTE, 한글: 3BYTE)

  - CHAR

    - CHAR은 고정길이 문자열을 저장, 자신이 차지한 것을 제외한 나머지 BYTE는 space로 채워짐

    - 사용법: 변수명 CHAR (크기 [CHAR|BYTE])

    - 예시: COL_CHAR1 CHAR(10 BYTE)

  - VARCHAR2

    - 가변길이 문자열을 저장, 자신이 차지하는 만큼 BYTE 저장
    - 사용법: 변수명 VARCHAR2 (크기 [CHAR|BYTE])
    - 예시: COL_VARCHAR1 VARCHAR2 (10 BYTE)

  - LONG

    - VARCHAR2의 최대크기 제한보다 큰 텍스트 문자 열을 저장 할 때 사용하며, 최대 2GB까지 저장 가능
    - 사용법: 변수명 LONG
    - 예시: COL_LONG LONG
    - 제한 사항
      - 한 테이블에 하나의 LONG컬럼 허용
      - 무결성 제약 조건에 사용 불가
      - SELECT 문에서 WHERE, GROUP BY, ORDER BY 등과 사용 불가

  - CLOB, NCLOB

    - 기존의 LONG을 대체하여 LONG의 제한사항 극복, 최대 4GB까지 저장 가능, NCLOB는 다국적 언어를 저장 가능
    - 사용법: 변수명 CLOB
    - 예시: CLO_CLOB1 CLOB

- 숫자 자료형

  - NUMBER
    - 정수, 실수와 같은 숫자형 자료를 저장
    - 사용법: 변수명 NUMBER(정밀도[, 스케일])
    - 예시
      - 부동소수점: COL_NUM1 NUMBER
      - 고정소수점: COL_NUM1 NUMBER(5) / COL_NUM1 NUMBER(5,2) / COL_NUM1 NUMBER(*,2)

- 날짜 자료형

  - DATE

    - 오라클의 가장 기본
    - 사용법: 변수명 DATE
    - 예시: COL_DATE1 DATE

  - TIMESTAMP

    - 9i 부터 지원되는 날짜 자료형
    - 사용법: 변수명 TIMESTAMP[(정밀도)] WITH [TIME ZONE|LOCAL TIME ZONE]
    - 예시: TIMESTAMP(0) WITH LOCAL TIME ZONE

  - INTERVAL

    - 시간 간격에 대한 자료형

    - 사용법: 변수명 INTERVAL YEAR[(연 정밀도)] TO MONTH

      ​	      변수명 INTERVAL DAY[(일 정밀도)] TO SECOND[ (단편 초 정밀도)]

    - 예시: COL_INTER1 INTERVAL DAY(3) TO SECOND(2)

- 기타 자료형

  - RAW / LONG RAW
    - 이진 데이터 저장
    - 사용법: 변수명 ROW(크기)
    - 예시: COL_ROW1 ROW(200)
  - ROWID
    - 테이블 내의 한 행에 대한 논리적인 주솟값을 가짐, 특정 행을 가장 빨리 찾음
    - 사용법: 변수명 ROWID
    - 예시: COL_ROW1 ROWID
  - BFILE
    - 이진 데이터를 DB 외부에 저장
  - BLOB
    - 이진 데이터를 DB 내부에 저장
  - XMLTYPE
    - XML데이터를 저장하고 처리