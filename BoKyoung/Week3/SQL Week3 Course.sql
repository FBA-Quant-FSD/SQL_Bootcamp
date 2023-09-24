## Section10 : Conditional Expressions and Procedures

## CASE
# IF/ELSE와 유사

사용법
#1. general CASE
#2. CASE expression

#1. general CASE - more flexible
CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    ELSE some_other_result
END

ex)
SELECT a,
CASE WHEN a = 1 THEN 'one'
     WHEN a = 2 THEN 'two'
ELSE 'other' AS label
END
FROM test;


#2. CASE expression
CASE expression
    WHEN value1 THEN result1
    WHEN value2 THEN result2
    ELSE some_other_result
END

ex)
SELECT a,
CASE WHEN 1 THEN 'one'
     WHEN 2 THEN 'two'
     ELSE 'other'
END
FROM test;


#pgAdmin example
# 1
# customer_id가 가입 순서라고 했을 때
# 100이하 고객은 'Premium'으로, 100~200 고객은 'Plus'로 분류하기
SELECT customer_id, #column
CASE 
	WHEN (customer_id <= 100) THEN 'Premium'
	WHEN (customer_id BETWEEN 100 and 200) THEN 'Plus'
	ELSE 'Normal'
END AS customer_class
FROM customer

# 2
# 2 이런 경우 Case expression이 나음 but 일반적인 경우 #1이 더 유연
SELECT customer_id,
CASE customer_id
	WHEN 2 THEN 'Winner'
	WHEN 5 THEN 'Second Place'
	ELSE 'Normal'
END AS raffle_results
FROM customer


#활용하기
SELECT 
CASE rental_rate 
	WHEN 0.99 THEN 1
	ELSE 0
END
FROM film

# 0.99원 짜리 영화 : 할인하는 것
# SUM()함수로 묶으면 0.99원짜리 영화가 몇 개인지 출력된다
SELECT
SUM(CASE rental_rate 
	WHEN 0.99 THEN 1
	ELSE 0
END) AS number_of_bargains
FROM film
# result : number_of_bargains : 341


SELECT
SUM(CASE rental_rate 
	WHEN 0.99 THEN 1
	ELSE 0
END) AS bargains,
SUM(CASE rental_rate
   WHEN 2.99 THEN 1
   ELSE 0
END) AS regular
FROM film
# result : bargains : 341 / regular : 323


## COALESCE
# accpts an unlimited number of arguments
# returns the first argument that is NOT NULL
# null 값을 대체할 때 유용
# TABLE 자체의 값을 바꾸지는 않고 연산시에 적용된다

ex)
SELECT COALESCE(NULL, 2, 3)
result : 2

#discount column의 값이 null이면 price-0을 해준다
SELECT item,(price-COALESCE(discount,0))
AS final FROM table


## CAST
# data type 변경 (ex. string -> integer)
# 모든 data type 변경이 가능한 것 x ('5'->integer O)
#                                  ('five'->integer X)

사용법
# 1 CAST function
SELECT CAST('5' AS INTEGER)

# 2 PostgreSQL CAST operator
SELECT '5'::INTEGER

ex)
SELECT CAST(date AS TIMESTAMP)
FROM table

# 활용
# inventory_id의 길이 파악하기
# inventory_id는 INTEGER이므로 길이 파악 위해 VARCHAR로 전환
SELECT CHAR_LENGTH(CAST(inventory_id AS VARCHAR))
FROM rental


## NULLIF
# takes in 2 inputs and returns NULL if both are equal
# otherwise returns the first argument passed

#NULLIF(arg1,arg2)


# 활용
CREATE TABLE depts(
	first_name VARCHAR(50),
	department VARCHAR(50)
)

INSERT INTO depts(
	first_name,
	department 
)
VALUES
('Vinton','A'),
('Lauren','A'),
('Claire','B');

SELECT (
SUM(CASE WHEN department = 'A' THEN 1 ELSE 0 END)/
SUM(CASE WHEN department = 'B' THEN 1 ELSE 0 END)
) AS department_ratio
FROM depts
# result : 2

DELETE FROM depts
WHERE department = 'B'


# ERROR : 다시 나누면 오류! ('B'가 NULL)
SELECT (
SUM(CASE WHEN department = 'A' THEN 1 ELSE 0 END)/
SUM(CASE WHEN department = 'B' THEN 1 ELSE 0 END)
) AS department_ratio
FROM depts


# GOOD : error 대신 [null] 값 출력
SELECT (
SUM(CASE WHEN department = 'A' THEN 1 ELSE 0 END)/
	NULLIF(   
SUM(CASE WHEN department = 'B' THEN 1 ELSE 0 END),0)
) AS department_ratio
FROM depts


## Views
# database object that is of a stored query
# does not store data physically, it simply stores the query
# 작업하면서 많이 쓰는 table, condition의 combination을
# 매번 다시 쓰는 대신 간단하게 불러오기

# 활용
CREATE VIEW customer_info AS  #위의 한 줄만 추가하면 된다
SELECT first_name,last_name,address 
FROM customer
INNER JOIN address
ON customer.address_id = address.address_id

# 호출
SELECT * FROM customer_info

# 변경하기
CREATE OR REPLACE VIEW customer_info AS
SELECT first_name,last_name,address,district 
FROM customer
INNER JOIN address
ON customer.address_id = address.address_id

#이름 변경하기
ALTER VIEW customer_info
RENAME to c_info


## Importing and Exporting data
# 모든 Import가 성공하는 것 x
# SQL과 호환되도록 해야한다
# compatible file types and examples documentation :
https://www.postgresql.org/docs/12/sql-copy.html

# Import command DOES NOT create a table
# It assumes a table is already created

## 1. Import
#Step1. csv 파일 만들기
#Step2. 파일이름 재설정, 경로 파악

#Step3. pgAdmin에서 TABLE 생성
CREATE TABLE simple(
a INTEGER,
b INTEGER,
c INTEGER
)

#Step4. simple테이블 우클릭 -> Import
(Options에서 Header -> Yes 해주기)

#Step5. Import 확인
SELECT * FROM simple
-> CSV 파일로 만든 내용이 정상적으로 출력된다


## 2. Export
#Step1. simple테이블 우클릭 -> Export
#Step2. 실제 파일 Export 되었는지 확인