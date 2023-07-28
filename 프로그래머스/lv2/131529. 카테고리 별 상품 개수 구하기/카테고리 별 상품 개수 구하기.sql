SELECT LEFT(PRODUCT_CODE, 2) AS CATEGORY, COUNT(PRODUCT_ID) AS PRODUCTS 
FROM PRODUCT
GROUP BY CATEGORY
ORDER BY PRODUCT_CODE ASC;
