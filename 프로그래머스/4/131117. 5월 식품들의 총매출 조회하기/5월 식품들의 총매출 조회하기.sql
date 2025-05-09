-- 코드를 입력하세요
SELECT A.PRODUCT_ID, B.PRODUCT_NAME, SUM(A.AMOUNT) * B.PRICE AS TOTAL_SALES
FROM FOOD_ORDER AS A
INNER JOIN FOOD_PRODUCT AS B
ON A.PRODUCT_ID = B.PRODUCT_ID
WHERE (A.PRODUCE_DATE >= '2022-04-30' AND A.PRODUCE_DATE < '2022-06-01')
GROUP BY A.PRODUCT_ID, B.PRODUCT_ID
ORDER BY TOTAL_SALES DESC, A.PRODUCT_ID ASC;