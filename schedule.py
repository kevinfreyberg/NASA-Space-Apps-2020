class schedule:
  def __init__(self, tags):
    self.lst = [];
    self.tags = tags;

  def insert_block(self, block):
    for item in block.tags:
      if self.tags[item]:
        self.tags[item] += 1;
      else:
        self.tags[item] = 1;
    self.lst.append(block);
      
  def count_tag(self, key):
    if tags[key]:
      return tags[key]
    else:
      return 0
  
  def __repr__(self):
    return str(self.lst)


def tag_conflict(s, b, max_tags):
  for tag in b.tags:
    if s.tags[tag] + 1 > max_tags[tag]:
      return False

  return True
