n=input('Enter your FizzBuzz Value', )


def fizz_buzz(n):
    '''
    enter the number you want to play fizz buzz with, default 15
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
    
    
fizz_buzz(n)
