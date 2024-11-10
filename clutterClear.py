import os
import shutil


#this is for copying images from one folder to another.

# print(os.getcwd())
# origin="D:/Semesters/Phone/Pictures/.thumbnails"
# destination="D:/Semesters/Semester 1/PYTHON/OOP/Pictures"
# # files=os.listdir(origin)

# try:
#     for i in range(12,51):
#         file_path = os.path.join(origin, files[i])
#         shutil.copy2(file_path, destination)
# except PermissionError as e:
#     print(f"Permission Denied {e}")

# print("The files copied are as follows:\n ",os.listdir(destination))

# files_=os.listdir(destination)
# for count in range(len(files_)):
#     file_path=os.path.join(destination,files_[count])
#     new_name=f"D:/Semesters/Semester 1/PYTHON/OOP/Pictures/{count}.png"
#     os.rename(file_path,new_name)
#     print("The files are renamed")


#this for copying and for renaming the files.

class clutterClear:
    def __init__(self,origin,destination):
        self._origin=origin
        self._destination=destination

    def copy(self):
        files=os.listdir(self._origin)
        try:
            for i in range(12,51):
                file_path = os.path.join(self._origin, files[i])
                shutil.copy2(file_path, self._destination)
        except PermissionError as e:
            print(f"Permission Denied {e}")

        print("The files copied are as follows:\n ",os.listdir(self._destination))
    
    def rename(self):
        files_=os.listdir(destination)
        for count in range(len(files_)):
            file_path=os.path.join(destination,files_[count])
            new_name=f"{destination}"+"/"+f"{count}"+".png"
            os.rename(file_path,new_name)
        print("The files are renamed")

if __name__=="__main__":
    origin=""
    destination=""
    C1=clutterClear(origin,destination)
    choice=int(input("Press 1 to copy files.\nPress 2 to rename files\nPress 3 to quit!"))

    if(choice==1):
        print("Enter the file origin!")
        origin=input("")
        destination=input("")
        print("Enter the file destination!")
        C1.copy()
    elif(choice==2):
        print("Enter destination!")
        destination=input("")
        C1.rename()
    elif(choice!=1 or choice!=2):
        print("Please enter proper integer!")

            

