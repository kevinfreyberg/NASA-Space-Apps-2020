import block as b
import schedule as s


def optimize_schedule(lst):
  #List is a list of blocks
  
  #Sort list by rising end time
  lst.sort(key=lambda x: x.end)
  weight_array = []
  
  #Solution array keeps track of what blocks are use
  #This allows us to return the solution as a list of blocks
  solution_array = []
  max_weight_index = 0

  # If you want to limit the ammount a tag can show up ex
  # Eating food has a very high value cause its important, if you dont limit
  # the ammount of meals the algorithm will make astronauts eat all day
  max_tags = {"Food":3, "Sleep":1}

  # copy weights into an array
  # put every block into its own a schedule and then the solution array
  for i in range(len(lst)-1):
    weight_array.append(lst[i].weight)
    schedule = s.schedule(dict.fromkeys(max_tags,0))
    schedule.insert_block(lst[i])
    solution_array.append(schedule)

  # https://www.youtube.com/watch?v=cr6Ip0J9izc
  # Weight array contains the best value you can have if you pick that array
  # As you progress through the list you see if element i overlaps with elemement j
  # If it does not then you check to see if i's weight_array_value is better than
  # i's original value + j's weight_array_value
  for i in range(0,len(lst)-1):
    for j in range(1,i): 
      #A tag conflit is when you have to many of one type of event. Ex: 2 Sleep times
      if not s.tag_conflict(solution_array[i], lst[j], max_tags):
        continue
      
      #If there is a time overlap, there is nothing to do
      elif (b.overlapping(lst[j], lst[i])):

        continue
      
      else:
        #If i's orginal value + j's weight array > i's current weight_array
        #You also need to clear and reset the current solution if the one you
        #just found is better
        if lst[i].weight + weight_array[j] > weight_array[i]:
          weight_array[i] = lst[i].weight + weight_array[j]
          solution_array[i].clear()
          solution_array[i].copy(solution_array[j])
          solution_array[i].insert_block(lst[i])
          #If weight array was updated then check to see if its the new max
          if weight_array[i] > weight_array[max_weight_index]:
            max_weight_index = i
      #input()

  solution_array[max_weight_index].lst.sort(key=lambda x: x.start)
  return solution_array[max_weight_index]
