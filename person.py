import block as b
class person:

  def __init__(self, name, sleep_start, sleep_end):
    #Each person has a name and a sleeping block
    self.name = str(name)
    self.sleep_block = b.block(sleep_start, sleep_end)
    self.sleep_duration = self.sleep_block.duration


  def sleep_offset(self, start_sleep_time):
    #Returns how much of an offset would be caused
    #if sleep started at start_sleep_time
    return self.sleep_block.start - start_sleep_time

  def __repr__(self):
    return self.name + str(self.sleep_block)
