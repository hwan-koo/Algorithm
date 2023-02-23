-- 코드를 입력하세요
SELECT MONTH(START_DATE) MONTH, CAR_ID, COUNT(CAR_ID) RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE CAR_ID IN 
(SELECT CAR_ID
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE MONTH(START_DATE) BETWEEN 8 and 10
GROUP BY CAR_ID
    HAVING COUNT(CAR_ID) >= 5
) AND MONTH(START_DATE) BETWEEN 8 and 10
GROUP BY MONTH,CAR_ID
ORDER BY MONTH(START_DATE) ASC, CAR_ID DESC