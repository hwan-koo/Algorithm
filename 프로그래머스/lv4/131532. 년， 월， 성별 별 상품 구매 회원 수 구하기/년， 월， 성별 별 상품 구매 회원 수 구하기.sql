-- 코드를 입력하세요
SELECT YEAR(SALES_DATE) YEAR, MONTH(SALES_DATE) MONTH, GENDER, COUNT(DISTINCT O.USER_ID) USERS
    FROM USER_INFO U, ONLINE_SALE O
    WHERE GENDER IS NOT NULL AND U.USER_ID = O.USER_ID
    GROUP BY YEAR, MONTH, GENDER
    ORDER BY YEAR, MONTH, GENDER