f=open("E:\Machine Learning\demo.txt","a")  #Append text

f.write("\ni wanted to learn javascript")
f.close()

f=open("E:\Machine Learning\demo.txt","w")  #Overwrite file
f.write("I am a good boy")
f.close()

import os                                   #Delete file
os.remove("E:\Machine Learning\demo.txt")
