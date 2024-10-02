import urllib.request as urllib

def main():
    print("Checking connection...")
    url = input("Enter url: ")
    response =  urllib.urlopen(url)
    print(f"Connected to {url} successfully")
    print("Response code is: ", response.getcode())

main()