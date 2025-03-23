import requests

def fetch_username_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()  # string --> json  #calling as a 'method'**
    
    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        picture = user_data["picture"]["thumbnail"]
        
        return username, picture
    else:
        raise Exception("Failed to fetch data")
    
def main():
    try:
        username, picture = fetch_username_freeapi()
        print(f"\n Username: {username} \n picture: {picture} \n")
    except Exception as e:
        print (str(e))
        
if __name__ == "__main__":
    main()