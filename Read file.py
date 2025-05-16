f = open("E:\Machine Learning\demo.txt", "r")

data = f.read()    #Reads the entire file
print(data)

f.seek(0)          #Moves file pointer back to the beginning
data = f.read(5)   #Reads the first 5 characters
print(data)

f.seek(0)           
line1 = f.readline()  # reads the first line
print(line1)

f.close()
