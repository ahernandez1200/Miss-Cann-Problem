from search import *

class MissCannibals(Problem):
    def __init__(self, initial, goal=(0, 0, False)):
        super().__init__(initial, goal)

    """val is the either the current amount of miss on left,
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
        # print("missionaries is: {}".format(miss))
        # print("cannibals is: {}".format(cann))
        if cann > miss and miss != 0: return True
        if (3-cann) > (3-miss) and (3-miss) != 0: return True

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
                    possible_actions.append([x*pos_or_neg, 0, not on_left])
        
        """Loop checks to see if sending 1 cannibal is a valid move,
            and then checks to see if sending 2 cannibals is a valid move"""
        for x in range(1,3):
            if self.within_bounds(cann, x * pos_or_neg):
                print(self.cann_outnumber_miss(miss, cann + x*pos_or_neg))
                if not self.cann_outnumber_miss(miss, cann + x*pos_or_neg):
                    possible_actions.append([0, x * pos_or_neg, not on_left])
        
        #checks to see if sending 1 cannibal and 1 missionary is a valid move
        if self.within_bounds(cann, pos_or_neg) and self.within_bounds(miss, pos_or_neg):
            if not self.cann_outnumber_miss(miss + pos_or_neg, cann + pos_or_neg):
                possible_actions.append([pos_or_neg, pos_or_neg, not on_left])
        
        return possible_actions
    
    #returns True if current state is equal to the goal state
    def goal_test(self, state):
        return state == self.goal
        




if __name__ == '__main__':
    initial_state = (3, 3, True)
    misscann = MissCannibals(initial_state)
    print(misscann.actions(initial_state))

