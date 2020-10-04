import person as p
import block as b
import interval_schedule


#List of tags
food_tag = set(["Food"])
sleep_tag = set(["Sleep"])
test_tag = set(["Test"])
max_tags = {"Food":3, "Sleep":1}


shifts = []
people = []
pairs = []

#This assigns the weight of differnt sleep schedules based on how far away from the original they are
#Currently the value of sleep is set to 100-(sleep_offset)^2, this means the more offset a sleep
#schedule becomes the lower value it has
sleep_value_eq = lambda x: 100-(person.sleep_offset(x)**2)

#shift1 is the first job that needs to be filled
#you add all of the tasks shift one could possibly do to a list
shift1 = []
shift1.append(b.block(1,3,5))
shift1.append(b.block(2,5,6))
shift1.append(b.block(4,6,5))
shift1.append(b.block(6,7,4))
shift1.append(b.block(7,9,2))
shift1.append(b.block(5,8,11))
shifts.append(shift1)

shift2 = []
shift2.append(b.block(20,24,6))
shift2.append(b.block(16,19,7))
shift2.append(b.block(15,16,3))
shift2.append(b.block(12,15,5))
shift2.append(b.block(14,17,6))
shift2.append(b.block(13,16,8))
shifts.append(shift2)

#All astronauts and their sleepschedules go here
people.append(p.person("a", 0,8))
people.append(p.person("b",16,24))


#See who has the best outcome for shift 1: place them in shift 1
#See who has the best outcome for shift 2: place them in shift 2
#ect
for shift in shifts:
  shift_scores = []
  for person in people:
    sleeptimes = []
    
    # This puts 16 different sleep blocks into the list. It then evaluates
    # each sleep block seperatly
    for start in range(0,24, 1):
      sleeptimes.append(b.block(start, start+person.sleep_duration, sleep_value_eq(start), sleep_tag))
    shift_scores.append(interval_schedule.optimize_schedule(sleeptimes+shift, max_tags))
  i = shift_scores.index(max(shift_scores, key= lambda x: x.value))
  pairs.append([shift_scores[i], people[i]])
  people.pop(i)

#printing results
for pair in pairs:
  print("Person:", pair[1])
  print("Schedule:", pair[0])
  print()

