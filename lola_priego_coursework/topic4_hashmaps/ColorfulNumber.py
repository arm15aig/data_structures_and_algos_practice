#This was previously a CareerCup problem. 
# Details can be found here: https://www.careercup.com/question?id=5710911741559040

def is_colorful(num):
    length = len(str(num))
    products = set()
    num_str = str(num)
    for i in range(length):
        product = 1
        for j in range(i, length):
            product *= int(num_str[j])
            if product in products:
                return 'Not Colorful'
            products.add(product)
    return 'Colorful'

num = 3245  
print(is_colorful(num))
