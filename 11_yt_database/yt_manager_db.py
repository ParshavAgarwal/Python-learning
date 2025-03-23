import sqlite3

con = sqlite3.connect('youtube.db')

cursor = con.cursor()
cursor.execute('''
            CREATE TABLE IF NOT EXISTS videos(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                time TEXT NOT NULL
            )
''')

def list_video():
    cursor.execute("SELECT * FROM videos") # after executing, cursor holds the value
    
    print ("\n")
    print("-" * 100)
    print("\n")
        
    for row in cursor.fetchall():   # we are fetching all from cursor
        print(row) #main
        con.commit()
    print ("\n")
    print("-" * 100)
    print("\n")
        

def add_video(name, time):
    cursor.execute("INSERT INTO videos(name, time) VALUES (?,?)", (name,time))
    con.commit()

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    con.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos where id = ?", (video_id,))  # Tuple value -> (name,) - (comma is imp)
    con.commit()


def main():
    
    print ("\n")
    print("-" * 100)
    print("\n")
    
    while True:
        
        print("\t YOUTUBE MANAGER")
        print("1. List all Videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. delete a video")
        print("5. Exit..")
        choice = input("Please enter your choice: ")
        
        if choice == '1':
            list_video()
            
        elif choice == '2':
            name = input("Enter the name of the video: ")
            time = input("Enter the duration of the video: ")
            add_video(name, time)
            
        elif choice == '3':
            id = input("Enter the video id: ")
            name = input("Enter the name of the video: ")
            time = input("Enter the duration of the video: ")
            update_video(id, name, time)
            
        elif choice == '4':
            id = input("Enter the video id you wish to delete: ")
            delete_video(id)
            
        elif choice == '5':
            break
        
        else:
            print("Invalid Choice...")
        
    con.close()
    
if __name__ == "__main__":
    main()
