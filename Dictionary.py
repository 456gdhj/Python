student={
    "name":"Salauddin",
    "subject":{
       "phy":94,
       "Chem":89,
       "Math":91
   }

}
print(student)

print(student.keys()) #print all keys

print(student.values())#print all valuse

print(student.items()) #print all (key and value) tuple

print(student.get("name"))#return the key accroding to value

student.update({"city":"Dinajpur"}) #insert spesefiq item in dictionary
print(student)