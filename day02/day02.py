
import sys
import os

SHAPE_SCORE = {
    "ROCK": 1,
    "PAPER": 2,
    "SCISSORS": 3
}

WIN_LOSE_DRAW_SCORE = {
    "WIN": 6,
    "LOSE": 0,
    "DRAW": 3
}

OPP_MAP = {
    "A": "ROCK",
    "B": "PAPER",
    "C": "SCISSORS"
}

# SHAPE loses too SHAPE
LOSES_TO_MAP = {
    "ROCK": "PAPER",
    "PAPER": "SCISSORS",
    "SCISSORS": "ROCK"
}

# SHAPE wins against SHAPE
WINS_AGAINST_MAP = {
    "ROCK": "SCISSORS",
    "PAPER": "ROCK",
    "SCISSORS": "PAPER"
}

def solution_1(input: str):
    OUR_MAP = {
        "X": "ROCK",
        "Y": "PAPER",
        "Z": "SCISSORS"
    }

    score = 0
    games = input.split("\n") 
    for game in games:
        opp_play = OPP_MAP[game.split(" ")[0]]
        our_play = OUR_MAP[game.split(" ")[1]]
        
        score += SHAPE_SCORE[our_play]

        if opp_play == our_play:
            score += WIN_LOSE_DRAW_SCORE["DRAW"]
        elif our_play == LOSES_TO_MAP[opp_play]:
            score += WIN_LOSE_DRAW_SCORE["WIN"]
        else:
            score += WIN_LOSE_DRAW_SCORE["LOSE"]

    return score

def solution_2(input: str):
    OUR_MAP = {
        "X": "LOSE",
        "Y": "DRAW",
        "Z": "WIN"
    }

    score = 0
    games = input.split("\n") 
    for game in games:
        opp_play = OPP_MAP[game.split(" ")[0]]
        outcome = OUR_MAP[game.split(" ")[1]]

        score += WIN_LOSE_DRAW_SCORE[outcome]
        
        if outcome == "DRAW":
            score += SHAPE_SCORE[opp_play]
        elif outcome == "WIN":
            score += SHAPE_SCORE[LOSES_TO_MAP[opp_play]]
        else:
            score += SHAPE_SCORE[WINS_AGAINST_MAP[opp_play]]


    return score


if __name__ == "__main__":
    is_test = sys.argv[1]
    dir = os.path.dirname(os.path.realpath(__file__))
    file = "test.txt" if eval(is_test.split("=")[1]) else "input.txt"
    
    with open(f'{dir}/{file}', 'r') as infile:
        input = infile.read()

    print("Solution 1:", solution_1(input))
    print("Solution 2:", solution_2(input))

