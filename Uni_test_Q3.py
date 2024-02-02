list1=[]

while True:
    
    num=int(input('enter positive integers, end by -1: '))
    
   
    if num==-1:
        break
        
    if num>0:
        list1.append(num)
               
        list2=list1.copy()
        list2.sort()


        if list1==list2:
            response='yes'

        elif list1 != list2:
            response='no'
    
   
        
print(response, 'for', list1)
