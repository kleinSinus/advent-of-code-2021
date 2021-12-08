# takes a desimal number, returns it in base x,
# number in base x is returned as a list where each entry is a digit
def int2base(num, base):
    result = []
    value = num
    if value == 0:
        return [0]
    while value > 0:
        result.insert(0, value%base)
        value = value // base
    return result

# takes a number in base x, returns its decimal value,
# number in base x is given as a list where each entry is a digit
def base2int(num, base):
    result = 0
    for i in range(len(num)):
        result = result * base + num[i]
    return result

# convert number from base x to base y
# number is represented as list of ints
def baseX2baseY(num, x, y):
    return int2base(base2int(num, x), y)

# generates alphabetical labels from integers
def int2label(i):
    label = ''
    base26_number = int2base(i, 26)
    for j in range(len(base26_number)):
        label += (chr(ord('@')+base26_number[j]))
    label = label[:-1] + (chr(ord(label[-1])+1))
    return label

# takes a bitstring, returns a binary number as a list of bits
def bits2bin(bits):
    bin = [0]*len(bits)
    for i in range(len(bits)):
        bin[i] = int(bits[i])
    return bin

# takes a binary number, returns a bitstring
def bin2bits(bin):
    bits = ""
    for bit in bin:
        bits += str(bit)
    return bits

# takes a string of comma-separated integers,
# returns a list of integers
def csv2intlist(csv):
    temp = csv.split(',')
    result = [0] * len(temp)
    for i in range(len(temp)):
        result[i] = int(temp[i])
    return result
