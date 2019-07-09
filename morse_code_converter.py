""" [Easy] – Morse Code Converter (1-2 points)

Write a function that converts a given string between English and Morse Code, the direction being determined by a Boolean argument (false for Eng->Morse, true for Morse->Eng).

Let “-“ (minus) represent a dash, and let “.” (period) represent a dot. Letters should be separated by one space, and words should be separated by a forward slash “/”.

Test Cases:
morseCode("ABC", false) -> ".- -... -.-."
morseCode(".- -... -.-.", true) -> "ABC"
morseCode("ABC XYZ", false) -> ".- -... -.-. / -..- -.-- --.."
morseCode(".- -... -.-. / -..- -.-- --..", true) -> "ABC XYZ"
morseCode("", false) -> ""
morseCode("Hello. World!", false) -> ".... . .-.. .-.. --- .-.-.- / .-- --- .-. .-.. -.. -.-.--"
morseCode(".... . .-.. .-.. --- .-.-.- / .-- --- .-. .-.. -.. -.-.--", true) -> "HELLO. WORLD!" """

morse_eng_dictionary = {    'A':'.-', 
                            'B':'-...', 
                            'C':'-.-.', 
                            'D':'-..', 
                            'E':'.', 
                            'F':'..-.', 
                            'G':'--.', 
                            'H':'....', 
                            'I':'..', 
                            'J':'.---', 
                            'K':'-.-', 
                            'L':'.-..', 
                            'M':'--', 
                            'N':'-.', 
                            'O':'---', 
                            'P':'.--.', 
                            'Q':'--.-', 
                            'R':'.-.', 
                            'S':'...', 
                            'T':'-', 
                            'U':'..-', 
                            'V':'...-', 
                            'W':'.--', 
                            'X':'-..-', 
                            'Y':'-.--', 
                            'Z':'--..', 
                            ',':'--..--', 
                            '.':'.-.-.-', 
                            '?':'..--..', 
                            '/':'-..-.', 
                            '-':'-....-', 
                            '(':'-.--.', 
                            ')':'-.--.-', 
                            '!':'-.-.--',
                            ' ': '/',
                            '':''} 


def morseCode(msg, trans):
    # (false for Eng->Morse, true for Morse->Eng).

    msg = msg.upper()
    #if eng->morse
    if msg == '':
        msg = ''
    elif trans == False:
        msg = buildMorseMsg(msg)
    else:
        msg = buildEnglishMsg(msg)

    print(msg)
        
def buildEnglishMsg(morse_msg):
    eng_msg = ''
    parsed_morse_msg = morse_msg.split()

    for code in parsed_morse_msg:
        for key,value in morse_eng_dictionary.items():
            if value == code:
                eng_msg = eng_msg + key

    return eng_msg

def buildMorseMsg(eng_msg):
    morse_msg = ''
    for c in eng_msg:
        morse_msg = morse_msg + morse_eng_dictionary.get(c) + ' '

    return morse_msg


if __name__ == '__main__':
    morseCode("ABC", False) # -> ".- -... -.-."
    morseCode(".- -... -.-.", True) # -> "ABC"
    morseCode("ABC XYZ", False) # -> ".- -... -.-. / -..- -.-- --.."
    morseCode(".- -... -.-. / -..- -.-- --..", True) # -> "ABC XYZ"
    morseCode("", False) # -> ""
    morseCode("Hello. World!", False) # -> ".... . .-.. .-.. --- .-.-.- / .-- --- .-. .-.. -.. -.-.--"
    morseCode(".... . .-.. .-.. --- .-.-.- / .-- --- .-. .-.. -.. -.-.--", True) # -> "HELLO. WORLD!"