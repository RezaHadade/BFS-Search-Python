'''BFS uses FIFO queue. In the other word, frontier must implement a FIFO queue of nodes'''
from collections import deque
# append() : appending a node to end of the list
# popleft() : poping a node from the front of the list


''' Actually, 'graph' is somehow the successor function - Problem formulation
    حرکات قابل انجام و حالات قابل دستیابی در/از هر حالت
'''
graph = {
    'A': ('B','C','D'),
    'B': ('E', 'F'),
    'C': ('G'),
    'D': ('H'),
    'E': (),
    'F': (),
    'G': (),
    'H': ()
}


class Node:
    
    def __init__(self, state, parent, depth):
        self.state = state
        self.parent = parent
        self.depth = depth     # ?


def expand(node):
     
    children = graph[node.state]
    children_nodes = []
    
    for child in children:
        child_node = Node(child, node, node.depth+1)
        children_nodes.append(child_node)
    
    return children_nodes


def goal_test(node, goal):
    if node.state == goal:
        return True


def in_frontier(state, frontier):
        for i in frontier:
            if i.state == state:
                return True

def get_path(goal_node):
    
    current = goal_node
    next = None
    path = []
    
    while current:
        next = current.parent
        path.append(current.state)
        current = next
    
    path.reverse()
    return path


def BFS(start_state, goal):
        
    frontier = deque()
    explored = set()
            
    start_node = Node(start_state, None, 0)
    
    frontier.append(start_node)

    while frontier:
    
        current_node = frontier.popleft()
        explored.add(current_node.state)
                 
        current_children = expand(current_node)
        for i in current_children:
        
            if goal_test(i, goal):      # آزمون هدف در لحظه گشترش         
                return i
            
            if i.state in explored or in_frontier(i.state, frontier):       # explored check
                continue
            
            
            frontier.append(i)
    
    return 'Failure'


goal = 'G'
start_state = 'A'

result = BFS(start_state, goal)
if result != 'Failure':
    goal = result
else:
    print(result)
    
goal_path = get_path(goal)

print(goal.state)
print(goal_path)
