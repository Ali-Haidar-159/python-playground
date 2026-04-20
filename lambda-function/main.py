
# def add(x,y):
#     return x+y 


add = lambda x,y : x+y  # lambda parameter : expression 
r = (lambda x,y : x-y)(10,3)  # lambda parameter : expression 
 

def main() :
    res = add(45,5)
    print("The result  is : ",res)
    print("The result  is : ",r)
    print("The result  is : ",(lambda x,y : x*y)(10,3))
    

if __name__ == "__main__" :
    main()