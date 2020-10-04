#scheudle broken up in blocks, each block is associated with a weight

class block:
  def __init__(self, start, end, weight = 0, tag=set()): 
    if start > end: #takes care of overlapping, makes it easier to compare
      end += 24
    self.start = start;
    self.end = end;
    self.weight = weight;
    self.duration = self.end - self.start
    self.tags = tag; #tags is a dictionary used to limit the ammount of events in one day

  def __repr__(self): #printing out string, (start, end)
    return "(" + str(self.start) +","+ str(self.end)+")"

def overlapping(block1, block2): #returns true if blocks overlap
  if (block2.start<=block1.start<block2.end) or (block2.start<block1.end<=block2.end):
    return True; 
  else:
    return False;

