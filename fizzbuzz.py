def fizzbuzz(input):
    if (input%3==0) and (input%5==0):
        return 'fizzbuzz'
    
    if input % 3 == 0:
        return 'fizz'

    if input % 5 == 0:
        return 'buzz'

    return input
for i in range(1,16):

    print(fizzbuzz(i))