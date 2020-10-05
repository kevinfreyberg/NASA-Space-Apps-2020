import person as p
import block as b
import interval_schedule


#List of tags, weights 1->4 depending on importance
#You can use functions to variably set the weight based on the time - see sleep
exercise_tag = set(["Exercise"]) #weight 1
work_tag = set(["Work"]) #weight 1
food_tag = set(["Food"]) #weight 2
sleep_tag = set(["Sleep"]) #weight variable
dock_tag = set(["Docking"]) #weight 4
launch_tag = set("Launching") #weight 4
landing_tag = set(["Landing"]) #weight 4
undock_tag = set(["Undocking"]) #weight 4

#Food = 1 hour per, Sleep is defined by input, Exercise = 1 hour, Work = 1 hour
max_tags = {"Food":3, "Sleep":1, "Exercise":1, "Work":12} 

shifts = []
people = []
pairs = []

#This assigns the weight of differnt sleep schedules based on how far away from the original they are
#Currently the value of sleep is set to 100-(sleep_offset)^2, this means the more offset a sleep
#schedule becomes the lower value it has
sleep_value_eq = lambda x: 1000-(person.sleep_offset(x)**2)
      


#All astronauts and their sleepschedules go here
#people.append(p.person("a", 0,8))
#people.append(p.person("b",16,24))

print("Welcome to our sleep shift scheduling tool! What is your name?\n")
name = input()
print("\nHi, {}! When do you normally go to sleep (24H Format, round by hour)?\n".format(name))
sleep_start = int(input())
print("\nWhen do you normally wake up (24H Format, round by hour)?\n")
sleep_end = int(input())
print("\nWould you consider yourself a morning-person (a), night-person (b), or in-between (c)?\n")
choice = str(input())

possible_choices = ["a", "b", "c"]
while (choice not in possible_choices):
  print("\nInvalid input!\n")
  print("\nWould you consider yourself a morning-person (a), night-person (b), or in-between (c)?\n")
  choice = str(input())

people.append(p.person(name, sleep_start, sleep_end))
shifts = []

#shift1 is the first job that needs to be filled
#you add all of the tasks shift one could possibly do to a list
for person in people:
  shift = [] #Hours 8-24
  for time in range(0, 24): #generates time blocks for all activities
    shift.append(b.block(time,(time+1)%24,10,exercise_tag))
    shift.append(b.block(time,(time+1)%24,2,work_tag))
    shift.append(b.block(time, (time+person.sleep_duration)%24, sleep_value_eq(person.sleep_offset(time)), sleep_tag))
  for time in range(0, 24, 4): #Food is served every 4 hours. Only add a food block every 4 hours
    shift.append(b.block(time,(time+1)%24,10,food_tag))
  shifts.append(shift)

#adds shifts based on preferences
if choice == "a":
  #shifts.append(shift1)
  pass
elif choice == "b":
  #shifts.append(shift1)
  pass
else:
  #shifts.append(shift1)
  pass

#See who has the best outcome for shift 1: place them in shift 1
#See who has the best outcome for shift 2: place them in shift 2
#ect
for shift in shifts:
  shift_scores = []
  for person in people:
    shift_scores.append(interval_schedule.optimize_schedule(shift, max_tags))
  i = shift_scores.index(max(shift_scores, key= lambda x: x.value))
  pairs.append([shift_scores[i], people[i]])
  people.pop(i)

#printing results
for pair in pairs:
  print("Person:", pair[1])
  print("Schedule:", pair[0])
  print()





