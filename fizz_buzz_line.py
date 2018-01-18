


def fizz_buzz(n):
    '''
    enter the number you want to play fizz buzz with
    '''
    
    for value in range (1,n+1):
        if value%3==0 and value%5==0:
            print('FizzBuzz')
        elif value%3==0:
            print('Fizz')
        elif value%5==0:
            print('Buzz')
        else:
            print(value)
    
while True:
    n=input('Enter your FizzBuzz Value:  ', )
    try:
        n=int(n)
        fizz_buzz(n)
        break
    
    except ValueError:
        print('INVALID ENTRY: please use a numeric entry.')
        print('')
        continue

