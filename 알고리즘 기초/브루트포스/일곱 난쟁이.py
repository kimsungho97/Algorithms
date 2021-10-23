arr = []
for _ in range(9):
    arr.append(int(input()))

arr.sort()

result = []


def bruteforce(arr, last, count, total, record):
    global result
    if(total == 100 and count == 7):
        result = record[:]
        return

    if(count >= 7 or total > 100):
        return
    for i in range(last, len(arr)):
        record.append(str(arr[i]))
        bruteforce(arr, i+1, count+1, total+arr[i], record)
        record.pop()


bruteforce(arr, 0, 0, 0, [])
print('\n'.join(result))
