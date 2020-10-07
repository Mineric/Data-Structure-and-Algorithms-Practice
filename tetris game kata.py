def get_score(arr) -> int:
    score=[40, 100, 300, 1200]
    result=0
    step = []
    for i in (arr):
        step += i
        while step<=10:
            
        result += score [i-1]* step if step%10=0)
        print(score [i-1]* (1+step//10))
       # if step//10 >= 1:
        #    result = 
        
        #result += arr[i] * (score [arr[i]-1]*i)
        
    return result
