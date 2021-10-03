"""
Anthony Hernandez 
Kevin Nguyen CWID: 891028136
Dylan Ngo
"""


from search import *

class MissCannibals(Problem):
    def __init__(self, initial, goal=(0, 0, False)):
        super().__init__(initial, goal)

    """val is  either the current amount of miss on left,
     or the current amount of canniabals on the left. Seats refers
     to the # of people to be sent on the boat. This function checks
     to see if sending seats amount of people to the other side 
     is within range given val."""
    def within_bounds(self, val, seats):
        if val + seats < 0: return False

        if val + seats > 3: return False

        return True

    #returns true if cannibals outnumber missionaries. False otherwise.
    def cann_outnumber_miss(self, miss, cann):
        if cann > miss and miss != 0: return True
        if (3-cann) > (3-miss) and (3-miss) != 0: return True

        return False

    def actions(self, state):
        stateList = list(state) #converting tuple to list
        miss = stateList[0] #the number of missionaries on left side
        cann = stateList[1] #the number of cannibals on left side
        on_left = stateList[2] #whether the boat is on the left side

        action = "" #where we will temporarily hold our actions 
        possible_actions = [] #list of all possible actions 
        pos_or_neg = 1 # 1 if moving to the left, -1 if moving to the right.

        """sending pieces to the right is like subtracting, while sending
            to the left is like adding. So if we are moving pieces to the
            right, we set pos_or_neg to -1 for subtraction."""
        if on_left: pos_or_neg = -1

        """Loop checks to see if sending 1 missionary is a valid move,
            and then checks to see if sending 2 missionaries is a valid move"""
        for x in range(1, 3):
            if self.within_bounds(miss, x*pos_or_neg):
                if not self.cann_outnumber_miss(miss + x*pos_or_neg, cann):
                    possible_actions.append(action.ljust(x, "M"))
        
        """Loop checks to see if sending 1 cannibal is a valid move,
            and then checks to see if sending 2 cannibals is a valid move"""
        for x in range(1,3):
            if self.within_bounds(cann, x * pos_or_neg):
                if not self.cann_outnumber_miss(miss, cann + x*pos_or_neg):
                    possible_actions.append(action.ljust(x, "C" ))
        
        #checks to see if sending 1 cannibal and 1 missionary is a valid move
        if self.within_bounds(cann, pos_or_neg) and self.within_bounds(miss, pos_or_neg):
            if not self.cann_outnumber_miss(miss + pos_or_neg, cann + pos_or_neg):
                possible_actions.append("MC")
        
        return possible_actions

    #determines a new state given an action to take
    def result(self, state, action):
        new_state = list(state)
        on_left = state[2]
        pos_or_neg = 1


        if on_left : pos_or_neg = -1

        "MC"
        """If we encounter an M in action, we subtract 1 from the current amount of
            M if the boat is to go right, and we add 1 if the boat is to go
            left. We do the same for Cs.
        """
        for char in action:
            if char == 'M': new_state[0] += pos_or_neg
            if char == 'C': new_state[1] += pos_or_neg

        #set the new location of the boat
        new_state[2] = not new_state[2]

        return tuple(new_state)

    
    #returns True if current state is equal to the goal state
    def goal_test(self, state):
        return state == self.goal

    def fancy_print(self, state):
        temp = "" #string to help us build our output
        state_list = list(state) #converting state to list

        #printing out missionaries and cannibals on the left
        print( temp.ljust(state_list[0], 'M') + " " + temp.ljust(state_list[1], 'C'), end="")
        
        #printing out whether boat is on left
        if state_list[2]: print(" " + "(B)", end="")

        #printing out the water
        print(" ~~~ ", end="")
 
        #printing out the missionaries and cannibals on the right
        print( temp.ljust(3 - state_list[0], 'M') + " " + temp.ljust(3 - state_list[1], 'C'), end="")

        #printing out whether the boat is on the right
        if not state_list[2]: print(" " + "(B)", end="")

        #printing out newline (python automatically does that with print)
        print("")
        


if __name__ == '__main__':
    initial_state = (3, 3, True)
    new_state = initial_state
    misscann = MissCannibals(initial_state)
    path = depth_first_graph_search(misscann).solution()

    misscann.fancy_print(initial_state)
    for item in path:
        new_state = misscann.result(new_state, item)
        misscann.fancy_print(new_state)



