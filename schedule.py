class schedule:
  def __init__(self, tags):
    self.lst = [];
    self.tags = tags;
    self.value = 0;

  def insert_block(self, block):
    #When inserting a block you need to see if it has tags
    #You need to update the schedules's value
    #and you need to add it to the list of blocks
    for item in block.tags:
      if self.tags[item]:
        self.tags[item] += 1;
      else:
        self.tags[item] = 1;
    self.value += block.weight;
    self.lst.append(block);
      
  def count_tag(self, key):
    #returns how count of the tag that is passed
    if tags[key]:
      return tags[key]
    else:
      return 0
  
  def __repr__(self):
    return str(self.lst)

  def clear(self):
    #resets schedule
    self.lst = [];
    self.tags = dict.fromkeys(self.tags,0);
    self.value = 0;

  def copy(self, s):
    #copy another schedule into this one
    self.lst = s.lst.copy()
    self.tags = s.tags.copy()
    self.value = s.value


def tag_conflict(s, b, max_tags):
  #See if adding block b would put you over the max count for a specific tag
  for tag in b.tags:
    if s.tags[tag] + 1 > max_tags[tag]:
      return False

  return True
