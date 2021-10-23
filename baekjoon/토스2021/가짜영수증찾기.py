def solution(amountText):
    if (amountText == '0'):
        return True
    if (amountText == ''):
        return False
    if (amountText[0] == ','):
        return False
    if (amountText[-1] == ','):
        return False
    
    arr = amountText.split(",")

    if (amountText[0] == '0'):
        return False

    if len(arr)!=1:
        for i in range(len(arr)):
            if (arr[i] == '' or (len(arr[i]) != 3 and i != 0)):
                return False

        for i in range(len(arr)):
            for c in arr[i]:
                if (c.isdigit() == False):
                    return False
        return True
    else:
        return amountText.isdigit()