def format_duration(seconds):
    #your code here
    readable  = []

    a = readable[-2:]
    
    sec = seconds % 60 
    
    minu = (seconds - sec) % 3600
    
    hours = (seconds - minu) % (86400)
    
    days = (seconds - hours) % (31536000)
    
    years = (seconds - days) 

    print(sec, minu, hours, days , years)
    
    if sec != 0 :
       # second = ;" seconds" if sec > 1 else ' second'
        readable.append (str(sec) + (" seconds" if sec > 1 else " second"))
    
    if minu//60 != 0 :
        readable.append(str(minu // 60) + (" minutes" if minu//60 >1 else " minute"))
    
    if hours//3600 != 0:
        readable.append(str(hours // 3600) + (" hours" if hours//3600 > 1 else " hour"))

 
    if days//86400 != 0:
        readable.append(str(days // 86400) + (" days" if days//86400 > 1 else " day"))
          
    if years//31536000 != 0:
        readable.append(str(years // 31536000) + (" years" if year//31536000 >1 else " year"))
      
    if seconds == 0  :
        return "now"

    if len(readable) >= 2:
        return ' ,'.join(readable[::-1][:-1]) +  ' and ' + readable[0]

    return readable[0]
    
