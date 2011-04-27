## @package pcat
# @TODO: needs full header

## THIS IS ALL JUST TESTING

# from pcat.globals import globals
# from pcat.globals import globals
# 
# import urwid

# under construction



"""
import time
import urwid

class gui:

# constructor of the gui object
def __init__(self):
  self.running = True
  self.next = 4
  print "self.next = ", self.next, " and self.running = ", self.running

  # this is the primary execution method that prepares and
  # starts the urwid terminal gui
  def run(self):
    loop = urwid.MainLoop(self._frame, unhandled_input=self.input)
    loop.run()

  # this function handles particular input from the user
  # escape shortcuts are 'q' and 'Q'
  def input(self, input):
    if input in ('q', 'Q'):
      self.running = False
      raise urwid.ExitMainLoop()

  def next(self):
    self.next += 1
    return self.next

  # these columns are in the body section of the frame
  # they have attributes that represent their tasks as
  # well as are referenced by the palette
  _body_columns = urwid.Columns([
    # column 1
    urwid.Text("Test Column 1"),
    # column 2
    urwid.Text("Test Column 2"),
    # column 3
    urwid.Text("Test Column 3")
    ], 1)

    # this is the top-most header object that simply names the
    # application, the class, and the authors of the project
    _header = urwid.Columns([
      urwid.Padding(urwid.BigText("ODUCS CS487", urwid.Thin6x6Font()), "left", width="clip"),
      urwid.BoxAdapter(urwid.Filler(urwid.Text("Group1 - Protein Structure - Alvin, Cole, Tim, Emre"), "middle"), 6),
      ])

  _debugging = [
    urwid.Text("Sample 1"),
    urwid.Text("Sample 2"),
    urwid.Text("Sample 3"),
  ]
	
  # this is the bottom-most footer object that is the container
  # for real-time debugging information printed from any of the nodes
  _footer = urwid.Pile([
    urwid.Columns([
      urwid.Text("Real-time debugging ---"),
      urwid.Divider()
    ]),
    urwid.BoxAdapter(urwid.ListBox(_debugging), 8),
    ])

	
  # urwid.LineBox(urwid.BoxAdapter(urwid.Filler(urwid.Text("Debugging information ---"), "top"), 8))
  _wrapper = urwid.Filler(_body_columns, "top")
  
  _frame = urwid.Frame(_wrapper, header=_header, footer=_footer)
		
  # overloaded class extending urwid.ListWalker to provide
  # an interface to urwid's signals for automatic updating of
  # the debug-scrolling contents
  # class debugger(urwid.ListWalker):
  # 	
  # 	def __init__(self):
			

if __name__ == "__main__" :
  g = gui()
  g.run()

  exit
"""
