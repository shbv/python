"""
Character encodings:
    Way of translating characters (an abstraction) to integers (unicode code point) to bits/bytes (files contain bytes, not strings)
        E.g. 
        - ASCII encoding scheme has 128 characters (a-z, 0-9, etc.) & code points (0 to 127 in base 10):  
            - each character requires at most 1 byte of space (7 bits to be exact)
        - Unicode has 1,114,111 characters & code points
            - encoded using UTF-8/16/32 encoding formats into binary data
            - each character may require more than 1 byte of space (1 - 4 bytes for UTF-8)
            - UTF-8 is variable length encoding (i.e. 1 to 4 bytes for each character)
    All Python 3 source code & text is Unicode by default

Numbering systems:
    Binary (base 2):        0b0 0b1 0b10  ...
    Octal (base 8):         0o1 .. 0o7 0o10 ...   
    Decimal (base 10),      0 1 .. 9 10 ...
    Hexadecimal (base 16)   0x0 .. 0x9 0xa .. 0xf 0x10 ...
    
References: 
    https://realpython.com/python-encodings-guide/
"""

"""
Character encoding utils:
"""
#ord(a): Single Unicode character -> Unicode code point (integer from 0 to 1,114,111)
print("=== ord() ===")
print(ord('b')) # 98
print(f"{ord('b'):08b}")  #01100010
print(ord('1')) # 49
print()
#chr(n): unicode code point (integer from 0 to 1,114,111) -> single unicode character
print("=== chr() ===")
print(chr(49))  # 1
print(chr(98))  # b
print()

"""
Numbering system
"""
print("=== numbering system using int & base ===")
print(int('11'))            # => base 10 => 11
print(int('11', base=10))   # => 11
print(int('11', base=2))    # => 3
print(int('11', base=8))    # => 9
print(int('11', base=16))   # => 17
print()
print("=== numbering system using literal forms ===")
print(11)      # => base 10 => 11
print(0b11)    # => base 2 => 3
print(0o11)    # => base 8 => 9
print(0x11)    # => base 16 => 17
print()
print("=== numbering system utils ===")
print(f"ascii('jalepeño'):  {ascii('jalepeño')}") #'jalepe\xf1o'
print(f"bin(10):  {bin(10)}") # 0b1010
print(f"hex(10):  {hex(10)}") # 0xa
print(f"bytes from iterable of ints: {bytes((104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100))}") # b'hello world'
print(f"bytes(3): {bytes(3)}") #b'\x00\x00\x00'
print()
print("=== byte immutable object & bytearray to edit it ===")
by = b'abcd\x65'    # each byte in it could be ASCII character or encoded hex (0-255 since 8 bits in byte)
barr = bytearray(by)  
print (barr)        #bytearray(b'abcde')
print (len(barr))   #5
barr[0] = 102         
print (barr)        #bytearray(b'fbcde')
print()

"""
Encoding & Decoding 
    <str>.encode()   => FROM unicode character string TO byte object/string (allows ascii characters as is)
    <bytes>.decode() => FROM byte object/string TO unicode character string 
    All I/O happens in bytes (not str/text)
"""

print("=== number of bytes in encoding ===")
n = 100
ascii_enc = chr(n).encode("ascii") # bytes rep
ascii_len = len(ascii_enc)
print(f"ascii_len of {n}: {ascii_len} bytes")  # 1 byte
print()

print("=== string to byte to string ===")
txt = "résumé"
by = txt.encode("utf-8")
st = by.decode("utf-8")
print(f"txt: {txt}, by: {by} (number of bytes: {len(by)}), st: {st}")
# txt: résumé, by: b'r\xc3\xa9sum\xc3\xa9' (number of bytes: 8), st: résumé
#           é needs 2 bytes \xc3\xa9 => 0xc3, 0xa9 in hex
print()

print("=== byte in latin-1 encoding (default for http) to string ===")
by = b"\xbc cup of flour"  # byte string
st = by.decode("latin-1")
print(f"by: {by}, st: {st}")
# by: b'\xbc cup of flour', st: ¼ cup of flour
print()

print("=== get unicode literal using 'unicode-escape' encoding ===")
alef_hamza = chr(1571)
alef_hamza_unicode = alef_hamza.encode('unicode-escape')
print(f"alef_hamza: {alef_hamza}, unicode: {alef_hamza_unicode}")
# alef_hamza: أ, unicode: b'\\u0623'
print()

print("=== unicodedata ===")
import unicodedata
print(unicodedata.name("a"))
#'LATIN SMALL LETTER A'
print(unicodedata.lookup("LATIN SMALL LETTER A"))
#'a'

