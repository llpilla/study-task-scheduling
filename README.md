# Practical scheduling activity using tasks with dependencies

This repository is intended for use by students to practice concepts related to scheduling tasks with dependencies.
It contains a few scheduling algorithms (priority functions for list scheduling) and some support functions.
A set of activities using this repository is presented in the [activities section](#activities) below.

## How To

- The code in this repository is written using Python3 with no additional modules.

- To run a code example, try `python3 example.py`.

- To learn more about the schedulers and support functions, try the code below in your Python3 interpreter:

```python
>>> import simulator.schedulers as schedulers
>>> help(schedulers)
>>> help(schedulers.priority_by_id)
```

- To check if the code you downloaded or changed is still working properly, try the following commands:

```bash
$ cd unitary_tests
$ ./test_graph.py 
$ ./test_simulator.py
$ ./test_implemented_schedulers.py
```

- To check if the new schedulers you have implemented are working as intended, try the following commands:

```bash
$ cd unitary_tests
$ ./test_other_schedulers.py 
```

## Activities

**Basic steps**

0. Run `python3 example.py` and try to understand its results. Check how to write code to use this simple scheduling simulator. Try to generate other task graphs and tests while also using *priority\_by\_topological\_order*. You can draw one of the graphs and check how the scheduling decisions are being made.

1. Write the priority functions using the Largest Processing Time (LPT) and the Shortest Processing Time (SPT) policies (complete functions in [the schedulers file](simulator/schedulers.py)). Check if they pass the tests in [the unitary tests' file](unitary_tests/test_other_schedulers.py). Compare how they perform against each other for a few basic graphs.

2. Run experiments using the previous priority functions for graphs with over a thousand tasks. Vary the number of resources and analyze how they behave. Is there an algorithm that always provides the best results?

3. Write the Highest Level First (HLF) and the largest number of successors priority policies (complete functions in [the schedulers file](simulator/schedulers.py)). Check if they pass the tests in [the unitary tests' file](unitary_tests/test_other_schedulers.py). Compare how they perform against each other for a few basic graphs.

4. Run experiments with the new algorithms and compare their results to the ones achieved in Step 3. Choose one of the graphs, draw it, and analyze how different algorithms lead to different scheduling decisions.

**Additional challenge**

5. Write the Critical Path (CP) scheduling policy based on the value of the bottom level of the tasks (complete function *priority\_by\_cp* in [the schedulers file](simulator/schedulers.py)). Check if it passes the test in [the unitary tests' file](unitary_tests/test_other_schedulers.py).

6. Choose a small graph, draw it, and analyze how its priorities are computed with the CP scheduling policy.

7. Run `python3 large_complete_test.py` and compare the results for all different policies. Try to vary the parameters used for the task graph and the number of resources and see if the same performance behavior appears or not.
