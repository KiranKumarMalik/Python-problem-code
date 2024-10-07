# Write a Python program to filter the prices of the stocks with price greater than 200.

prices={("ACME",45.23),("AAPL",612.78),('IBM',205.5),("HPQ",37.20),("FB",10.75)}
result_price={}
for item in prices:
    if item[1]>200: # item[1] is the price of the stock
     result_price[item[0]]=item[1] # item[0] is the name of the stock and item[1] is the price of the stock
print(result_price)