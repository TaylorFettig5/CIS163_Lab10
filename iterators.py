"""
Taylor Fettig
Lab 10
11/08/2023
"""

# Class for BackwardsList
class BackwardsList():
    def __init__(self):
        # Starting list is 1,2,3
        self.data = [1,2,3]
        # Setting value variable to -1
        self.value = -1
        
    def __iter__(self):
        return self   
    
    def __next__(self):
        # If starting value is -1, 
        if self.value == -1:
            # Gives index of last element
            self.value = len(self.data) - 1
        else:
            self.value -= 1
        # StopIteration  
        if self.value < 0:
            raise StopIteration
        
        return self.data[self.value]
    # Appends given item to end of list    
    def add(self, item):
        self.data.append(item)
        self.value = -1
        
myList = BackwardsList()

# Output: 3 2 1
for item in myList:
    print(item)  

myList.add(4)

# Output: 4 3 2 1
for item in myList:
    print(item) 
    
# Class for ListThirds
class ListThirds():
    def __init__(self):
        # Starting list is A, B, C, D, E
        self.data = ['A','B','C','D','E']
        # Keeps track of current position
        self.value = 0
        # Keeps track of returned elements
        self.returned = 0
        
    def add(self, item):
        self.data.append(item) 
        
    def __iter__(self):
        return self    
        
    def __next__(self):
        # If returned is equal to length of list, StopIteration
        if self.returned == len(self.data):
            raise StopIteration
        # Get the next element
        next_ = self.data[self.value]
        # Increment the counter
        self.value = (self.value + 3) % len(self.data)
        self.returned += 1

        return next_
    
myList = ListThirds()
# Output: A,D,B,E,C
for item in myList:
    print(item)
        
