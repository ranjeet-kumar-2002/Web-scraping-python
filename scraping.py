# import pandas as pd
# import requests
# from bs4 import BeautifulSoup

# for i in range(2,10):
#     url = "https://www.flipkart.com/search?q=mobile+under+50000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_18_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_18_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobile+under+50000%7CMobiles&requestId=04f1fb97-46e0-4c62-ab85-faac9c3a524a&as-searchtext=mobile+under+50000&page="+str(i)

#     r = requests.get(url)

#     soup = BeautifulSoup(r.text, "lxml")

#     np = soup.find("a", class_ = "_1LKTO3").get("href") 
#     cnp = "https://www.flipkart.com"+np
#     print(cnp)


import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Description = []
Reviews = []
for i in range(2,12):
    url = "https://www.flipkart.com/search?q=mobile+under+50000&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_18_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_18_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobile+under+50000%7CMobiles&requestId=04f1fb97-46e0-4c62-ab85-faac9c3a524a&as-searchtext=mobile+under+50000&page="+str(i)

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_="_1YokD2 _3Mn1Gg")

# for product names
    names = box.find_all("div", class_="_4rR01T")
    for i in names:
        name = i.text
        Product_name.append(name)
# print(len(Product_name))    

# for prices
    prices = box.find_all("div", class_="_30jeq3 _1_WHN1")
    for i in prices:
        name = i.text
        Prices.append(name)
# print(len(Prices))

# desc
    desc = box.find_all("ul", class_="_1xgFaf")
    for i in desc:
        name = i.text
        Description.append(name)
# print(len(Description))

# reviews
    review = box.find_all("div", class_="_3LWZlK")
    for i in review:
        review_text = i.text
        Reviews.append(review_text)
# print(len(Reviews))

#Adjust the lengths of the arrays
    max_length = max(len(Product_name), len(Prices), len(Description), len(Reviews))
    Product_name += ["N/A"] * (max_length - len(Product_name))
    Prices += ["N/A"] * (max_length - len(Prices))
    Description += ["N/A"] * (max_length - len(Description))
    Reviews += ["N/A"] * (max_length - len(Reviews))


#data frame 
df = pd.DataFrame({
    "Product Name": Product_name,
    "Prices": Prices,
    "Description": Description,
    "Reviews": Reviews
})

# print(df)

df.to_csv("D:/dsa c++ college wallah/python project/webscraping/flipkart_mobile_under_50000.csv")
