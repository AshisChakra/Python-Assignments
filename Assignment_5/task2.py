def print_list():
    numbers = []
    extracted_numbers = []
    for i in range(1,11):
        numbers.append(i)
    extracted_numbers = numbers[:5]
    print("Original List :",numbers) 
    print("Extracted first five elements :", extracted_numbers)
    print("Reversed extracted elements :", extracted_numbers[::-1])

print_list()
