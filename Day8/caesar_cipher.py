def encrypt(text, shift):
    shift=int(shift)
    shifted_string=''
    for each in text :
        if each.isalpha():
            each=each.lower()
            if (ord(each)+shift) < ord('z'):
                new_char=chr(ord(each)+shift)
            else :
                diff=shift-(ord('z')-ord(each))
                new_char=chr(ord('a')+diff-1)
        else :
            new_char=each
        shifted_string+=new_char
    return shifted_string

#e=encrypt(text, shift)
#print(e)

def decrypt(text, shift):
    shift=int(shift)
    shifted_string=''
    for each in text :
        if each.isalpha():
            each=each.lower()
            if (ord(each)-shift) > ord('a'):
                new_char=chr(ord(each)-shift)
            else :
                diff=shift-(ord(each)-ord('a'))
                new_char=chr(ord('z')-diff+1)
        else :
            new_char=each
        shifted_string+=new_char
    return shifted_string

text=input("Enter the text to be encoded")
shift=input("Enter the shift value")


e=encrypt(text, shift)
print("Encrypted text is ",e)
d=decrypt(e, shift)
print("Decrypted text is ", d)
