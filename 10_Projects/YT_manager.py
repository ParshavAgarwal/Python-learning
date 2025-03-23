import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            test = json.load(file)
            # print ("test name ->", test) 
            # print("type is ",type(test))
            return test
    except FileNotFoundError:
        return []


def save_data_hepler(videos):
    with open('youtube.txt','w') as file:
        return json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("-" * 70)
    print("\n")
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")  ## with '', humko dictionary access mil gaya
    print("\n")
    print("-" * 70)

def add_video(videos):
    name = input("Enter the Video's Name: ")
    time = input("Enter the Duration: ")
    videos.append({'name': name, 'time': time})
    save_data_hepler(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Choose the video number you want to update: "))
    
    if 1<= index <= len(videos):
        name = input("Enter new name: ")
        time = input("Enter new time: ")
        videos[index-1] = {'name':name, 'time': time}
        save_data_hepler(videos)
        videos = load_data()
    
    else:
        print("Enter Correct Video Number..")


def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the Video Number you want to delete: "))
    
    if 1<= index <= len(videos):
        del(videos[index - 1])
        save_data_hepler(videos)
        
    else:
        print("This Video number is not avaialable")


def main():
    videos = load_data()
    while True:
        print("\n")
        print("\t Youtube Manager\n")
        print("1. List all the videos")
        print("2. Add videos")
        print("3. Update Video Details")
        print("4. Delete Video")
        print("5. Exit..")
        option = input("Please choose the option: ")

        match option:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case __:  # __ <- default
                print("Invalid Option..")
                
main()