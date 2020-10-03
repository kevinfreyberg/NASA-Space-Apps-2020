import block as b

def schedule(lst):
  #List is a list of blocks
  
  #Sort list by rising end time
  lst.sort(key=lambda x: x.end)
  weight_array = []
  
  #Solution array keeps track of what blocks are use
  #This allows us to return the solution as a list of blocks
  solution_array = [] 
  max_weight_index = 0

  #copy weights into an array
  #copy each block into its solution array
  for i in range(len(lst)-1):
    weight_array.append(lst[i].weight)
    solution_array.append([lst[i]])

  # https://www.youtube.com/watch?v=cr6Ip0J9izc
  # Weight array contains the best value you can have if you pick that array
  # As you progress through the list you see if element i overlaps with elemement j
  # If it does not then you check to see if i's weight_array_value is better than
  # i's original value + j's weight_array_value
  for i in range(0,len(lst)-1):
    for j in range(1,i):
      #If there is an overlap, there is nothing to do
      if (b.overlapping(lst[j], lst[i])):
        continue
      else:
        #If i's orginal value + j's weight array > i's current weight_array
        if lst[i].weight + weight_array[j] > weight_array[i]:
          weight_array[i] = lst[i].weight + weight_array[j]
          solution_array[i].append(lst[j])
          #If weight array was updated then check to see if its the new max
          if weight_array[i] > weight_array[max_weight_index]:
            max_weight_index = i
  solution_array[max_weight_index].sort(key=lambda x: x.start)
  return solution_array[max_weight_index]

lst = []
lst.append(b.block(1,3,5))
lst.append(b.block(2,5,6))
lst.append(b.block(4,6,5))
lst.append(b.block(6,7,4))
lst.append(b.block(7,9,2))
lst.append(b.block(5,8,11))
print(schedule(lst))
