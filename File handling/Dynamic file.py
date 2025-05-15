f=open("New_text","w")
while True:
    data = input("Enter data to enter :")
    f.write(data+'\n')
    option = input("Do you wish to enter any more data : [yes/no]")
    if option.lower()=="no":
        break
f.close()
print("Data written successfully !!")