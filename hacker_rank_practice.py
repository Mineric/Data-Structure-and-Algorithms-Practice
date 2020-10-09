def hourGlassSum(arr):
    chunkArr = []
    hourGlassArr = []
    sumHour = []
    
    for index in range(0, len(arr)-2):
        chunkArr.append(arr[index : index+3])

    for j in chunkArr:
        for i in range(1, 5):
            hourGlassArr.append([j[0][i-1], j[0][i], j[0][i+1], j[1][i], j[2][i-1], j[2][i], j[2][i+1]])

    for k in range(0, len(hourGlassArr)):
        hourGlassArr[k] = sum(hourGlassArr[k])
    

    return max(hourGlassArr)
