from random import randint


def  isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime_generator():
    primeone = 12

    while not isprime(primeone):
        primeone = randint(11, 5000)
        print (primeone)

    primetwo = primeone
    primetwo += 1
    while not isprime(primetwo):
        primetwo += 1
    return primeone, primetwo


def gcd(x, y):
    """
        use to calculate the greatest common divisible of x and y """
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def caculatePhi(prime1, prime2):
    """
        calculate Phi(N) and return Phi(N)"""
    return (prime1 - 1) * (prime2 - 1)


def e_finder(e, phi):
    """
        calculate e for the public key and return Phi(n),e,n"""
    while True:
        if gcd(phi, e) == 1:   # check to see if phi(N) and e has any
                               #common factor except one(1)
            return e
        else:
            e += 2    # increment e by two if there is a gcd>1


def Extended_Euclidean_Algorithm(PHI, E):
    phi = PHI
    e = E
    A, X, previous_X, Y, previous_Y = phi, 0, 1, 1, 0
    while e != 0:

        temp = e
        quotient = int(phi / e)
        e = phi % e
        phi = temp

        temp = X
        phi = previous_X - quotient * X
        previous_X = temp

        temp = Y
        Y = previous_Y - quotient * Y
        previous_Y = temp

    return A + previous_Y


def generate_keys(E, D, N):
    e, d, n = E, D, N
    """Calcualte private key(d),generate keys and return these keys
        ie. public and private keys for encryption and decryption"""

    return {"public_key": {"e": e, "n": n}}, {"private_key": {"d": d, "n": n}}


def DecimalToChar(decimal):
    d = decimal % 256
    print((str(chr(d))))
    return str(chr(d))


def encrypt(m, e, n):
    """encrypt message and return that encrypted message """
    encryped_string = ""
    encrypt_lst = []
    for i in m:   # loop through message, getting
                 # charactor at a time for encryption
        m_char = int(ord(i))   # convert each charactor
                                    # to its decimal equivalent
        c = pow(m_char, e, n)   # equivalent to c=(m**e)%n
        encrypt_lst.append(c)   # add each encrypted charactor to a LIST
        encryped_string += str(c)
    return encrypt_lst, encryped_string


def decrypt(c, d, n):
    """decrypt message and return that decrypted message"""
    decrypt_string = ""
    for i in c:     # loop through LIST of encrypted
                    # values,for decryption index by index
        m = pow(i, d, n)   # equivalent to m=(i**d)%n
        decrypt_string += DecimalToChar(m)   # add each charactor to a string
    return decrypt_string

if __name__ == "__main__":
    """Main for excuting programme"""
    message = str(raw_input("Enter message to encrypt: "))

    prime_one, prime_two = prime_generator()
    n = prime_one * prime_two
    phi = caculatePhi(prime_one, prime_two)
    e = e_finder(3, phi)
    d = Extended_Euclidean_Algorithm(phi, e)
    keys = generate_keys(e, d, n)     # get generated keys
                                # (public and private) and store them in keys

    print (("keys are: ", keys))

    encrypted_message, encryped_string = encrypt(message, e, n)    # encrypt
                                                            # message from user
    print (("Encrypted string: " + str(encryped_string)))   # display
                                                    # string of encrypted input
    print (encrypted_message)
    decrypt_message = decrypt(encrypted_message, d, n)    # decrypt
                                                # message that was encrypted.
    print (("Our message decrypted is: " + str(decrypt_message)))
