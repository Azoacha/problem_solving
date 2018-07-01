## Level 2

def decode(text):
    """
    Original solution.
    Args:
        text (str): the text to decode
    Returns:
        str: the original text with every letter shifted to the second
        next letter in the alphabet.
    """
    txt = ''
    for char in text:
        if not char.isalpha():
            txt += char
            continue
        encod = ord(char)
        if char in ['y', 'z']:
            encod -= 26
        txt += chr(encod + 2)
    return txt

if __name__ == '__main__':
    og_txt = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq " \
             + "ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw " \
             + "rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq " \
             + "pcamkkclbcb. lmu ynnjw ml rfc spj."
    # to get instructions for next url
    print(decode(og_txt))
    # next url
    print(decode("map"))