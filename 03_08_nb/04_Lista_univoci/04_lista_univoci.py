def unique_list(lst):
    uni=[]
   
    for ele in lst:
        if ele not in uni :
            uni.append(ele)
    
    return uni


print (unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))