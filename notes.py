'''
######Plan#########
I need to figure out what the role of 'moving' is.  Im not sure if i can just skip that and transvers the maze withought actually moving.  I have to explore each room.  To start I just want to get through the rooms regardless of how long it takes

How do the directions play into this?

'''

'''
######Plan#########
I need to figure out if its going to be a DFT vs BFT and DFS vs DFT

i need to at least get it to do one of the above through the smaller map


Get it to work with one of the algos then optimize

I think DFT of DFS would be the easiest to start tryig to make work.  

    I will need to initialize the stack
    I will need to push the world into the stack
        the starting room (world.starting_room) is set to None
    visited rooms will be a set
    current room will start off in starting room
        current_room = world.startingroom

Out of the Room file I might need to use:
    get_exits which shows where a player can move
    get_room_in_direction which the room in a given direction
Player has a travel method
    travel which tells the player which direction to go
I need to get the cyclic part figured out, I think thatll come into play here.



'''

'''
############ Methods ###############
'''
Room:
    def print_room_description(self, player)
    def get_exits(self):
    def get_exits_string(self):
    def connect_rooms(self, direction, connecting_room):
    def get_room_in_direction(self, direction):
    def get_coords(self):

World:
    def load_graph(self, room_graph):
    def print_rooms(self):
Player
    def travel(self, direction, show_rooms=False):
'''
############ Methods ###############
'''

'''
# Create an empty queue
    q = Queue()
    # Add the starting vertex_id to the queue
    q.enqueue(starting_vertex)
    # Create an empty set to store visited nodes
    visited = set()
    # While the queue is not empty...
    print("BREAK BFT")
    while q.size() > 0:
        # Dequeue, the first vertex
        v = q.dequeue()
        # Check if its been visited
        # if it has not been visited...
        if v not in visited:
            # Mark it as visited
            print(v)
            visited.add(v)
            # The add all neighbors to the back of the queue
            for neighbor in self.get_neighbors(v):
                q.enqueue(neighbor)


'''

'''
############## BFT #######################
# Create an empty queue
# Add the starting vertex_id to the queue
# Create an empty set to store visited nodes
# While the queue is not empty...
    # Dequeue, the first vertex
    # Check if its been visited
    # if it has not been visited...
        # Mark it as visited
        # The add all neighbors to the back of the queue    
'''
def bft(self, starting_vertex):
    """
    Print each vertex in breadth-first order
    beginning from starting_vertex.
    """
    # Create an empty queue
    q = Queue()
    # Add the starting vertex_id to the queue
    q.enqueue(starting_vertex)
    # Create an empty set to store visited nodes
    visited = set()
    # While the queue is not empty...
    print("BREAK BFT")
    while q.size() > 0:
        # Dequeue, the first vertex
        v = q.dequeue()
        # Check if its been visited
        # if it has not been visited...
        if v not in visited:
            # Mark it as visited
            print(v)
            visited.add(v)
            # The add all neighbors to the back of the queue
            for neighbor in self.get_neighbors(v):
                q.enqueue(neighbor)

'''
############## BFT #######################
'''

'''
############## DFT #######################
# Create an empty stack
# Push the starting vertex_id to the stack
# Create an empty set to store visited nodes
# While the stack is not empty...
    # Pop, the first vertex
    # Check if its been visited
    # if it has not been visited...
        # Mark it as visited
        # The push all neighbors to the top of the stack
'''

def dft(self, starting_vertex):
    """
    Print each vertex in depth-first order
    beginning from starting_vertex.
    """
    # Create an empty stack
    s = Stack()
    # Push the starting vertex_id to the stack
    s.push(starting_vertex)
    # Create an empty set to store visited nodes
    visited = set()
    # While the stack is not empty...
    print("BREAK DFT")
    while s.size() > 0:
        # Pop, the first vertex
        v = s.pop()
        # Check if its been visited
        # if it has not been visited...
        if v not in visited:
            # Mark it as visited
            print(v)
            visited.add(v)
            # The push all neighbors to the top of the stack
            for neighbor in self.get_neighbors(v):
                s.push(neighbor)

'''
############## DFT #######################
'''

'''
############## BFS #######################
    # Create an empty queue
    # # Add A PATH TO the starting vertex_id to the queue 
    # # Create an empty set to store visited nodes    
    # While the queue is not empty...
        # Dequeue, the first PATH
        # GRAB THE LAST VERTEX FROM THE PATH
        # CHECK IF ITS THE TARGET
            # If so, return the path
        # Check if its been visited
        # if it has not been visited...
            # Mark it as visited
            # Then add a PATH to all neighbors to the back of the queue
'''


def bfs(self, starting_vertex, destination_vertex):
    """
    Return a list containing the shortest path from
    starting_vertex to destination_vertex in
    breath-first order.
    """
    # Create an empty queue
    q = Queue()
    # # Add A PATH TO the starting vertex_id to the queue
    q.enqueue([starting_vertex])

    # # Create an empty set to store visited nodes
    visited = set()
    # While the queue is not empty...
    counter = 0
    print("BREAK BFS")
    while q.size() > 0:
        counter += 1
        print(counter)
        # Dequeue, the first PATH
        path = q.dequeue()
        # GRAB THE LAST VERTEX FROM THE PATH
        v = path[-1]
        # CHECK IF ITS THE TARGET
        if v == destination_vertex:
            # If so, return the path
            return path
        # Check if its been visited
        # if it has not been visited...
        if v not in visited:
            # Mark it as visited
            visited.add(v)
            # Then add a PATH to all neighbors to the back of the queue
            for neighbor in self.get_neighbors(v):
                path_copy = path.copy()
                path_copy.append(neighbor)
                q.enqueue(path_copy)


'''
############## BFS #######################
'''
'''
############## DFS #######################
    # Create an empty stack
    # Add a PATH to the starting vertex_id to the stack
    # Create an empty set to store visited nodes
    # While the stack is not empty...
        # Pop, the first PATH
        # GRAB the last vertex from the path
        # CHECK if its the target
            #  If so, return the path
        # Check if its been visited
        # If it has not been visitedd...
            # Mark it as visited
            # Then add a PATH to all neighbors to the top of the stack
                # (Make a copy of the path before adding)
'''

def dfs(self, starting_vertex, destination_vertex):
    """
    Return a list containing a path from
    starting_vertex to destination_vertex in
    depth-first order.
    """
    # Create an empty stack
    s = Stack()
    # Add a PATH to the starting vertex_id to the stack
    s.push([starting_vertex])
    # Create an empty set to store visited nodes
    visited = set()
    # While the stack is not empty...
    counter = 0
    print("BREAK DFS")
    while s.size() > 0:
        counter += 1
        print(counter)
        # Pop, the first PATH
        path = s.pop()
        # GRAB the last vertex from the path
        v = path[-1]
        # CHECK if its the target
        if v == destination_vertex:
            #  If so, return the path
            return path
        # Check if its been visited
        # If it has not been visitedd...
        if v not in visited:
            # Mark it as visited
            visited.add(v)
            # Then add a PATH to all neighbors to the top of the stack
            for neighbor in self.get_neighbors(v):
                # (Make a copy of the path before adding)
                path_copy = path.copy()
                path_copy.append(neighbor)
                s.push(path_copy)

'''
############## DFS #######################
'''
