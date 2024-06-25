# befintliga varor i warehouse
warehouse = {
    "köttfärs": 5,
    "grädde": 8,
    "krossade tomater": 5,
    "gul lök": 100
}

print(warehouse["krossade tomater"])
# prints: 5



from operator import itemgetter

# Nya varor levererat till warehouse
warehouse["krossade tomater"] = 58
warehouse["röd lök"] = 7

print(warehouse)
# prints: {'köttfärs': 5, 'grädde': 8, 'krossade tomater': 58, 'gul lök': 100, 'röd lök': 7}



# skriv ut varje item med key - value 
for k, v in warehouse.items():
    print(k,':',v, 'st.')

# Prints:
# köttfärs : 5 st.
# grädde : 8 st.
# krossade tomater : 58 st.
# gul lök : 100 st.
# röd lök : 7 st.


# sortering på key 
for k, v in warehouse.items():
    print(k, ':',warehouse[k], 'st.')

# Prints:
# köttfärs : 5 st.
# grädde : 8 st.
# krossade tomater : 58 st.
# gul lök : 100 st.
# röd lök : 7 st.


dict_as_list = [('köttfärs', 5), ('grädde', 8), ('krossade tomater', 58), ('gul lök', 100), ('röd lök', 7)]

getter_func = itemgetter(1)
print('dict as list: ',getter_func(dict_as_list[0])) # prints: dict as list: 5
print('dict as list: ',getter_func(dict_as_list)) # dict as list:  ('grädde', 8)

sorted_warehouse = sorted(warehouse.items(), key=itemgetter(1), reverse=True)
print(sorted_warehouse)
# prints: [('gul lök', 100), ('krossade tomater', 58), ('grädde', 8), ('röd lök', 7), ('köttfärs', 5)]

print(warehouse.values())
# prints: dict_values([5, 8, 58, 100, 7])



warehouse_deluxe = {
    "köttfärs" : { "stock" : 20, "price" : 50, "ids" : (1234, "K14") },
    "grädde" : { "stock" : 80, "price" : 20, "ids" : (3141, "L12") },
    "krossade tomater": { "stock" : 33, "price" : 10, "ids" : (4224, "E13") },
    "gul lök" : { "stock" : 42, "price" : 5, "ids" : (2742, "D02") }
}

for k in sorted(warehouse_deluxe.keys()):
    print(k,':',warehouse_deluxe[k]["price"])

# Prints:
# grädde : 20
# gul lök : 5
# krossade tomater : 10
# köttfärs : 50

warehouse_deluxe["röd lök"] = {}
warehouse_deluxe["röd lök"]["stock"] = 7
warehouse_deluxe["röd lök"]["price"] = 9
warehouse_deluxe["röd lök"]["ids"] = (6314, "D04")



for key in sorted(warehouse_deluxe.keys()):
    item = warehouse_deluxe[key]
    print("{product} costs {price} and we have {stock} in stock. It has barcode {barcode} and stock id {stock_id}.".format(
        product=key,
        price=item["price"],
        stock=item["stock"],
        barcode=item["ids"][0],
        stock_id=item["ids"][1]
    ))



for i, v in enumerate(["ko", "apa","häst"]):
    print(i,v)
# Prints: 
# 0 ko
# 1 apa
# 2 häst


for i, d in warehouse_deluxe.items():
    print(i,d)
# Prints:
# köttfärs {'stock': 20, 'price': 50, 'ids': (1234, 'K14')}
# grädde {'stock': 80, 'price': 20, 'ids': (3141, 'L12')}
# krossade tomater {'stock': 33, 'price': 10, 'ids': (4224, 'E13')}
# gul lök {'stock': 42, 'price': 5, 'ids': (2742, 'D02')}
# röd lök {'stock': 7, 'price': 9, 'ids': (6314, 'D04')}



search_for = "E13"
for item, data in warehouse_deluxe.items():
    if data["ids"][1] == search_for:
        print(item)
# prints:
# krossade tomater