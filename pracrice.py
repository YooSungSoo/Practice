def add_mul(choice,*avg):

    if choice == "add":
        result = 0
        for i in avg:
            result = result + i
        
    elif choice=="mul":
        result = 1
        for i in avg:
            result = i * result
    return result

a = add_mul("mul",1,2,3,4,5)

print(a)