"""Module containing the scheduling simulator (engine).

The simulator takes a DAG of tasks and a number of resources, and
computes how the tasks would execute following their priorities.
"""

import heapq   # for heaps (it implements only min-heaps)

import matplotlib.pyplot as plt


def simulate(graph, num_resources, debug=False, scheduler=""):
    """Simulation engine.

    Parameters
    ----------
    graph : Graph object
        DAG of tasks to run
    num_resources : int
        Number of identical resources to simulate
    debug : bool [default = False]
        True if debug messages should be printed
    scheduler :
        the name of the scheduler used

    Returns
    -------
    int
        Makespan
    """
    print('* Starting the simulation *')
    if debug:
        print(f'- Graph of {len(graph.vertices)} tasks running on' +
              f' {num_resources} resources')

    # Setup:
    # - Creates a list of free resources
    free_resources = [i for i in range(num_resources)]
    # - Puts all available tasks (top tasks) in the priority queue
    priority_queue = list()
    for task in graph.vertices.values():
        if not task.predecessors:
            priority_queue.append(task)
            if debug:
                print(f'- {task} is ready to run')
    heapq.heapify(priority_queue)
    # - Sets the start time as zero
    time = 0
    # - Creates the bootstrapping event in the event queue of the simulator
    # format of an event: (time, task id, resource id)
    events = [(time, None, None)]

    #
    fig, gnt = plt.subplots()
    gnt.set_ylim(0, num_resources * 10)

    gnt.set_xlabel('time')
    gnt.set_ylabel('resources')

    gnt.set_yticks([5 + i * 10 for i in range(num_resources + 1)])
    gnt.set_yticklabels([i + 1 for i in range(num_resources + 1)])

    gnt.grid(True)
    colors = ['blue', 'green', 'red', 'yellow']
    color_id = 0

    # Simulation runs while there are events to handle
    # Steps:
    # 1. remove the first event, see if there are any new free tasks
    # 2. schedule available tasks while there are available resources
    while events:
        # Step 1
        time, task_id, res_id = heapq.heappop(events)
        if task_id != None:
            # event: task finished running
            task = graph.vertices[task_id]
            if debug:
                print(f'[t={time}]: END {task}, resource {res_id}')

            # removes the task from the predecessors of its successors
            for succ_id in task.successors:
                successor = graph.vertices[succ_id]
                successor.predecessors.remove(task_id)
                # if it has no predecessors, it is free to run
                if not successor.predecessors:
                    heapq.heappush(priority_queue, successor)
                    if debug:
                        print(f'- {successor} is now ready to run')

            # adds the resource to the list of available resources
            free_resources.append(res_id)

        # Step 2
        while free_resources and priority_queue:
            # pops the first free resource and free task
            res_id = free_resources.pop(0)
            task = heapq.heappop(priority_queue)
            end_time = time + task.load
            # creates the event for the task's execution
            heapq.heappush(events, (end_time, task.id, res_id))
            gnt.broken_barh([(time, task.load - 0.1)], (res_id * 10, 9), facecolors=colors[color_id % len(colors)])
            color_id += 1

            if debug:
                print(f'[t={time}]: START {task}, resource {res_id}')

    plt.legend()
    plt.savefig(f"scheduling_using_{scheduler}_with_{num_resources}_resources.png")

    # No more events
    print(f'* Total execution time (makespan) = {time}\n')
    return time
