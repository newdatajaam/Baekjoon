-- 코드를 입력하세요
SELECT count(*) AS USERS from user_info
WHERE AGE >= 20 and AGE <= 29 and Year(joined) = '2021';