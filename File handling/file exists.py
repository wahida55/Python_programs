import os
if os.path.isfile("New_text"):
    with open("New_text","r") as f:
        data=f.read()
        print(data)
else :
    print("File does not exist!!")