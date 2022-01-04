from node import Node 

class Node2Way(Node):
    def __init__(self,initdata):
        Node.__init__(self,initdata)
        self.previous = None

    def getPrevious(self):
        return self.previous

    def setPrevious(self,newprevious):
        self.previous = newprevious


