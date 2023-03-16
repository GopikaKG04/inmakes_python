def student_discount(price):
    price = price - (price * 10) / 100
    return price
def regular_discount(price):
    price = price - (price * 5) / 100
    return price
original_price = int(input("enter your number"))
print(regular_discount(student_discount(original_price)))
