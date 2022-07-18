def add_many(*avg):
    result =0
    for i in avg:
        result = result + i
        
    return result

a = add_many(1,2,3,4,5,6,7,8,9,10)
print(a)