import argparse

from root.goal.calculation import add
from root.goal.display import magic

parser = argparse.ArgumentParser()

parser.add_argument(
    "--goal" , "-g" ,
    type=str , default="calculation" ,
    metavar="goal"
)
parser.add_argument(
    "--data1" , "-d1" ,
    type=str , default="10" ,
    metavar="data 1"
)
parser.add_argument(
    "--data2" , "-d2" ,
    type=str , default="20" ,
    metavar="data 2"
)

args = parser.parse_args()
goal:str = args.goal


try : 
    match goal :
        case "calculation" : 
            num1 = int(args.data1)
            num2 = int(args.data2)
            
            result = add(num1,num2)        
            print("Your final result is : ",result)
            
        case _:
            result = magic(args.data1 , args.data2)
            print(result)
        
except Exception as e :
    print(e)