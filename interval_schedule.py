import block as b
#dynamic interval sheduzin

def schedule(lst):
  #List is a list of blocks
  lst.sort(key=lambda x: x.end)
  weight_array = []
  max_weight_index = 0
  
  for i in range(len(lst)-1):
    weight_array.append(lst[i].weight)
  
  for i in range(0,len(lst)-1):
    for j in range(1,i):
      print(lst)
      print(weight_array)
      print()
      if (b.overlapping(lst[j], lst[i])):
        print("index", j, "overlaps with",i)
        continue
      else:
        print("index", j, "does not overlap with",i)
        if lst[i].weight + weight_array[j] > weight_array[i]:
          weight_array[i] = lst[i].weight + weight_array[j]
        if weight_array[i] > weight_array[max_weight_index]:
          max_weight_index = i
    
  return weight_array[max_weight_index]

lst = []
lst.append(b.block(1,3,5))
lst.append(b.block(2,5,6))
lst.append(b.block(4,6,5))
lst.append(b.block(6,7,4))
lst.append(b.block(7,9,2))
lst.append(b.block(5,8,11))
print(schedule(lst))
