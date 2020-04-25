import sys # This has no purpose whatsoever. Do not question.

'''
A complete maze solver-er!

This code is self-editable and made to be rather readable, such that a non-coder can
use this as their homework. Even if your school offers you different formats for your maze
(aka make 0 the wall, 1 the path, etc) this code will be able to solve.

Scroll down and edit the values as needed.
'''

class Maze:
  def __init__(self):
    # Firstly we need to take values from a text file (let's say test_maze1.txt)
    # These lines of code do exactly that:
    extract = [i.rstrip().split(' ,') for i in open("test_maze1.txt")]
    str_extract = [j.split(', ') for i in extract for j in i]
    self.blueprint = [list(map(int, i)) for i in str_extract]
    # In essence, firstly we take out all the values from text file, strip and split (so as
    # to remove spaces and seperate them into different lists) into a list, seperates the 
    # collection of lists into singular numbers, and finally converts the numbers (which are
    # extracted as strings) into integers.
    
    # These are switches that will be later used to help the code backtrack!
    self.up_path = False
    self.down_path = False
    self.right_path = False
    self.left_path = False
    self.tried_path = {}
    
  def find_point(self, symbol):
    k = 0
    for n in self.blueprint:
      k += 1 # This is the y-value of the point! 
      for i, j in enumerate(n): # Enumerate results in the symbol and its position in the list
        if j == symbol:
          return(k-1, i) # Returns its position in the format (y-position, x-position)
            
  def on_symbol(self, destination):
    y, x = destination
    return self.blueprint[y][x] # Tells you the symbol that's on [y][x]
  
  def set_point(self, destination, symbol):
    try:
      y, x = destination
      self.blueprint[y][x] = symbol # Sets [y][x] as the given symbol
    except TypeError:
      print("you fool. you think you can play me by giving me a maze which doesn't have a starting point? foolish. i'm wise, wiser than everyone. you think you can outsmart me? come again after you've trained more, fool.")
      sys.exit()
      # Do not question.
      
      
  ##############################################################################################
  #
  # The following lines of code find the correct pathing to the maze, and thus are basically
  # the brains of the code! In essence they:
  #
  # -> Check all the directions. If there's any safespace, move there. You move by shifting your
  #    current position (which is 8) in the safe space, leaving a trail on your previous position
  #    and updating your current position.
  # -> You also note down which direction you went at what point. E.g. If you went west at (1, 0),
  #    it'll be stored in self.tried_path.
  # -> If there's no safe space (i.e. dead end), backtrack following the trail you left. 
  #    Once you find a path which has a zero, you start going there.
  # -> Whilst backtracking, you leave a trail of 7. This is to make sure you never come back on 7,
  #    and thus be able to go the correct path.
  # -> Once you see the ending next to you, you go there and stop the code. Simple!
  #
  ##############################################################################################

    
  def add_topathdict(self, point, symbol):
    try:
      if self.using_dict:
        self.tried_path[str(point)].append(symbol)
    except KeyError:
      if self.using_dict:
        self.tried_path[str(point)] = [symbol]
      
  def check_pathdict(self, point, symbol):
    point = str(point)
    try:
      if symbol not in self.tried_path[point]:
        return True
    except KeyError:
      return True
    
  def check_aroundforpoint(self, current_point, symbol):
    y, x = current_point
    aroundpoints = 0
    if x != len(self.blueprint[y])-1:
      if self.blueprint[y][x+1] in symbol:
        aroundpoints += 1
    if y != len(self.blueprint)-1:
      if self.blueprint[y+1][x] in symbol:
        aroundpoints += 1
    if x != 0:
      if self.blueprint[y][x-1] in symbol:
        aroundpoints += 1
    if y != 0:
      if self.blueprint[y-1][x] in symbol:
        aroundpoints += 1
    if aroundpoints > 0:
      aroundpoints = 0
      return True
    else:
      return False
    
  def turnoff_paths(self):
    self.right_path = False
    self.up_path = False
    self.left_path = False
    self.down_path = False
    
  def check_aroundpoint(self, current_point, symbol):
    y, x = current_point
    if x != len(self.blueprint[y])-1:
      if self.blueprint[y][x+1] not in symbol:
        if self.check_pathdict(current_point, ">"):
          self.right_path = True
    if y != len(self.blueprint)-1:
      if self.blueprint[y+1][x] not in symbol:
        if self.check_pathdict(current_point, "v"):
          self.down_path = True
    if x != 0:
      if self.blueprint[y][x-1] not in symbol:
        if self.check_pathdict(current_point, "<"):
          self.left_path = True
    if y != 0:
      if self.blueprint[y-1][x] not in symbol:
        if self.check_pathdict(current_point, "^"):
          self.up_path = True
  
  def calculate_travel(self, current_point):
    if self.right_path:
      self.add_topathdict(current_point, ">")
      self.turnoff_paths()
      return (0, 1)
    elif self.up_path:
      self.add_topathdict(current_point, "^")
      self.turnoff_paths()
      return (-1, 0)
    elif self.left_path:
      self.add_topathdict(current_point, "<")
      self.turnoff_paths()
      return (0, -1)
    elif self.down_path:
      self.add_topathdict(current_point, "v")
      self.turnoff_paths()
      return (1, 0)
    else:
      return False
    
  def move_point(self, current_point, distance, symbol):
    y, x = current_point
    moveY, moveX = distance
    self.blueprint[y+moveY][x+moveX] = symbol
    
  ########################################################################################
    
  def print_maze(self): # Prints the maze, self explanatory
    for i in self.blueprint:
      print (i)
      
  def check_end(self, end_point):
    try:
      check_num = int(end_point[0])
    except TypeError:
      print("fool. you fool. you think you can make me solve a code without giving me a proper end point? how foolish. i'm wise. i'm wiser than everyone. i can solve the maze faster than usain bolt can finish an ice cream. you fool, you think you can outsmart me? how stupid. one day, when you finally realise, you fool, come back again. perhaps one day you, a fool, will realise how truly wise i am.")
      sys.exit()
      # Do not question.
      
  def move_replace(self, point, symbol, second_symbol): 
    # Just to shorten the code a bit and to make it look less messy
    self.move_point(point, self.calculate_travel(point), symbol)
    self.set_point(point, second_symbol)
  
  # Here's everything compiled! 
  def solve_maze(self, start, wall, end, empty):
    end_point = self.find_point(end) 
    self.check_end(end_point) # Serves no purpose other than to, you know, call you a fool.
    
    current_point = self.find_point(start) # Finds the position of the start symbol
    self.set_point(current_point, 8) # Replaces the current position with 8
    
    self.found_solution = False
    
    while self.found_solution == False:
      self.using_dict = True # If we're adding the directions in the self.tried_path or not
      
      try:
        self.check_aroundpoint(current_point, [wall, start, 7])
        # Above line checks if there's a wall, trail/start or 7 around it. If there is, 
        # then the code will not move there!
        
        self.move_replace(current_point, 8, start) # Leaves a trail
        current_point = self.find_point(8) # Updates the position
        
        if self.check_aroundforpoint(current_point, [end]):
          self.check_aroundpoint(current_point, [wall, start, 7, empty]) # Only move to a 3
          self.move_replace(current_point, 8, start)
          self.found_solution = True # End the code!
          
      except TypeError:
        current_point = self.find_point(8)
        while self.check_aroundforpoint(current_point, [empty]) == False:
          # Basically, go on as long as there is no zero next to you
          self.using_dict = False
          self.check_aroundpoint(current_point, [wall, 7, end])
          
          # Essentially go back following the trail!
          self.move_replace(current_point, 8, 7)
          current_point = self.find_point(8)
          
    # These lines of code replace all seven with empty:
    ###
    k = 0
    for n in self.blueprint:
      k += 1
      for i, j in enumerate(n):
        if j == 7:
          self.set_point((k-1, i), empty)
        if j == 8:
          self.set_point((k-1, i), end)
    ####
    
    self.print_maze() # Finally, print the maze!
      
maze = Maze()

#########################################################################################
#
# You can edit the values down below to match your own maze! Edit the starting point,
# the ending point, what the wall is, and the safe point! 
# 
# NOTE: DO NOT USE 7 OR 8. IF YOU DO, EDIT THE CODE ACCORDINGLY.
#
#########################################################################################

START = 5 # Change this value according to what your start symbol is!
END = 3 # Change this value according to what your end symbol is!
        # Try putting a number (e.g. 6) that isn't in the maze as your start or end point. 
        # I recommend it.
WALL = 1 # Change this value according to what your wall symbol is!
SAFE = 0 # Change this value according to what your safe symbol is!

#########################################################################################

maze.solve_maze(START, WALL, END, SAFE) 
# ^ The holy line that runs everything. ^
# ^ Run the code and pray to the holy duck that it works ^
