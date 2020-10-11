def balanced_num(number):
    n = str(number)
    left_sum=0
    right_sum=0
    
    if len(n)%2 == 0:
        left = list(n[:len(n)//2-1])
        right = list(n[len(n)//2+1:])
    elif len(n)%2 == 1:
        left = n[:len(n)//2]
        right = n[len(n)//2+1:]
        
        
    for i in left:
        left_sum += int(i)
        
    for j in right:
        right_sum += int(j)
        
    if left_sum == right_sum:
        return "Balanced"
    else:
        return "Not Balanced"
  
        
