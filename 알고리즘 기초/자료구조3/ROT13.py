line = input()

result = []
for c in line:
    if(c.isalpha()):
        new_c = ord(c)+13
        if(ord(c) > ord('Z')):
            if(new_c > ord('z')):
                result.append(chr(new_c-(26)))
            else:
                result.append(chr(new_c))
        else:
            if(new_c > ord('Z')):
                result.append(chr(new_c-(26)))
            else:
                result.append(chr(new_c))
    else:
        result.append(c)

print(''.join(result))
