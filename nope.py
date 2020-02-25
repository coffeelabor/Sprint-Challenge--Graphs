
'''
Tried to do a bft to scout the rooms then a dfs to move player
'''
from ast import literal_eval
import random
from util import Stack, Queue
from world import World
from player import Player
from room import Room
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

'''
############################ WORKS ###################################
'''

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# Keeps track of route the player took
traversal_path = []


# keeps track of what rooms the player has visited
visited = {}

# Starting room as per the readme
beginning_room = {'n': '?', 's': '?', 'w': '?', 'e': '?'}
# The player begins in room '0'
visited[0] = beginning_room

# Useing a bfs that looks for a '?'


def bfs_map(starting_vertex):
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
        # If room is not in bfs_visited
        if room_vertex not in bfs_visited:
            # Check if its reached a target of '?'
            for room in visited[room_vertex]:
                # print('room', room)
                # Check if the set has the current room and that room has unexplored exits
                if visited[room_vertex][room] == '?':
                    # print('Path', path)
                    # If it finds an unexplored exit, break the loop and return the path to it
                    return path
            # Mark it as visited
            bfs_visited.add(room_vertex)
            # then add a path to all neighbors to the back of the queue
            for neighbor in visited[room_vertex]:
                # Make a copy of the path
                path_copy = list(path)
                # print('path_copy 1', path_copy)
                # append the path copy with neighbor
                path_copy.append(visited[room_vertex][neighbor])
                # print('path_copy 2', path_copy)
                # Add the path copy to the queue
                queue.enqueue(path_copy)
    # If no destination was found return None
    return None

# Finds a possible route to travel down


def travel_route(route):
    # all the possible exits for a room
    exit_list = []
    # print('exit_list', exit_list)
    # print('route', route)

    # Cycle through each room in the route being passed in
    for room in route:
        # print('room', room)
        # Find how many exits each room has
        for exit in visited[route[0]]:
            # print('visited', visited[route[0]][exit])
            # print('visited1', visited[route[0]])
            # print('visited2', visited[exit])
            # print(f'exit, {exit}, room: {room}')
            # Check if the room and the exit for the first visited room are a match
            if room == visited[route[0]][exit]:
                # Add the exit to the list
                exit_list.append(exit)
                # print('exit_list', exit_list)
    # Return a list of exits for the room
    return exit_list

# Simple if else function for the inverse of each direction so the player can backtrack the route


def backtrack_route(direction):
    reverse_direction = None
    if direction == 'n':
        reverse_direction == 's'
        # print('reverse_direction', reverse_direction)
    elif direction == 's':
        reverse_direction == 'n'
        # print('reverse_direction', reverse_direction)
    elif direction == 'w':
        reverse_direction == 'e'
        # print('reverse_direction', reverse_direction)
    elif direction == 'e':
        reverse_direction == 'w'
        # print('reverse_direction', reverse_direction)
    return reverse_direction


# While loop that runs until it hits a 'break'
while True:
    # Variable for just finding the location id of where the player is
    current_room = visited[player.current_room.id]
    # List of exits in each room
    room_list = []
    # print('room_list', room_list)
    # Cycle through the current room exits
    for next_room in current_room:
        # print('next_room', next_room)
        # Check if there are any unexplored exits
        if current_room[next_room] == '?':
            # Add the unexplored room directions to the room exit list
            room_list.append(next_room)
    # print(f'room_list, {room_list}, current {current_room}')
    # Check if a room has at least 1 unexplored direction
    if len(room_list) > 0:
        # Randomely choose a direction to travel in
        random.shuffle(room_list)
        # Set a direction to travel down based on the list of shuffled rooms
        travel_direction = room_list[0]
        # Use a variable that can be used for the backtrack_route function
        previous_room = visited[player.current_room.id]
        # The id of the previous room
        previous_room_id = player.current_room.id
        # Add the direction to the path for the player to travel
        traversal_path.append(travel_direction)
        # Use the travel method to actually move the direction
        player.travel(travel_direction)
        # Create a set to store the exits for an uneplored room
        set_exits = {}
        # Check if the player is currently in a room that is not been visited
        if player.current_room.id not in visited:
            # Find all the exits in a non-visited room
            for direction in player.current_room.get_exits():
                # Update the exits in the room to a '?' so it can be explored
                set_exits.update({direction: '?'})
            # Update the room to have the exits that need to be explored
            visited[player.current_room.id] = set_exits
        # Start juggleing the room ids so the algo can go back to keep exploring rooms
        previous_room[travel_direction] = player.current_room.id
        # Set the direction to backtrack once it has explored a path
        backtrack = backtrack_route(travel_direction)
        # print('backtrack', backtrack)
        # Update the visited set to reflect all the room's exits
        visited[player.current_room.id][backtrack] = previous_room_id
        # print('visited', visited)
    # Else the player has hit a dead end
    else:
        # Set a variable that starts the bfs to find a new destination to search for
        get_route = bfs_map(player.current_room.id)
        # If there are still valid paths to travel
        if get_route is not None:
            # A variable for storing the route with new direction
            directions = travel_route(get_route)
            # loop through all the directions in the route
            for direction in directions:
                # print('direction', direction)
                # Make a new traversal path with the directions
                traversal_path.append(direction)
                # Move the player in the direction
                player.travel(direction)
        # If all the rooms have been explored than bfs return None so break the while loop
        if get_route == None:
            break

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")



'''
###################################################################
'''

