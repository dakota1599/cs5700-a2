import base64

def encrypt(m, k):
    result = bytearray(len(m))
    for i in range (len(m)):
        result[i]= (ord(m[i]) ^ ord(k))
    return base64.b64encode(str(result).encode('utf-8'))


def decrypt(c, k):
    arr = base64.b64decode(c)
    message = bytearray(len(arr))
    for i in range(len(arr)):
        message[i] = arr[i] ^ ord(k)
    return message.decode('utf-8')

def toString(c):
    arr = base64.b64decode(c)
    return arr.decode('utf-8')

def count(m):
    decodedMessage = toString(m)
    count = {}
    for i in decodedMessage:
        if (i not in count):
            count[i] = 1
        else:
            count[i] += 1
    
    save = ''
    for i in count:
        save += f"{ord(i)},{count[i]}\n"

    file = open("./count.csv", "w")
    file.write(save)
    file.close()
    return count

def xor(c, s):
    arr = []
    for i in c:
        arr.append(chr(i ^ s))
    return ''.join(arr)

def brute_force(c):
    file = open("./brute-force-attempt.txt", "w")
    for i in range(128):
        a = ""
        a += (f"Attempt {i}:\n")
        a += (decrypt(c, chr(i)))
        a += ("\n")
        file.write(a)
    file.close()

if __name__ == '__main__':
    cipher = b"OhVTChwGUxEBFhIYUwcbGgBTEBoDGxYBBxYLB19TGgdTHhYSHQBTBxsSB1MKHAZTEgEWUxIRHxZTBxxTEQEWEhhTAAYRAAcaBwYHGhwdUxAaAxsWAQBTBgAaHRRTFQEWAgYWHRAKUxIdEh8KABoAXVMkFh8fUzccHRZS"
    count(cipher)
    brute_force(cipher)
    print(decrypt(cipher, 's'))