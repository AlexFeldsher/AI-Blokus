"""
In search.py, you will implement generic search algorithms
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def get_start_state(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def is_goal_state(self, state):
        """
        state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def get_successors(self, state):
        """
        state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def get_cost_of_actions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def depth_first_search(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches
    the goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    # fringe is a stack of tuples (state,  actions)
    # actions is a list of actions that led to that state from the start
    fringe = util.Stack()
    fringe.push((problem.get_start_state(), list()))
    closed = set()

    while not fringe.isEmpty():
        current, actions = fringe.pop()
        if problem.is_goal_state(current):
            return actions
        elif current not in closed:
            for successor, action, _ in problem.get_successors(current):
                if successor in closed:
                    continue
                fringe.push((successor, actions + [action]))
            closed.add(current)
    return list()


def breadth_first_search(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    # fringe is a stack of tuples (state,  actions)
    # actions is a list of actions that led to that state from the start
    fringe = util.Queue()
    fringe.push((problem.get_start_state(), list()))
    closed = set()

    counter = 0
    while not fringe.isEmpty():
        current, actions = fringe.pop()
        if problem.is_goal_state(current):
            return actions
        elif current not in closed:
            counter += 1
            for successor, action, _ in problem.get_successors(current):
                if successor in closed:
                    continue
                fringe.push((successor, actions + [action]))
            closed.add(current)
    return list()


def uniform_cost_search(problem):
    """
    Search the node of least total cost first.
    """
    # fringe is a stack of tuples (state,  actions)
    # actions is a list of actions that led to that state from the start
    fringe = util.PriorityQueue()
    fringe.push(PriorityTuple((problem.get_start_state(), list()), 0), 0)
    closed = set()

    while not fringe.isEmpty():
        current, actions = fringe.pop()
        if problem.is_goal_state(current):
            return actions
        elif current not in closed:
            for successor, action, _ in problem.get_successors(current):
                if successor in closed:
                    continue
                new_actions = actions + [action]
                cost = problem.get_cost_of_actions(new_actions)
                fringe.push(PriorityTuple((successor, new_actions), cost), cost)
            closed.add(current)
    return list()


def null_heuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def a_star_search(problem, heuristic=null_heuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    fringe = util.PriorityQueue()
    fringe.push(PriorityTuple((problem.get_start_state(), list()), 0), 0)
    closed = set()

    while not fringe.isEmpty():
        current, actions = fringe.pop()
        if problem.is_goal_state(current):
            return actions
        elif current not in closed:
            for successor, action, _ in problem.get_successors(current):
                if successor in closed:
                    continue
                new_actions = actions + [action]
                cost = problem.get_cost_of_actions(new_actions) + heuristic(successor, problem)
                fringe.push(PriorityTuple((successor, new_actions), cost), cost)
            closed.add(current)
    return list()

class PriorityTuple():

    tup = None
    priority = None

    def __init__(self, tup, priority):
        self.tup = tup
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __iter__(self):
        for item in self.tup:
            yield item



# Abbreviations
bfs = breadth_first_search
dfs = depth_first_search
astar = a_star_search
ucs = uniform_cost_search
