student=["md salauddin",21,"dinajpur"]
print(student[0])
student[0]="samiul"
print(student[0])

marks=[23,4,5,45,89,34] #mark=["a","d","g","f"]
print(marks[1:4])

marks.sort()  #asending order 
print(marks)

marks.sort(reverse=True) #Desending order
print(marks)

marks.reverse() #Reverse list
print(marks)

marks.pop(3)#remove index from list
print(marks)

tup=(1,3,5,7,2,7,8,97,7) #tuple. using count how time have the element
#("a","b","d,"b","e")
print(tup.count(7))