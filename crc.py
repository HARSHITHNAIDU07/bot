def xor(a, b):
    result = []
    for i in range(1, len(b)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result)

def mod2div(dividend, divisor):
    pick = len(divisor)
    tmp = dividend[0:pick]

    while pick < len(dividend):
        if tmp[0] == '1':
            tmp = xor(divisor, tmp) + dividend[pick]
        else:
            tmp = xor('0'*pick, tmp) + dividend[pick]
        pick += 1

    if tmp[0] == '1':
        tmp = xor(divisor, tmp)
    else:
        tmp = xor('0'*pick, tmp)

    checkword = tmp
    return checkword

def encodeData(data, key):
    l_key = len(key)
    appended_data = data + '0'*(l_key-1)
    print("Appended data is " + appended_data)
    remainder = mod2div(appended_data, key)
    print("Remainder is: " + remainder)
    codeword = data + remainder
    return codeword

def decodeData(data, key):
    l_key = len(key)
    appended_data = data + '0'*(l_key-1)
    remainder = mod2div(appended_data, key)
    return remainder

data = "1101"
key = "101"
print("Original Data: ", data)
encoded_data = encodeData(data, key)
print("Encoded Data: ", encoded_data)

received_data=str(int(input("Enter recieved data")))
print("Received Data: ", received_data)
remainder = decodeData(received_data, key)
print("Remainder after decoding: ", remainder)

if '1' in remainder:
    print("Error detected in received data")
else:
    print("No error detected in received data")
