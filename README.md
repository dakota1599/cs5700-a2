# Assignment 2

## Dakota Shapiro

### CS 5700 - Dr. Nada Lachtar

# Cipher, Plaintext, and Key

### Cipher

OhVTChwGUxEBFhIYUwcbGgBTEBoDGxYBBxYLB19TGgdTHhYSHQBTBxsSB1MKHAZTEgEWUxIRHxZTBxxTEQEWEhhTAAYRAAcaBwYHGhwdUxAaAxsWAQBTBgAaHRRTFQEWAgYWHRAKUxIdEh8KABoAXVMkFh8fUzccHRZS

### Plaintext

If you break this ciphertext, it means that you are able to break substitution ciphers using frequency analysis. Well Done!

### Key

`s` or `115`

# Execution Instructions

1. You will need the python interpreter to run this program. Go to [python.org](https://www.python.org/) to install python onto your machine.
2. In a terminal window, navigate to the directory of the `main.py` file included in this project.
3. Run the following command: `python3 main.py`
   - This will run the count function, the brute force function, and print out the deciphered text using the key.

# Method Used to Break the ciphertext

## Step 1

First I figured out how to decrypt the encryption algorithm. I did this basically by reversing the steps of the encryption algorithm.

I decoded the base64 encoded string and created a new bytearray the size of the decoded string.

```python
arr = base64.b64decode(c)
message = bytearray(len(arr))
```

Next I had to xor each character with the inputted key character, which was essentially the same task as in the encryption algorithm. A copy and paste basically, just without needing to run each index of the `m` variable through the `ord()` function to get each character's ascii value.

```python
for i in range(len(arr)):
    message[i] = arr[i] ^ ord(k)
```

Finally I decoded the bytearray into a `utf-8` string and returned it.

```python
return message.decode('utf-8')
```

The final decryption algorithm is this:

```python
def decrypt(c, k):
    arr = base64.b64decode(c)
    message = bytearray(len(arr))
    for i in range(len(arr)):
        message[i] = arr[i] ^ ord(k)
    return message.decode('utf-8')
```

## Step 2

I wrote a function for counting the occurance of each character in the decoded ciphertext and dumping those counts into a csv.

```python
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
```

```python
def toString(c):
    arr = base64.b64decode(c)
    return arr.decode('utf-8')
```

**`toString()` is used to decode the base64 string into a regular `utf-8` string.**

## Step 3

According to [Wikipedia](https://en.wikipedia.org/wiki/Letter_frequency), `e` is the most frequently used letter in the english language. I went down the list of frequency counts and xor'd each value with the ascii value of `e` (`101`), taking the returned value and running that value through the decryption algorithm with the ciphertext until a human readable text appeared.

It took two tries before I got the correct key value of `s`. The ascii value of `83` had the highest frequency of 19, however it was not `e`. After deciphering the value using `s`, I found `83` came out to `32` or the `SPACE` character. The next value with the highest frequency was `22` with a value of 12, which turned out to be `e` and produced the key value of `115` or `s`. Use the counts from the `count.csv` file and the `playground.py` file to test this out for yourself. Run `python3 playground.py` to execute.

# Extra - Brute Force

Seeing as the key was only one character, and the ascii code set only has 128 characters, it was pretty trivial to brute force this ciphertext. I wrote a brute force function that loops through all 128 ascii values and passes each value and the ciphertext into the decryption algorithm. All results were dumped into a file labelled with the ascii value used to decrypt. This method ultimately took less time because it involved less human intervention and trialing to get the plaintext.

```python
def brute_force(c):
    file = open("./brute-force-attempt.txt", "w")
    for i in range(128):
        a = ""
        a += (f"Attempt {i}:\n")
        a += (decrypt(c, chr(i)))
        a += ("\n")
        file.write(a)
    file.close()
```

You can view the brute force attempt in the file `brute-force-attempt.txt`.
