-- 코드를 입력하세요
SELECT SUBSTR(PRODUCT_CODE,1,2) CATEGORY, COUNT(PRODUCT_ID) PRODUCTS
    FROM PRODUCT
    GROUP BY CATEGORY