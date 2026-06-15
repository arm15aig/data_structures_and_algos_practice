def is_colorful(number):
    num_str = str(number)
    length = len(num_str)
    product_set = set()

    for i in range(length):
        product = 1
        for j in range(i, length):
            product *= int(num_str[j])
            if product in product_set:
                return False
            product_set.add(product)
    
    return True

# Testing the function
print("326 Colorful -", is_colorful(326))
print("3245 Colorful -", is_colorful(3245))
print("32458 Colorful -", is_colorful(32458))