# 데이터 베이스(DB)

데이터베이스란? 체계화된 데이터의 모임.

SQL언어로 조작을 할 수 있는 데이터의 모임.

> 여러 사람에 의해 공유되어 사용될 목적으로 통합하여 관리되는 데이터의 집합을 말하는 개념이다. 줄여서 DB라고도 하며, 특정 다수의 이용자들에게 필요한 정보를 제공한다든지 조직 내에서 필요로 하는 정보를 체계적으로 축적하여 그 조직 내의 이용자에게 필요한 정보를 제공하는 정보 서비스 기관의 심장부에 해당된다.



대표적인 DB: 

RDBMS(관계형 데이터 베이스 관리 시스템): 관계형 모델을 기반으로 하는 데이터베이스 관리 시스템. 대표적인 오픈소스 RDMBS (MySQL, SQLite, PostgreSQL)와 ORACLE, MS SQL 등이 있음.



SQLite

서버가 아닌 응용 프로그램에 넣어 사용하는 비교적 가벼운 데이터베이스이다. 구글 안드로이드 운영체제에 기본적으로 탑재댄 데이터베이스이며 임베디드 소프트웨어에도 많이 활용되고 있다. 로컬에서 간단한 DB 구성을 할 수 있으며, 오픈소스 프로젝트이므로 자유롭게 사용이 가능하다.



스키마(scheme/schema)

데이터베이스에서 자료의 구조, 표현방법, 관계등을 정의한 구조

데이터베이스의 구조와 제약조건에 관련한 전반적인 명세를 기술 한 것. 이를 바탕으로 테이블 등을 생성 할 수 있음.



데이터베이스의 구조

테이블

열(column): 각 열에는 고유한 데이터 형식이 지정된다. Integer, text, null 등

행(row), 레코드: 테이블의 데이터는 행에 저장된다. 즉 user 테이블에 4명의 고객정보가 저장되어 있으며, 행은 4개가 존재한다.

기본키(Primary Key): 각 행(레코드)의 고유값으로 Primary Key로 불린다. 반드시 설정해야하며, 데이터베이스 관리 및 관계 설정시 주요하게 활용된다..



SQL?

SQL(Structured Query Langauage)는 관계형 데이터 베이스 관리 시스템의 데이터를 관리하기 위해 설계뙨 특수 목적의 프로그래밍 언어이다.RDBMS에서 자료의 검색과 관리, DB의 스키마 생성과 수정......



SQL의 문법

데이터 정의 언어(DDL): 데이터를 정의하기 위한 언어. 관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어이다. ex) CREATE, DROP, ALTER

데이터 조작 언어(DML): 데이터를 저장, 수정 삭제, 조회등을 하기 위한 언어 ex) INSTER, UPDATE, DELETE, SELECT

데이터 제어 언어(DCL): 데이터 베이스 사용자의 권한 제어를 위한 사용되는 언어 ex) GRANT, REVOKE, COMMIT, ROCKBACK



### C9에서 SQL 실행하기

```bash
#C9에 내장되어있는 sqlite를 실행하기
harrylee0810:~/workspace/flask/sql $ sqlite3

#실행하면, 다음과 같은 코드가 실행된다.
SQLite version 3.8.2 2013-12-06 14:53:30
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> 

#examples라는 테이블을 생성
sqlite> .mode csv
sqlite> .import hellodb.csv examples

#SELECT문은 데이터베이스에서 특정한 행을 출력한다.
sqlite> SELECT * FROM examples;
1,"길동","홍",600,"충청도",010-2424-1232

#header를 on하고, 모드를 csv가 아닌 column으로 변경해보자
sqlite> .headers on
sqlite> .mode column
sqlite> SELECT*FROM examples;
id          first_name  last_name   age         country     phone        
----------  ----------  ----------  ----------  ----------  -------------
1           길동      	홍         600         충청도   	010-2424-1232

#sqlite 종료하기
#명령어 앞에 .을 쓰는것은 SQL의 언어가아니라 sqlite를 조작하는 명령어임.
sqlite> .exit
```



### Database 생성

```bash
#데이터 베이스 생성하기(sqlite3는 확장자는 제한이 없음. tutorial.sqlite3 라는 파일을 생성)
harrylee0810:~/workspace/flask/sql $ sqlite3 tutorial.sqlite3

SQLite version 3.8.2 2013-12-06 14:53:30
Enter ".help" for instructions
Enter SQL statements terminated with a ";"

#.databases: 생성된 데이터베이스의 목록을 열어줌.
seq  name             file                                                      
---  ---------------  ----------------------------------------------------------
0    main             /home/ubuntu/workspace/flask/sql/tutorial.sqlite3         
```

