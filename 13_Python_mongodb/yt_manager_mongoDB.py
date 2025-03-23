from pymongo import MongoClient
from bson import ObjectId

client = MongoClient("mongodb+srv://ytpy:ytpy@cluster03.itxwp.mongodb.net/?retryWrites=true&w=majority", tls=True, tlsAllowInvalidCertificates=True)
# Not a good practice to use id and password
#tlsAllowInvalidCertificates = True) - Not a good thing to do

try:
    client.admin.command('ping')
    print("Connected successfully")
except Exception as e:
    print(f"Connection failed: {e}")

print(client)

db = client["yt_manager"]
video_collection = db["videos"]

def list_videos():
    for video in video_collection.find(): # video_collection.find() will iterate
        print(video)

def add_video(name, time):
    video_collection.insert_one({'name': name, 'time': time})

def update_video(video_id, new_name, new_time):
    video_collection.update_one(
        {"_id": ObjectId(video_id)},
        {"$set": {"name": new_name, "time": new_time} }
    )

def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)}) # ObjectId coverts string into bson

def main():
    while True:
        print("\n \t Youtube Manager")
        print("-"*80)
        
        print("1. List all Videos")
        print("2. Add a Video")
        print("3. Update Video")
        print("4. Delete a Video")
        print("5. Exit")
        choice = input("Enter you choice: ")
        
        if choice == '1':
            list_videos()
            
        elif choice == '2':
            name = input("Enter the name: ")
            time = input("Enter the duration: ")
            add_video(name, time)
        
        elif choice == '3':
            video_id = input("Enter the video id to be updated: ")
            name = input("Enter the updated name: ")
            time = input("Enter the updated duration: ")
            update_video(video_id, name, time)
            
        elif choice == '4':
            video_id = input("Enter the video id to be updated: ")
            delete_video(video_id)
            
        elif choice == '5':
            break
        
        else:
            print("Invalid Choice...Choose again")
            
            
if __name__ == "__main__":
    main()