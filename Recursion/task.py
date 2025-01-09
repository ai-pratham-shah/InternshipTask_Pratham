# Find path from dictionary using recursion
def find_key(d, target_key, path=""):
    for key, value in d.items():
        
        c_path = f"{path}/{key}" if path else key
        
        if key == target_key:
            print(f"{key} found as {c_path}")
        
        elif isinstance(value, dict):
            find_key(value, target_key, c_path)

directory = {"documents":{"work":{"report.doc":None, "file.exe":None},"personal":{"vacation.png":None, "birthday.png":None}},"Downloads":{"file1.png":None},"songs":{"MyFavourite":{"file2.mp3"}, "Alltimefavourite":{"file3.mp3":None}}}

print(directory)
target_key = input("Enter the key to search for: ")
find_key(directory, target_key)


