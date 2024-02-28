def parse_date(date_str):
    day, month, year = map(int, date_str.split('-'))
    return (day, month, year)

name1 = input().strip().capitalize()
dob1 = parse_date(input().strip())

name2 = input().strip().capitalize()
dob2 = parse_date(input().strip())

if dob1[4:]>dob2[4:]:
    print(name1 , end="")
elif dob1[4:]==dob2[4:]:
    if dob1[2:4]>dob2[2:4]:
        print(name1 , end="")
    elif dob1[2:4]==dob2[2:4]:
        if dob1[:2]>dob2[:2]:
            print(name1 , end="")
        elif dob1[:2]==dob2[:2]:
            sorted_name=sorted([name1,name2])
            print(sorted_name[0] , end="")
        else:
            print(name2 , end="")
    else:
        print(name2 , end="")
else:
    print(name2 , end="")
