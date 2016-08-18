# Ctrl + Shift + B : Build and Run this Python in VSCode

print 'hello world'
d = {}
d.setdefault('a', {}).setdefault('b', []).append(1)

print d

taxes = 100
if taxes > 100:
    print 'too much tax'
elif taxes == 100:
    print 'on the border'
else:
    print 'safe'

discount = 25 if taxes > 100 else 0

print taxes, discount

# Example of for loop
from datetime import date, timedelta #  importing date timedelta module

today = date.today()
tomorrow = today + timedelta(days = 1) #tomorrow = taday + 1
products = [
    {'sku': '1', 'exp_date': today, 'price' : 100.0},
    {'sku': '2', 'exp_date': tomorrow, 'price' : 50.0},
    {'sku': '3', 'exp_date': today, 'price' : 20.0}
]

for product in products:
    if product['exp_date'] != today:
        continue
    product['price'] *= 0.8
    print 'Price for sku', product['sku'], 'is now', product['price'] # Printing with multiple variales