import requests
import pandas as pd

def fetch_data(url):
    response = requests.get(url)
    return response.json()

def main():
    url = 'https://jsonplaceholder.typicode.com/posts'
    data = fetch_data(url)
    df = pd.DataFrame(data)
    
    print("Ersten 5 Zeilen des DataFrame:")
    print(df.head())

if __name__ == "__main__":
    main()