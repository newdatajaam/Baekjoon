-- 코드를 작성해주세요
SELECT ID, EMAIL, FIRST_NAME, LAST_NAME FROM DEVELOPER_INFOS 
WHERE SKILL_3 = 'Python' OR SKILL_2 = 'Python' OR SKILL_1 = 'Python'
ORDER BY ID ASC;