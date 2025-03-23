import requests

def fetch_prodct():
    url = "https://api.freeapi.app/api/v1/public/randomproducts/product/random"
    response = requests.get(url)
    data = response.json() # string --> json
    
    if data["success"] and "data" in data:
        product_data = data['data']
        title = product_data["title"]
        price = product_data["price"]
        image = product_data["images"][1]
        
        return title, price, image
    
    else:
        raise Exception("Failed to Fetch Data from this API.....\nCheck Again.")
    
def main():
    try:
        title, price, image = fetch_prodct()
        print(f"\nProdct Title: {title}\nProduct Price: {price}\nProduct Image: {image}")
    
    except Exception as e:
        print(str(e))
        
if __name__ == "__main__":
    main()