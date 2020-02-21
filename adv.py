from room import Room
from player import Player
from world import World
from util import Stack, Queue
import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

def dfs_map(self, starting_vertex, destination_vertex):
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

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
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
