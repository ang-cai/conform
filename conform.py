def please_flip_original(caps: list[str])-> list[str]:   
  """
    Generates a minimal list of shouts needed to have all fan caps face the same direction.

    Args:
      caps: list of strings which are either 'F' (Forward) or 'B' (Backward)

    Return:
      a list of shouts, which could be empty if the list of caps is either empty or all the same direction
  """
  intervals = []       
  interval_start = 0 
  forward_count = backward_count = 0 
  shouts = []

  #Step 1: Determine intervals where hats face the same direction
  if len(caps) == 0:
    return []
  for i in range(1, len(caps)):
    if caps[interval_start] != caps[i]:
      intervals.append((interval_start, i - 1, caps[interval_start])) #(start, end, direction)
       	 
      if caps[interval_start] == 'F':
        forward_count += 1
      else:
        backward_count += 1
      interval_start = i   #new hat direction->new interval start 

  intervals.append((interval_start, len(caps)-1, caps[interval_start]))
  if caps[interval_start] == 'F':
    forward_count += 1
  else:
    backward_count += 1
  
  #Step 2: Decide which way to flip based on hat direction with least number of intervals
  if forward_count < backward_count:
    flip_direction = 'F'
  else:
    flip_direction = 'B'
  
  #Step 3: Flip all of the intervals that match with the flip direction
  for t in intervals:
    if t[2] == flip_direction and str(t[0]) != str(t[1]):
        shouts.append(f"People in positions {str(t[0])} through {str(t[1])} flip your caps!")
    elif t[2] == flip_direction:
        shouts.append(f"Person in position {str(t[0])} flip your cap!")

  return shouts

def please_flip_streamlined(caps: list[str])-> list[str]:
  """
    Generates a minimal list of shouts needed to have all fan caps face the same direction.

      Args:
      caps: list of strings which are either 'F' (Forward) or 'B' (Backward)

      Return:
      a list of shouts, which could be empty if the list of caps is either empty or all the same direction
  """
  intervals = []       
  interval_start = 0 
  forward_count = backward_count = 0 
  shouts = []
  new_caps = caps.copy()
  new_caps.append("end")
  #Step 1: Determine intervals where hats face the same direction
  for i in range(1, len(new_caps)):
    if new_caps[interval_start] != new_caps[i]:
      intervals.append((interval_start, i - 1, new_caps[interval_start])) #(start, end, direction)
       	 
      if new_caps[interval_start] == 'F':
        forward_count += 1
      else:
        backward_count += 1
      interval_start = i   #new hat direction->new interval start
  
  #Step 2: Decide which way to flip based on hat direction with least number of intervals
  if forward_count < backward_count:
    flip_direction = 'F'
  else:
    flip_direction = 'B'
  
  #Step 3: Flip all of the intervals that match with the flip direction
  for t in intervals:
    if t[2] == flip_direction and str(t[0]) != str(t[1]):
        shouts.append(f"People in positions {str(t[0])} through {str(t[1])} flip your caps!")
    elif t[2] == flip_direction:
        shouts.append(f"Person in position {str(t[0])} flip your cap!")

  return shouts

def please_flip_bare(caps: list[str])-> list[str]:
  """
    Generates a minimal list of shouts needed to have all fan caps face the same direction, skipping
    fans with no cap.

      Args:
      caps: list of strings which are either 'F' (Forward) or 'B' (Backward) or 'H' (Bareheaded)

      Return:
      a list of shouts, which could be empty if the list of caps is either empty or all the same direction
  """
  intervals = []       
  interval_start = 0 
  forward_count = backward_count = 0 
  shouts = []
  new_caps = caps.copy()
  new_caps.append("end")
  #Step 1: Determine intervals where hats face the same direction
  for i in range(1, len(new_caps)):
    if new_caps[interval_start] != new_caps[i]:
      intervals.append((interval_start, i - 1, new_caps[interval_start])) #(start, end, direction)
       	 
      if new_caps[interval_start] == 'F':
        forward_count += 1
      elif new_caps[interval_start] == 'B':
        backward_count += 1
      interval_start = i   #new hat direction->new interval start
  
  #Step 2: Decide which way to flip based on hat direction with least number of intervals
  if forward_count < backward_count:
    flip_direction = 'F'
  else:
    flip_direction = 'B'
  
  #Step 3: Flip all of the intervals that match with the flip direction
  for t in intervals:
    if t[2] == flip_direction and str(t[0]) != str(t[1]):
        shouts.append(f"People in positions {str(t[0])} through {str(t[1])} flip your caps!")
    elif t[2] == flip_direction:
        shouts.append(f"Person in position {str(t[0])} flip your cap!")

  return shouts

def please_flip_one_pass(caps:list)->list:
  """
    Generates a minimal list of shouts needed to have all fan caps face the same direction using exactly 1 for loop

      Args:
      caps: list of strings which are either 'F' (Forward) or 'B' (Backward)

      Return:
      a list of shouts, which could be empty if the list of caps is either empty or all the same direction
  """
  intervals = []       
  interval_start = 0 
  shouts = []
  new_caps = caps.copy()
  new_caps.append("end")
  
  if new_caps[interval_start] == 'B':
    flip_direction = 'F'
  else:
    flip_direction = 'B'

  for i in range(1, len(new_caps)):
    if new_caps[interval_start] != new_caps[i]:
      intervals.append((interval_start, i - 1, new_caps[interval_start])) #(start, end, direction)
       	 
      if new_caps[interval_start] == flip_direction and interval_start != i-1:
        shouts.append(f"People in positions {interval_start} through {i - 1} flip your caps!")
      elif new_caps[interval_start] == flip_direction:
        shouts.append(f"Person in position {interval_start} flip your cap!")
      
      interval_start = i   #new hat direction->new interval start  

  return shouts

if __name__ == "__main__":
    # Some exercise 1, 2, & 4 test cases:
    caps_1 = ["F", "F", "B", "B", "B", "F", "B", "B", "B", "F", "F", "B", "F"]
    caps_2 = ["F", "F", "B", "B", "B", "F", "B", "B", "B", "F", "F", "F", "F"]
    caps_3 = ["B", "B", "F", "F", "B", "F", "F", "F", "B", "B"]
    caps_4 = ["B", "B", "B", "B", "B"]

    # Some exercise 3 test cases:
    caps_5 = ["F", "F", "B", "H", "B", "F", "B", "B", "B", "F", "H", "F", "F"]
    caps_6= ["B", "B", "F", "H", "F", "B", "F", "F", "F", "B", "H", "B", "H"]

    print(please_flip_original(caps_1))           #Ex 1
    print(please_flip_streamlined(caps_1))       #Ex 2

    print(please_flip_bare(caps_5))             #Ex 3

    print(please_flip_one_pass(caps_1))          #Ex 4
