from board import Board
from search import SearchProblem, ucs
import util


class BlokusFillProblem(SearchProblem):
    """
    A one-player Blokus game as a search problem.
    This problem is implemented for you. You should NOT change it!
    """

    def __init__(self, board_w, board_h, piece_list, starting_point=(0, 0)):
        self.board = Board(board_w, board_h, 1, piece_list, starting_point)
        self.expanded = 0

    def get_start_state(self):
        """
        Returns the start state for the search problem
        """
        return self.board

    def is_goal_state(self, state):
        """
        state: Search state
        Returns True if and only if the state is a valid goal state
        """
        return not any(state.pieces[0])

    def get_successors(self, state):
        """
        state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        # Note that for the search problem, there is only one player - #0
        self.expanded = self.expanded + 1
        return [(state.do_move(0, move), move, 1) for move in state.get_legal_moves(0)]

    def get_cost_of_actions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        return len(actions)



#####################################################
# This portion is incomplete.  Time to write code!  #
#####################################################
class BlokusCornersProblem(SearchProblem):

    board = None
    expanded = None
    targets = None

    def __init__(self, board_w, board_h, piece_list, starting_point=(0, 0)):
        self.board = Board(board_w, board_h, 1, piece_list, starting_point)
        self.expanded = 0
        self.targets = [(0, 0), (board_h-1, 0), (0, board_w-1), (board_h-1, board_w-1)]

    def get_start_state(self):
        """
        Returns the start state for the search problem
        """
        return self.board

    def is_goal_state(self, state):
        for height, width in self.targets:
            if state.state[height][width] == -1:
                return False
        return True

    def get_successors(self, state):
        """
        state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        # Note that for the search problem, there is only one player - #0
        self.expanded = self.expanded + 1
        return [(state.do_move(0, move), move, move.piece.get_num_tiles()) for move in state.get_legal_moves(0)]

    def get_cost_of_actions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        cost = 0
        for action in actions:
            cost += action.piece.get_num_tiles()
        return cost


def blokus_corners_heuristic(state, problem):
    """
    Your heuristic for the BlokusCornersProblem goes here.

    This heuristic must be consistent to ensure correctness.  First, try to come up
    with an admissible heuristic; almost all admissible heuristics will be consistent
    as well.

    If using A* ever finds a solution that is worse uniform cost search finds,
    your heuristic is *not* consistent, and probably not admissible!  On the other hand,
    inadmissible or inconsistent heuristics may find optimal solutions, so be careful.
    """
    import numpy as np
    targets = list()

    # find remaining targets
    for goal in problem.targets:
        height, width = goal
        if state.state[height][width] == -1:
            targets.append(goal)

    # find the minimal straight line distances to all the targets from the give state
    # distance calculated with manhattan distance
    dist = state.board_h + state.board_w
    distance_vec = [dist for i in range(len(targets))] # initialize with high values
    for height in range(state.board_h):
        for width in range(state.board_w):
            if state.state[height][width] != -1:
                for num, (i, j) in enumerate(targets):
                    new_dist = np.abs(height-i) + np.abs(width-j)
                    if new_dist < distance_vec[num]:
                        distance_vec[num] = new_dist
    # sum all the distance BlokusCoverProblem(self.board.board_w, self.board.board_h,
    total_distance = sum(distance_vec)
    return total_distance


class BlokusCoverProblem(SearchProblem):
    def __init__(self, board_w, board_h, piece_list, starting_point=(0, 0), targets=[(0, 0)]):
        self.targets = targets.copy()
        self.expanded = 0
        self.board = Board(board_w, board_h, 1, piece_list, starting_point)

    def get_start_state(self):
        """
        Returns the start state for the search problem
        """
        return self.board

    def is_goal_state(self, state):
        "*** YOUR CODE HERE ***"
        for height, width in self.targets:
            if state.state[height][width] == -1:
                return False
        return True

    def get_successors(self, state):
        """
        state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        # Note that for the search problem, there is only one player - #0
        self.expanded = self.expanded + 1
        return [(state.do_move(0, move), move, move.piece.get_num_tiles()) for move in state.get_legal_moves(0)]

    def get_cost_of_actions(self, actions):
        """
        actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        cost = 0
        for action in actions:
            cost += action.piece.get_num_tiles()
        return cost


