def join(*arg,sep='-'):
    if len(arg)==0:
        return None
    final_list = arg[0]
    for i in range(1,len(arg)):
         final_list+=[sep]+arg[i]
    return final_list


print(join([1, 2], [8], [9, 5, 6], sep='@'))
print(join([1, 2], [8], [9, 5, 6],))
print(join([1]))
print(join())
