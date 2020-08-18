import codecs

def hexdecoder(hex):
    return codecs.encode(codecs.decode(hex, "hex"), "base64").decode()

if __name__ == '__main__':
    n = input("hex:")
    print(hexdecoder(n))