def blokus_cover_heuristic(state, problem):
    import numpy as np
    targets = list()

    # find remaining targets
    for goal in problem.targets:
        height, width = goal
        if state.state[height][width] == -1:
            targets.append(goal)

    # find the max straight line distances to all the targets from the give state
    # distance calculated with manhattan distance
    dist = state.board_h + state.board_w
    distance_vec = [dist for i in range(len(targets))] # initialize with high values
    for height in range(state.board_h):
        for width in range(state.board_w):
            if state.state[height][width] != -1:
                for num, (i, j) in enumerate(targets):
                    new_dist = np.abs(height-i) + np.abs(width-j)
                    if new_dist < distance_vec[num]:
                        distance_vec[num] = new_dist

    # use the maximal distance
    if distance_vec != []:
        max_distance = sum(distance_vec)
    else:
        max_distance = 0
    return max_distance

class ClosestLocationSearch:
    """
    In this problem you have to cover all given positions on the board,
    but the objective is speed, not optimality.
    """

    def __init__(self, board_w, board_h, piece_list, starting_point=(0, 0), targets=(0, 0)):
        self.expanded = 0
        self.targets = targets.copy()
        "*** YOUR CODE HERE ***"
        self.board = Board(board_w, board_h, 1, piece_list, starting_point)
        self.start_pos = starting_point

    def get_start_state(self):
        """
        Returns the start state for the search problem
        """
        return self.board

    def solve(self):
        """
        This method should return a sequence of actions that covers all target locations on the board.
        This time we trade optimality for speed.
        Therefore, your agent should try and cover one target location at a time. Each time, aiming for the closest uncovered location.
        You may define helpful functions as you wish.

        Probably a good way to start, would be something like this --

        current_state = self.board.__copy__()
        backtrace = []

        while ....

            actions = set of actions that covers the closets uncovered target location
            add actions to backtrace

        return backtrace
        """
        import numpy as np
        import search
        targets = self.targets[:]
        # find closest point to the start position
        start_h = self.start_pos[0]
        start_w = self.start_pos[1]
        min_dist_point = self.targets[0]
        dist = np.abs(start_h-min_dist_point[0]) + np.abs(start_w-min_dist_point[1])
        for target in self.targets:
            new_dist = np.abs(start_h-target[0]) + np.abs(start_w-target[1])
            if new_dist < dist:
                dist = new_dist
                min_dist_point = target

        # define a new cover problem with the found point
        # and use uniform search cost to find optimal solution
        cover_problem = BlokusCoverProblem(self.board.board_w, self.board.board_h, self.board.piece_list,
                self.start_pos, [min_dist_point])
        actions = search.ucs(cover_problem)
        self.expanded = cover_problem.expanded
        targets.remove(min_dist_point)

        # find the closest target point in the current state
        # define a new cover problem and find the optimal solutino with ucs
        while targets != []:
            current_state = self.board.__copy__()
            for action in actions:
                current_state = current_state.do_move(0, action)

            min_dist_point = self._get_closest_point(current_state)
            cover_problem = BlokusCoverProblem(self.board.board_w, self.board.board_h, self.board.piece_list,
                    self.start_pos, [min_dist_point])
            cover_problem.board = current_state
            actions += search.ucs(cover_problem)
            self.expanded += cover_problem.expanded
            targets.remove(min_dist_point)

        return actions


    def _get_closest_point(self, state):
        ''' returns the closest target point in the given state '''
        import numpy as np
        points = list()

        # find remaining targets
        for goal in self.targets:
            height, width = goal
            if state.state[height][width] == -1:
                points.append(goal)

        dist = state.board_h + state.board_w
        distance_vec = [dist for i in range(len(points))] # initialize with high values
        for height in range(state.board_h):
            for width in range(state.board_w):
                if state.state[height][width] != -1:
                    for num, (i, j) in enumerate(points):
                        new_dist = np.abs(height-i) + np.abs(width-j)
                        if new_dist < distance_vec[num]:
                            distance_vec[num] = new_dist
        return points[distance_vec.index(min(distance_vec))]




class MiniContestSearch :
    """
    Implement your contest entry here
    """

    def __init__(self, board_w, board_h, piece_list, starting_point=(0, 0), targets=(0, 0)):
        self.targets = targets.copy()
        "*** YOUR CODE HERE ***"

    def get_start_state(self):
        """
        Returns the start state for the search problem
        """
        return self.board

    def solve(self):
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

