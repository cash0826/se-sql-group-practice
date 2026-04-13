import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

overview = pd.read_sql("""
SELECT *
FROM products;
""", conn)

# print(overview)

count_product_line = pd.read_sql("""
SELECT productLine, COUNT(*) as count
FROM products
GROUP BY productLine
ORDER BY count DESC;
""", conn)

# print(count_product_line)

avg_price_product_line = pd.read_sql("""
SELECT productLine, 
AVG(buyPrice) AS avgPrice
FROM products
GROUP BY productLine
ORDER BY avgPrice DESC;
""", conn)

# print (avg_price_product_line)

min_max = pd.read_sql("""
SELECT productLine, 
MIN(MSRP) AS minMSRP,
MAX(MSRP) AS maxMSRP
FROM products
GROUP BY productLine
""", conn)

# print(min_max)

min_max_over_50 = pd.read_sql("""
SELECT productLine, 
MIN(MSRP) AS minMSRP,
MAX(MSRP) AS maxMSRP
FROM products
WHERE MSRP >= 50
GROUP BY productLine
""", conn)

# print(min_max_over_50)

avg_over_50 = pd.read_sql("""
SELECT productLine, 
AVG(buyPrice) AS avgPrice
FROM products
GROUP BY productLine
HAVING avgPrice >= 50
ORDER BY avgPrice DESC;
""", conn)

# print(avg_over_50)

complex_q = pd.read_sql("""
SELECT productLine,
AVG(buyPrice) AS avgBuyPrice,
AVG(MSRP) AS avgMSRP 
FROM products
WHERE MSRP >= 50
GROUP BY productLine
HAVING avgBuyPrice >= 50
ORDER BY avgBuyPrice ASC;
""", conn)

print(complex_q)


conn.close()