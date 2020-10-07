def tribonacci(signature, n):
    #your code here
    tribon = [signature[0], signature[1], signature[2]]
    s = 0
    for i in range(n-3):
        s = tribon[0+i] + tribon[1+i] + tribon[2+i]
        tribon.append(s)
             
    return tribon[:n]
            
    
