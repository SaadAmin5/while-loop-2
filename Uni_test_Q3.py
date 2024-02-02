'''Question 3

Write a Python program that reads a series of positive integer numbers one by one from the 
keyboard (ending by -1) and, at the end, outputs 'Yes' once if the numbers were in (strictly) 
ascending order, otherwise it outputs 'No' (again, only once and at the end).

For example, it should output 'Yes' for 3, 5, 8, 15, 22, -1, and for 10, 20, 45, -1; 
but ‘No’ for 3, 5, 4, 8, -1, for 1, 2, 1, -1, and for 3, 5, 5, 8, -1.

You may assume that the user enters at least two positive numbers before the -1 and 
that there are no incorrect inputs.
'''

#solution

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