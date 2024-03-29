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
    INFTY = 100000
    targets = list()
    # find remaining targets
    for target in problem.targets:
        height, width = target
        if state.state[height][width] == -1:
            targets.append(target)

    if len(targets) == 0:
        return 0

    targets_distance = {target: INFTY for target in targets}
    for start in _new_start(state):
        for target in targets:
            targets_distance[target] = min(targets_distance[target], _chebyshev_distance(start, target))
    cost = targets_distance[max(targets_distance, key=targets_distance.get)]

    '''
    # make sure that the optimal solution is reachable
    reach = 0
    for piece in state.piece_list:
        piece_index = state.piece_list.pieces.index(piece)
        if state.pieces[0, piece_index] == True:
            reach += piece.get_num_tiles()
    if reach < cost:
        cost = INFTY
    '''

    return cost

def _chebyshev_distance(pos1, pos2):
    return max(abs(pos1[0] - pos2[0]), abs(pos1[1] - pos2[1]))


def _get_corners(x, y, state):
    ''' Returns a list of valid corner position states on the board for the give (x,y) position
        if a corner is occupied the list will contain a non -1 value'''
    all_corners = [(x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)]
    # valid sides are position that don't step beyond the board size
    valid_corners = [i for i in all_corners if i[0] >= 0 and i[1] >= 0 and i[0] < state.board_h and i[1] < state.board_w]
    return [state.state[i][j] for i, j in valid_corners]

def _get_sides(x, y, state):
    ''' Returns a list of valid side position states on the board for the give (x,y) position
        if a side is occupied the list will contain a non -1 value'''
    all_sides = [(x, y-1), (x, y+1), (x+1, y), (x-1, y)]
    # valid sides are position that don't step beyond the board size
    valid_sides = [i for i in all_sides if i[0] >= 0 and i[1] >= 0 and i[0] < state.board_h and i[1] < state.board_w]
    return [state.state[i][j] for i, j in valid_sides]

def _new_start(state):
    ''' Iterator that returns valid board start positions for the given state
        Valid board start positions are positions where it's legal to place a piece of size 1 '''
    for i in range(state.board_h):
        for j in range(state.board_w):
            # if current board position is occupied, skip
            if state.state[i][j] != -1:
                continue
            corners = _get_corners(i, j, state)
            sides = _get_sides(i, j, state)

            # if atleast one corner is occupied and no side is occupuied
            if 0 in corners and 0 not in sides:
                yield (i, j)


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
    targets = list()
    # find remaining targets
    for target in problem.targets:
        height, width = target
        if state.state[height][width] == -1:
            targets.append(target)
    return len(targets)

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
        targets = self.targets[:]
        # find closest point to the start position
        min_dist_point = self.targets[0]
        dist = util.manhattanDistance(self.start_pos, min_dist_point)
        for target in self.targets:
            new_dist = util.manhattanDistance(self.start_pos, target)
            if new_dist < dist:
                dist = new_dist
                min_dist_point = target

        # define a new cover problem with the found point
        # and use uniform search cost to find optimal solution
        cover_problem = BlokusCoverProblem(self.board.board_w, self.board.board_h, self.board.piece_list,
                                           self.start_pos, [min_dist_point])
        actions = ucs(cover_problem)
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
            actions += ucs(cover_problem)
            self.expanded += cover_problem.expanded
            targets.remove(min_dist_point)

        return actions


    def _get_closest_point(self, state):
        ''' returns the closest target point in the given state '''
        live_targets = list()

        # find remaining targets
        for target in self.targets:
            height, width = target
            if state.state[height][width] == -1:
                live_targets.append(target)

        max_dist = state.board_h + state.board_w
        distance_vec = [max_dist for target in live_targets] # initialize with high values
        for start in _new_start(state):
            if state.state[start[0]][start[1]] != -1:
                for i, target in enumerate(live_targets):
                    new_dist = util.manhattanDistance(start, target) + 1
                    if new_dist < distance_vec[i]:
                        distance_vec[i] = new_dist
        return live_targets[distance_vec.index(min(distance_vec))]


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

