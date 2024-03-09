output=[]
i=0
while(i<2):
    input_operations = input()
    separated_operations = input_operations.split(',')
    if separated_operations[0]=="JOIN":
        output.append(separated_operations[1])
    elif separated_operations[0]=="LEAVE":
        output.remove(output[0])
    elif separated_operations[0]=="MOVE":
        if separated_operations[2]=="HEAD":
            output.remove(separated_operations[1])
            output.insert(0,separated_operations[1])
        elif separated_operations[2]=="TAIL":
            output.remove(separated_operations[1])
            output.insert(len(output),separated_operations[1])
    elif separated_operations[0]=="PRINT":
        print(",".join(output))
    elif separated_operations[0]=="END":
        break
    i=i-1
