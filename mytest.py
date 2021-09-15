# from search.py import *
# eight_puzzle = EightPuzzle((1, 2, 3, 4, 5, 7, 8, 6, 0))
# if __name__ == '__main__':

#     print(eight_puzzle.find_blank_square((6, 3, 5, 1, 8, 4, 2, 0, 7)))
#     print(eight_puzzle.actions((0, 1, 2, 3, 4, 5, 6, 7, 8))) # DOWN, RIGHT
#     #print(eight_puzzle.result((0, 1, 2, 3, 4, 5, 6, 7, 8), 'DOWN'))
#     #print(eight_puzzle.goal_test((1, 2, 3, 4, 5, 6, 7, 8, 0))) #true
#     #print(eight_puzzle.goal_test((4, 8, 1, 6, 0, 2, 3, 5, 7))) #false
#     #print(eight_puzzle.check_solvability((0, 1, 2, 3, 4, 5, 6, 7, 8)))
#     #print(breadth_first_graph_search(eight_puzzle).solution())
#     #print(depth_first_graph_search(eight_puzzle).solution())


from search import *
eight_puzzle = EightPuzzle((6,3,5,1,8,4,2,0,7))

if __name__ == '__main__' :
    # print(eight_puzzle.find_blank_square((6,3,5,1,8,4,2,0,7)))
    # print(eight_puzzle.actions((0, 1, 2, 3, 4, 5, 6, 7, 8))) # DOWN, RIGHT
    # print(eight_puzzle.result((0, 1, 2, 3, 4, 5, 6, 7, 8), 'DOWN'))
    # print(eight_puzzle.goal_test((1, 2, 3, 4, 5, 6, 7, 8, 0))) #true
    # print(eight_puzzle.goal_test((4, 8, 1, 6,0, 2, 3, 5, 7))) #false
    print(eight_puzzle.check_solvability((6,3,5,1,8,4,2,0,7)))
    print(breadth_first_graph_search(eight_puzzle).solution())
    print("done")
    # print(depth_first_graph_search(eight_puzzle).solution())