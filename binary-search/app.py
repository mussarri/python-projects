def binary_search(target, list):
    step = 0
    middle = 0
    start = 0
    end = len(list) 
    
    while start<=end:
        print("Step: " + str(step) + " List: " + str(list[start:end+1]))
        step = step + 1
        middle = (start + end)//2 
        print("Start: " + str(start) + " Middle: " + str(middle) + " End: " + str(end))
        if(target == list[middle]):
            print(str(list[middle]))
            return middle
        elif(target > list[middle]):
            start = middle + 1
        elif(target < list[middle]):
            end = middle - 1 
    return -1
            
        

binary_search(2, [1,2,3,4,5,6])