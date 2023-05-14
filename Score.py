import os
def add_score(DIFFICULTY):
    POINTS_OF_WINNING = (int(DIFFICULTY)  *  3) + 5
    print(POINTS_OF_WINNING*3.5)

    f = open("score.txt" ,'w')
    f.write(f"{POINTS_OF_WINNING}")
    f.close()


