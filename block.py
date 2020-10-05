#scheudle broken up in blocks, each block is associated with a weight

class block:
  def __init__(self, start, end, weight = 0, tag=set()): 
    self.start = start;
    self.end = end;
    self.weight = weight;
    self.duration = self.end - self.start if(self.end > self.start) else self.end - self.start + 24
    self.tags = tag; #tags is a dictionary used to limit the ammount of events in one day

  def __repr__(self): #printing out string, (start, end)
    string = "(" + str(self.start) +","+ str(self.end)
    if bool(self.tags):
      string += "," +str(self.tags)
    string += ")"
    return string

def overlapping(block1, block2): #returns true if blocks overlap
  cmp_start1 = block1.start if block1.start < block1.end else block1.start - 24
  cmp_start2 = block2.start if block2.start < block2.end else block2.start - 24
  if (cmp_start2<=cmp_start1<block2.end) or (block2.start<block1.end<=block2.end):
    return True; 
  elif (cmp_start1<=cmp_start2<block1.end) or (cmp_start1<block2.end<=block1.end):
    return True;
  elif (cmp_start1 == cmp_start2) or (block1.end == block2.end):
    return True;
  else:
    return False
