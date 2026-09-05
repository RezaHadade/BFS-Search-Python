# Breadth-First Search (BFS)

Breadth-First Search (BFS) is an **uninformed search algorithm** that explores the state-space search tree level by level. In other words, it expands all nodes at the current depth before moving on to nodes at the next depth.

## FIFO Queue

To guarantee this level-by-level exploration, BFS uses a **FIFO (First-In, First-Out)** data structure for its frontier.

In this implementation, the frontier is managed using Python's `collections.deque`, which provides efficient **O(1)** insertion and removal operations at both ends of the queue.

The FIFO behavior of the queue ensures that nodes generated earlier are expanded earlier, which is what allows BFS to explore the search space level by level.

## Goal Test

An important aspect of this implementation is the placement of the goal test.

In Breadth-First Search, nodes are generated in the same depth order in which they are expanded. Therefore, the goal test can be performed when a node is generated rather than waiting until it is selected for expansion.

This allows the algorithm to detect the goal earlier and avoid unnecessary operations.

## Path Reconstruction

If the goal is found, the `get_path()` function can be used to reconstruct the path from the initial node to the goal node.

This is typically achieved by keeping track of the relationship between each node and its parent during the search process.

## Properties

### Completeness

BFS is **complete**, meaning that it is guaranteed to find a solution if one exists, assuming the branching factor is finite.

Unlike Depth-First Search (DFS), BFS does not get trapped exploring a single infinitely deep branch because it explores the search space level by level.

### Optimality

BFS is **optimal when all step costs are equal** (or when the objective is to find the solution with the minimum number of steps).

Since BFS explores shallower nodes before deeper nodes, the first goal it finds is guaranteed to have the minimum depth.

### Time Complexity

**O(b^d)**

Where:

* `b` = branching factor
* `d` = depth of the shallowest goal node

### Space Complexity

**O(b^d)**

BFS must keep a large number of nodes in memory, especially those in the frontier. This is one of its main limitations.

## Limitations

The biggest drawback of BFS is its high **time and memory consumption**.

Because BFS explores the search space level by level, the number of nodes grows exponentially as the depth increases. The algorithm may need to store a very large number of nodes in memory before reaching the goal.

For this reason, BFS can become impractical for large search spaces or problems with deep solutions.

---

**In summary, BFS is complete and optimal for equal step costs, but its exponential time and space requirements make it unsuitable for many large-scale problems.**

## Example

Graph = {
  'Arad': ('Zerind', 'Sibiu', 'Timisoara'),
  'Zerind': (),
  'Timisoara': (),
  'Sibiu': ('Arad', 'Fagaras', 'Rimnicu Vilcea'),
  'Fagaras': ('Sibiu', 'Bucharest'),
  'Rimnicu Vilcea': ('Sibiu', 'Pitesti'),
  'Pitesti': ('Rimnicu Vilcea', 'Bucharest'),
  'Bucharest': ()
}

Start: Arad
Goal: Bcharest 

Output:
Arad → Sibiu → Fagaras → Bucharest
