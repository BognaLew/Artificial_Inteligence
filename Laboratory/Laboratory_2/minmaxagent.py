import copy
import random

from exceptions import AgentException


class MinMaxAgent:
    def __init__(self, my_token='o'):
        self.my_token = my_token

    def decide(self, connect4):
        if connect4.who_moves != self.my_token:
            raise AgentException('not my round')
        else:
            result, move = self.minmax(connect4, 6, True, -10000, 10000)
            print((move))
        return move

    def minmax(self, connect4, depth, maximisation, alfa, beta):
        if connect4.check_game_over():
            if connect4.wins == self.my_token:
                return 1000, 0
            if connect4.wins != self.my_token:
                return -1000, 0
            return 0, 0
        if depth == 0:
            return self.h(connect4), 0
        best_result = -1000
        if maximisation == False:
            best_result = 1000
        best_move = -1
        drops = connect4.possible_drops()
        for i in drops:
            state_copy = copy.deepcopy(connect4)
            state_copy.drop_token(i)
            if maximisation:
                result, move = self.minmax(state_copy, depth-1, False, alfa, beta)
                if result > best_result:
                    best_result = result
                    best_move = i
                alfa = max(alfa, best_result)
            else:
                result, move = self.minmax(state_copy, depth-1, True, alfa, beta)
                if result < best_result:
                    best_result = result
                    best_move = i
                beta = min(beta, best_result)
            if alfa >= beta:
                break

        return best_result, best_move

    def h(self, state):
        result = 0
        center = state.center_column()
        count_o = 0
        count_x = 0
        for i in center:
            if i == "x":
                result += 1
                count_x += 1
            if i == "o":
                result += 1
                count_o += 1
        if state.who_moves == self.my_token and self.my_token == 'o':
            if count_x > 1:
                result -= count_x
            if count_o > 1:
                result += count_o
        else:
            if count_x > 1:
                result += count_x
            if count_o > 1:
                result -= count_o

        return result

