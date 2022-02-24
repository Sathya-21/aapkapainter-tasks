input_list=[1,2,3,2,1]
dump_list=[]
for i in input_list:
  if i in dump_list:
    print(i)
    break
  else:
    dump_list.append(i)
    
