class block:
  def __init__(self, start, end, weight = 0):
    if start > end:
      end += 24
    self.start = start;
    self.end = end;
    self.weight = weight;

  def __repr__(self):
    return "(" + str(self.start) +","+ str(self.end)+")"

def overlapping(block1, block2):
  if (block2.start<block1.start<block2.end) or (block2.start<block1.end<block2.end):
    return True;
  else:
    return False;
