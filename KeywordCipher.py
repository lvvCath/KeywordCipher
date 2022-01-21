lsymbols = """`~!@#$%^&*()-_=+"""
rsymbols = """{}[]|\\;:'",<.>/?"""
special_symbols = lsymbols + rsymbols
numbers = "1234567890"
valid_symbols = "abcdefghijklmnopqrstuvwxyz " + numbers + special_symbols

#scans and validates character of the inputted string
#only those symbols that are matched inside the global variable will be replaced
#unmatched symbols will be ignored and removed
def check(paragraph):

    validated_text = ""

    for char in paragraph: 
        if char in valid_symbols:
            validated_text += char
    return validated_text

def switch(variation, password, keyletter):
    dict={
        1: Original(password),
        2: Reverse1(password),
        3: Keyword_Atbash(password),
        4: Keyletter(password, keyletter)
    }    
    return  dict.get(variation, 'Invalid Operation') 

# KEYWORD ======================================
def Original(password):

    keyword = ""

    for char in password:
        if char in valid_symbols:
            if char not in keyword:
                keyword += char

    for char in valid_symbols:
        if char not in keyword:
            keyword += char

    return keyword

# KEYWORD-Reverse ======================================
def Reverse1(password):

    keyword = ""
    password = password
    reverseString = "".join(reversed(password))

    for char in reverseString:
        if char in valid_symbols:
            if char not in keyword:
                keyword += char

    for char in valid_symbols:
        if char not in keyword:
            keyword += char

    return keyword

# KEYWORD-Atbash ======================================
def Keyword_Atbash(password):
    origKey = ""
    keyword = ""

    for char in password:
        if char in valid_symbols:
            if char not in origKey:
                origKey += char

    for char in valid_symbols:
        if char not in origKey:
            origKey += char

    keyword = "".join(reversed(origKey))
    
    return keyword

# KEYWORD-Keyletter ======================================
def Keyletter(password, keyletter):
    position = valid_symbols.find(keyletter)
    
    keyword = Original(password)
    result = keyword[-position:] + keyword[:-position] 
    return result


# ENCRYPTION =================================================================================
def encrypt(validated_text, keyword):
    cipher_text = ""
    index_values = [valid_symbols.index(char) for char in validated_text]
    cipher_text ="".join(keyword[indexKeyword] for indexKeyword in index_values)
    
    return cipher_text
# DECRYPTION =================================================================================
def decrypt(cipher_text, keyword):
    deciphered_text = ""
    index_values = [keyword.index(char) for char in cipher_text]
    deciphered_text = "".join(valid_symbols[indexKeyword] for indexKeyword in index_values)

    return deciphered_text