
numbers = [1,2,3,4,5]
marks = [55,60,67,78,88]

# maps

def square(x:int)-> int :
    return x*x 


result1 = list(map(square,numbers))
print("The result of suqare : ",result1)

result2 = list(map(lambda x:x*x , marks))
print("The result of square2 : ",result2)


#filters : 

def is_pass(mark) :
    return mark>=60

passed_marks = list(filter(is_pass,marks))
print("All the passed marks : ",passed_marks)

failed_marks = list(filter(lambda mark:mark<60,marks))
print("All the failed marks : ",failed_marks)


