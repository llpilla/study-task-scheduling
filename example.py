"""Example of use of the simulator.

To run, use 'python3 example.py'.

"""

import simulator.schedulers as schedulers
from simulator.graph import Graph
from simulator.simulator import simulate

print('Scenario 1: 6 tasks over 2 and 3 resources - ordered task ids')
graph = Graph.generate_graph(6, (1, 10), (0, 3), False, 5)
print(graph)
schedulers.priority_by_id(graph)
simulate(graph, 2, True)
graph.reset_predecessors()
simulate(graph, 3, True)

print('\nScenario 2: 6 tasks over 2 and 3 resources - unordered task ids')
graph = Graph.generate_graph(6, (1, 10), (0, 3), True, 5)
print(graph)
schedulers.priority_by_id(graph)
simulate(graph, 2, True)
graph.reset_predecessors()
simulate(graph, 3, True)
