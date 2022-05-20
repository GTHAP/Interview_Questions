# Count and return the number of ON bits in a given integer

def bitCounting(num):
    temp_list = []
    binary_list = []
    if num % 2 == 0:
        on_bits = 0
    if num % 2 != 0:
        on_bits = 1
    while num > 0:
        num = num // 2
        temp_list.append(num)
    for i in temp_list:
        binary = i % 2
        binary_list.append(binary)
    for i in binary_list:
        if i == 1:
            on_bits += 1
    return on_bits
  
num = 1234
bitCounting(num)
