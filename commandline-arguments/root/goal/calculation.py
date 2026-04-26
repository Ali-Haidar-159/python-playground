from root.service.validation import validate_numbers


def add(x:int , y:int) -> int :
    isValid = validate_numbers(x,y)
    
    if isValid :
        return x+y 
    else :
        raise Exception("Invalid Number")