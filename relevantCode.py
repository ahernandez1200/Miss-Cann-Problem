class Problem:
    """The abstract class for a formal problem. You should subclass
    this and implement the methods actions and result, and possibly
    __init__, goal_test, and path_cost. Then you will create instances
    of your subclass and solve them with the various search functions."""

    def __init__(self, initial, goal=None):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal. Your subclass's constructor can add
        other arguments."""
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        raise NotImplementedError

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        raise NotImplementedError

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal or checks for state in self.goal if it is a
        list, as specified in the constructor. Override this method if
        checking against a single self.goal is not enough."""
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2. If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""
        return c + 1

    def value(self, state):
        """For optimization problems, each state has a value. Hill Climbing
        and related algorithms try to maximize this value."""
        raise NotImplementedError


class MissCannibals(Problem):
    def __init__(self, initial, goal=(0, 0, False)):
        super().__init__(initial, goal)

    """val is the either the current amount of miss on left,
     or the current amount of canniabals on the left. Seats refers
     to the # of people to be sent on the boat. This function checks
     to see if sending seats amount of people to the other side 
     is within range given val."""
    def within_bounds(val, seats):
        if val + seats < 0: return False

        if val + seats > 3: return False

        return True

    #returns true if cannibals outnumber missionaries. False otherwise.
    def cann_outnumber_miss(miss, cann):
        if cann > miss or (3-cann) > (3-miss): return True 

        return False

    def actions(self, state):
        stateList = list(state)
        miss = stateList[0]
        cann = stateList[1]
        on_left = stateList[2]

        possible_actions = []
        pos_or_neg = 1

        """sending pieces to the right is like subtracting, while sending
            to the left is like adding. So if we are moving pieces to the
            right, we set pos_or_neg to -1 for subtraction."""
        if on_left: pos_or_neg = -1

        """Loop checks to see if sending 1 missionary is a valid move,
            and then checks to see if sending 2 missionaries is a valid move"""
        for x in range(1, 3):
            if self.within_bounds(miss, x*pos_or_neg):
                if not self.cann_outnumber_miss(miss + x*pos_or_neg, cann):
                    possible_actions.push([x*pos_or_neg, 0, not on_left])
        
        """Loop checks to see if sending 1 cannibal is a valid move,
            and then checks to see if sending 2 cannibals is a valid move"""
        for x in range(1,3):
            if self.within_bounds(cann, x * pos_or_neg):
                if not self.cann_outnumber_miss(miss, cann + x*pos_or_neg):
                    possible_actions.push([0, x * pos_or_neg, not on_left])
        
        #checks to see if sending 1 cannibal and 1 missionary is a valid move
        if self.within_bounds(cann, pos_or_neg) and self.within_bounds(miss, pos_or_neg):
            if not self.cann_outnumber_miss(miss + pos_or_neg, cann + pos_or_neg):
                possible_actions.push([pos_or_neg, pos_or_neg, not on_left])
        


        # #checking to see if sending 2 missionaries is a valid move
        # #we first check to see if sending 2 missionaries is within bounds
        # #then, we check to see if cannibal ournumber missionaries
        # if self.within_bounds(miss, 2*pos_or_neg):
        #     if not self.cann_outnumber_miss(miss + 2*pos_or_neg, cann):
        #         possible_actions.push([2*pos_or_neg, 0, not on_left])

        # #checking to see if sending 1 missionary is a valid move
        # if self.within_bounds(miss, pos_or_neg):
        #     if not self.cann_outnumber_miss(miss + pos_or_neg, cann):
        #         possible_actions.push([pos_or_neg, 0, not on_left])

        # #checking to see if sending 2 cannibals is a valid move
        # if self.within_bounds(cann, 2*pos_or_neg):
        #     if not self.cann_outnumber_miss(miss, cann + 2*pos_or_neg):
        #         possible_actions.push([0, 2*pos_or_neg, not on_left])

        # #checking to see if sending 1 cannibal is a valid move
        # if self.within_bounds(cann, pos_or_neg):
        #     if not self.cann_outnumber_miss(miss, cann + pos_or_neg):
        #         possible_actions.push([0, pos_or_neg, not on_left])

      
        

        









class EightPuzzle(Problem):
    """ The problem of sliding tiles numbered from 1 to 8 on a 3x3 board, where one of the
    squares is a blank. A state is represented as a tuple of length 9, where  element at
    index i represents the tile number  at index i (0 if it's an empty square) """

    def __init__(self, initial, goal=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
        """ Define goal state and initialize a problem """
        super().__init__(initial, goal)

    def find_blank_square(self, state):
        """Return the index of the blank square in a given state"""

        return state.index(0)

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """

        # print(state)
        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        index_blank_square = self.find_blank_square(state)

        if index_blank_square % 3 == 0:
            possible_actions.remove('LEFT')
        if index_blank_square < 3:
            possible_actions.remove('UP')
        if index_blank_square % 3 == 2:
            possible_actions.remove('RIGHT')
        if index_blank_square > 5:
            possible_actions.remove('DOWN')

        return possible_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        # blank is the index of the blank square
        blank = self.find_blank_square(state)
        new_state = list(state)

        delta = {'UP': -3, 'DOWN': 3, 'LEFT': -1, 'RIGHT': 1}
        neighbor = blank + delta[action]
        new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]

        return tuple(new_state)

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """

        return state == self.goal

    def check_solvability(self, state):
        """ Checks if the given state is solvable """

        inversion = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if (state[i] > state[j]) and state[i] != 0 and state[j] != 0:
                    inversion += 1

        return inversion % 2 == 0

    def h(self, node):
        """ Return the heuristic value for a given state. Default heuristic function used is 
        h(n) = number of misplaced tiles """

        return sum(s != g for (s, g) in zip(node.state, self.goal))


# ______________________________________________________________________________