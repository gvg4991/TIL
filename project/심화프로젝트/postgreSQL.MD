# PostgreSQL 연동하기



### PostgreSQL 설치 및 설정

PostgresSQL Database 설치

- [설치 경로](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads#windows) - 최신 버전인 12.0을 설치함
- 설치 방법은 [링크](http://www.postgresqltutorial.com/install-postgresql/) 참조

1. 설치 후 PgAdmin4 실행
   - 설치 시, 저장한 비밀번호 ㅇ비력

2. 유저 생성: Login/Group Roles 우클릭 후, Create -> Login/Group Role
   - General: Name 입력
   - Definition: Password 입력
   - Privileges: 권한부여 설정
   - 이후, 저장
3.  데이터 베이스 생성: Database 우클릭 후, Create -> Database
   - General에서 Database와 Owner를 입력
   - Database에는 생성한 DB의 이름을 입력
   - Owner에는 생성한 유저 이름을 입력



### Django 내 설정

- Django 프로젝트 내에서 psycopg2 설치
  - `pip install psycopg2`
- settings.py 내 DATABASES를 설정

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'sample_db', #PostgreSQL 내 DB 이름 입력
        'USER':'harry', # PostgreSQL 유저 명 입력
        'PASSWORD':'1234',# PostgreSQL 유저 비밀번호 입력
        'HOST':'localhost',
        'PORT':'5432'
    }
}
```

- 설치 후, 마이그레이션 재 설정
  - `Python manage.py makemigrations`
  - `python manage.py migrate`

- PgAdmin 내 DB > Schemas > Tables를 들어가면 테이블 확인 가능





------



#### postgreSQL

###### DB

Server [localhost]:
Database [postgres]: dodam_db
Port [5432]:
Username [postgres]: mino
Password for user mino:
psql (12.0)
Type "help" for help.

**dodam_db=# \l (엘)**
                                       List of databases
   Name    |  Owner   | Encoding |     Collate      |      Ctype       |   Access privileges
-----------+----------+----------+------------------+------------------+-----------------------
 dodam_db  | mino     | UTF8     | Korean_Korea.949 | Korean_Korea.949 |
 postgres  | postgres | UTF8     | Korean_Korea.949 | Korean_Korea.949 |
 template0 | postgres | UTF8     | Korean_Korea.949 | Korean_Korea.949 | =c/postgres          +
           |          |          |                  |                  | postgres=CTc/postgres
 template1 | postgres | UTF8     | Korean_Korea.949 | Korean_Korea.949 | =c/postgres          +
           |          |          |                  |                  | postgres=CTc/postgres
(4 rows)

**dodam_db=# \c dodam_db**
You are now connected to database "dodam_db" as user "mino".
**dodam_db=# \dt:**
                  List of relations
 Schema |            Name            | Type  | Owner
--------+----------------------------+-------+-------
 public | api_profile                | table | mino
 public | auth_group                 | table | mino
 public | auth_group_permissions     | table | mino
 public | auth_permission            | table | mino
 public | auth_user                  | table | mino
 public | auth_user_groups           | table | mino
 public | auth_user_user_permissions | table | mino
 public | authtoken_token            | table | mino
 public | django_admin_log           | table | mino
 public | django_content_type        | table | mino
 public | django_migrations          | table | mino
 public | django_session             | table | mino
(12 rows)

**dodam_db=# select * from api_profile;**
 id | email | nickname | age | gender | user_id
----+-------+----------+-----+--------+---------
(0 rows)

**dodam_db=# select * from auth_user;**
 id |                                    password                                    |          last_login          | is_superuser | username | first_name | last_name |      email      | is_staff | is_active |          date_joined          ----+--------------------------------------------------------------------------------+------------------------------+--------------+----------+------------+-----------+-----------------+----------+-----------+-------------------------------  1 | pbkdf2_sha256$150000$fN0HWThcQFR3$jSGO9PXjocZKagiGHN44dxDprN6tFt3ADvHMSMs8P7Q= | 2019-10-23 11:13:55.17921+09 | t            | admin    |            |           | admin@admin.com | t        | t         | 2019-10-23 11:13:07.291937+09
(1 row)


dodam_db=#



















------

cmd > ipconfig > 

무선 LAN 어댑터 Wi-Fi:
   IPv4 주소 . . . . . . . . . : 192.168.100.60

front > src > api > index.js > const apiUrl = 'http://192.168.100.60:8000/api'



python manage.py runserver 192.168.100.60:8000



①②③④⑤ 

