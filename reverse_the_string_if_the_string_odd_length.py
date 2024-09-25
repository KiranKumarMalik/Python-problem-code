name=["Apple", "google", "yahoo", "facebook", "flipkart", "chrome", "gmail", "instagram", "microsoft", "qtalk", "Zomato"]
result=[]
for i in name:
    if len(i) % 2 != 0:
     result.append(i[::-1])
    else:
       result.append(i)
print(result)