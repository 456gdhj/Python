def sadman(list,idx=0):
    if(idx ==len(list)):
        return
    print(list[idx])
    sadman(list,idx+1)

new=["Dhka","Rangpur","Dinajpur"]
sadman(new)   
    
    