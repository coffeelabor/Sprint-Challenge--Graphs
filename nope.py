
'''
Tried to do a bft to scout the rooms then a dfs to move player
'''
been_there = []

exit_options = {'n': 'n', 's': 's', 'w': 'w', 'e': 'e'}

# I need something to return me to the room with 2 exits

print("Heres a print statement")


def __init__(self):
    self.vertices = {}


def add_vertex(self, vertex_id):
    self.vertices[vertex_id] = set()


def get_neighbors(self, vertex_id):
    return self.vertices[vertex_id]

# bft until it hits a room with >2 exits or a dead end


def bft_scout(self, starting_vertex):
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

# use the path scouted to the as the destination for the player to move


def dfs_player(self, starting_vertex, destination_vertex):
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
###################################################################
'''
'''
Tried to implement a bfs within a graph, like the projects
'''
class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]
    # Useing a bfs that looks for a '?'

    # def bfs_map(self, starting_vertex):
    def bfs_map(self, starting_vertex, destination_vertex):
        # create an empty queue
        queue = Queue()
        # Create an empty set to store visited rooms
        bfs_visited = set()
        # Add a path to the starting vertex_id to the queue
        queue.enqueue([starting_vertex])
        # While the queue is not empty...
        while queue.size() > 0:
            # dequeue, the first path
            path = queue.dequeue()
            # Grab the last rom from the path
            room_vertex = path[-1]
            # Check if its reached a target of '?'
            # if room_vertex == "?":
            if room_vertex == destination_vertex:
                return path
            # If room is not in bfs_visited
            if room_vertex not in bfs_visited:
                # Mark it as visited
                bfs_visited.add(room_vertex)
                # then add a path to all neighbors to the back of the queue
                for neighbor in self.get_neighbors(room_vertex):
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    queue.enqueue(path_copy)


'''
###################################################################
'''
'''
for neighbor in visited[room_vertex]:
                # Make a copy of the path
                path_copy = path.copy()
                print('path_copy 1', path_copy)
                # append the path copy with neighbor
                path_copy.append(neighbor)
                print('path_copy 2', path_copy)
                # Add the path copy to the queue
                queue.enqueue(path_copy)
'''
