import os
if os.path.isfile("New_text"):
    lc=wc=cc=0
    f=open("New_text","r")
    for line in f:
            lc=lc+1
            words_per_line=len(line.split())
            wc=wc+words_per_line
            char_per_line=len(line)
            cc=cc+char_per_line
    print("No of lines:",lc)
    print("No of word count:", wc)
    print("No of character count:", cc)
else :
    print("File does not exist!!")