class World:
    def __init__(self, used, probability, parent=None):
        self.used = used
        self.probability = probability
        self.child = []
        self.parent = parent

    def add_child(self, child):
        self.child.append(child)
    

        
    