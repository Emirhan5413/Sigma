x = y = 0
list = []

while x < 10 and y < 10:
    
    if y > x:
        list.append(str(x)+str(y))
        
        y+=1
        if y == 10:
            y = 0
            x += 1
    else:
        y += 1

print(", ".join(list))