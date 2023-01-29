import httpx
from pprint import pprint

url = "https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/denni_kurz.txt"
res = httpx.get(url)
rows = res.text.split("\n")
rows = rows[2:-1]
data = {}

for r in rows:
    cols = r.split("|")
    amount = int(cols[-3])
    curr = cols[-2]
    
    rate = cols[-1]
    rate = rate.replace(",", ".")
    rate = float(rate)

    x = [rate,float(cols[-3])]
    data[curr] = x

pprint(data)

user_choice = input("Zadejte kód cílové měny: ")

if user_choice == "CZK":
    user_curr = input("Zadejte kód vaší měny: ")
    user_amount = input("Zadejte částku v {user_curr}: ")
    user_amount = float(user_amount)
    x = data[user_curr]

    result = (user_amount * x[0])/x[1]
    result = round(result, 2) 
else:
    user_amount = input("Zadejte částku v CZK: ")
    user_amount = float(user_amount)
    x = data[user_choice]

    result = (user_amount / x[0])*x[1]
    result = round(result, 2)

print(f"Vysledna castka je {result} {user_choice}")
