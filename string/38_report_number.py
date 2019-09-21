def countAndSay(n: int) -> str:
    if n == 1:
        return str(n)

    number_array = "1"
    for i in range(1, n):
        count = 1
        temp = ""
        for j in range(1, len(number_array)):
            if number_array[j] == number_array[j-1]:
                count += 1
            else: 
                temp += str(count) + number_array[j-1]
                count = 1
        temp += str(count) + number_array[-1]
        number_array = temp
countAndSay(5)
