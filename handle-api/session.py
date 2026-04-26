import requests
import time


def get_data():

    url = "https://jsonplaceholder.typicode.com/posts"

    offset = 0
    limit = 10

    with requests.Session() as session:

        while True:

            params = {
                "_start": offset,
                "_limit": limit
            }

            response = session.get(url, params=params, timeout=5)

            response.raise_for_status()

            json_response = response.json()

            if not json_response:
                print("No more data")
                break

            counter = 1

            for data in json_response:
                print(
                    f"offset={offset} | {data.get('title')} - {counter}"
                )
                counter += 1

            time.sleep(2)  # simulate rate limit

            offset += limit
            
            
def main() :
    get_data()
    
    


if __name__ == "__main__" :
    main()
