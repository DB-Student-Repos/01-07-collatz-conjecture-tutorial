def steps(number):
    steps = 0
    if(number==1):
        return 0
    if(number < 1):
        raise ValueError("Only positive numbers are allowed")
    while(number>1):
        if((number % 2) == 0):
            number = (number/2)
        else:
            number = (3 * number) + 1
        steps = steps + 1
    return steps
    
