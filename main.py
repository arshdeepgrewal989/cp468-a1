import puzzle as pz
from puzzle import goalState, h1, puzzleSolved, h2, initialState, h3, aStar1, aStar2
import copy


def main():
    puzzle_size = int(input(
        "What size of puzzle you want to have? Enter 8, 15 or 24 Please: "))
    # check if user input is 8/15/24, ask for input again if it is not
    while(puzzle_size != 8 and puzzle_size != 15 and puzzle_size != 24):
        puzzle_size = int(input(
            "What size of puzzle you want to have? Enter 8, 15 or 24 Please: "))
    print("You choose {}-puzzle, now it is  time to create the puzzle for you...".format(puzzle_size))
    originalPuzzle = pz.initialState(puzzle_size)
    print("Puzzle created...Show puzzle for you now...")
    # heuristic()

    gameOver = puzzleSolved(originalPuzzle, goalState(puzzle_size))
    j = 0
    # execute 100 different random puzzles
    while (j != 100):
        # deepcopy original puzzle
        puzzle4Execute = copy.deepcopy(originalPuzzle)
        # run three different heuristic functions
        if(not gameOver):
            h1_mt = h1(puzzle4Execute, goalState(puzzle_size))
        # gameOver = False
        # if(not gameOver):
            h2_mt = h2(puzzle4Execute, goalState(puzzle_size))
        # gameOver = False
        # if(not gameOver):
            h3_mt = h3(puzzle4Execute, goalState(puzzle_size))
        # check which heuristic function has least misplaced Tiles
        if (h1_mt < h2_mt < h3_mt):
            smallest_mt = h1_mt
        elif (h2_mt < h1_mt < h3_mt):
            smallest_mt = h2_mt
        elif (h3_mt < h1_mt < h2_mt):
            smallest_mt = h3_mt
        # use heuristic function with shortest path to do A* search
        astar1puzzle = aStar1(
            puzzle4Execute, goalState(puzzle_size), puzzle_size)
        astar2puzzle = aStar2(puzzle4Execute, goalState(
            puzzle_size), puzzle_size, smallest_mt)

        j += 1

    # # format and display the table

    print("Show Table...")
    print("-------------")
    if puzzle_size == 8:
        for i in range(3):
            print("|{}|{}|{}|".format(
                astar1puzzle[i][0], astar1puzzle[i][1], astar1puzzle[i][2]))
    elif puzzle_size == 15:
        for i in range(4):
            print("|{}|{}|{}|{}|".format(
                astar1puzzle[i][0], astar1puzzle[i][1], astar1puzzle[i][2], astar1puzzle[i][3]))
    elif puzzle_size == 24:
        for i in range(4):
            print("|{}|{}|{}|{}|{}|".format(
                astar1puzzle[i][0], astar1puzzle[i][1], astar1puzzle[i][2], astar1puzzle[i][3], astar1puzzle[i][4]))

    print("-------------")
    print("Show Table...")
    print("-------------")
    if puzzle_size == 8:
        for i in range(3):
            print("|{}|{}|{}|".format(
                astar2puzzle[i][0], astar2puzzle[i][1], astar2puzzle[i][2]))
    elif puzzle_size == 15:
        for i in range(4):
            print("|{}|{}|{}|{}|".format(
                astar2puzzle[i][0], astar2puzzle[i][1], astar2puzzle[i][2], astar2puzzle[i][3]))
    elif puzzle_size == 24:
        for i in range(4):
            print("|{}|{}|{}|{}|{}|".format(

    print("-------------")

if __name__ == "__main__":
    main()
