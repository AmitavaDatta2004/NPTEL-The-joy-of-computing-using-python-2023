def solution(marks):
    ### Enter your solution below this line
    ### Indent your entire code by one unit (4 spaces) to the right
    for i in range(1, len(marks)):
        key = marks[i]
        j = i - 1
        while j >= 0 and key < marks[j]:
            marks[j + 1] = marks[j]
            j -= 1
        marks[j + 1] = key
    n=len(marks)
    if (n%2)==1 :
        median=marks[int(((n+1)/2)-1)]
    else:
        median=(marks[int((n/2)-1)]+marks[int((n/2))])/2
### Enter your solution above this line
    return median
marks_input = input()

# Extracting numeric values from the input string
marks = [float(mark.strip()) for mark in marks_input.split(',') if mark.strip().isdigit()]


result = solution(marks)
print(result)
