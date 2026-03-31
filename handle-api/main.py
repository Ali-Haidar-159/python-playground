import requests

def getData () : 
    url = "https://jsonplaceholder.typicode.com/posts"
    
    response = requests.get(url)
    data = response.json()
    
    return data 


def main() : 
    try : 
        data = getData()
        
        for v in data :
            print(v['title'])
        
    except Exception as e:
        print (e)


if __name__ == "__main__" : 
    main()
