n=input('Enter your FizzBuzz value ', )


def fizz_buzz(n):
    '''
    enter the number you want to play fizz buzz with
    '''
    lst=[]
    for value in range (1,n):
        if value%3==0 and value%5==0:
            lst.append('FizzBuzz')
        elif value%3==0:
            lst.append('Fizz')
        elif value%5==0:
            lst.append('Buzz')
        else:
            lst.append(value)
    print (lst)
    
fizz_buzz(n)