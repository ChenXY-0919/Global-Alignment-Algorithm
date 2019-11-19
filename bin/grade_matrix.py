from global_class import GlobalTarget
from score_matrix import ScoreMatrix
from copy import deepcopy
import math


class GradeMatrix:
    def __init__(self):
        self.__rowname = []
        self.__colname = []
        self.__matrix = []
        self.__dataframe = []
        self.__score_matrix = ScoreMatrix()

    def initialize(self, seq1, seq2, score_matrix):
        self.__score_matrix = score_matrix
        a = list(seq1)
        b = list(seq2)
        a.insert(0, "-")
        b.insert(0, "-")
        self.__rowname = a
        self.__colname = b
        c = []
        for i in range(len(b)):
            c.append(GlobalTarget())
        for i in range(len(a)):
            self.__matrix.append(deepcopy(c))
        # initialize line 1 and column 1
        score = 0
        self.__matrix[0][0] = GlobalTarget(score=score)
        score = score + self.__score_matrix.gap
        for i in range(1, len(self.__matrix[0])):
            self.__matrix[0][i] = GlobalTarget(score=score)
            self.__matrix[0][i].state.append("2")
            score = score + self.__score_matrix.gap
        score = 0 + self.__score_matrix.gap
        for j in range(1, len(self.__matrix)):
            self.__matrix[j][0] = GlobalTarget(score=score)
            self.__matrix[j][0].state.append("1")
            score = score + self.__score_matrix.gap

    def calculate_matrix(self, verbose=True):
        max_score = 0
        if verbose:
            print("Now run the main process... it may take a long time...")
        for i in range(1, len(self.__matrix)):
            for j in range(1, len(self.__matrix[i])):
                a = [0, 0, 0]
                a[0] = self.__matrix[i - 1][j].score + self.__score_matrix.gap
                a[1] = self.__matrix[i][j - 1].score + self.__score_matrix.gap
                a[2] = self.__matrix[i - 1][j - 1].score + self.__score_matrix.get_element(
                    row_index=self.__rowname[i],
                    col_index=self.__colname[j])
                state = ["1", "2", "3"]
                max_score = max(a)
                for k in range(len(a)):
                    if a[k] == max_score:
                        self.__matrix[i][j].state.append(state[k])
                self.__matrix[i][j].score = max_score
                self.__matrix[i][j].update()
        return max_score

    def get_sequence(self, verbose=True):
        seq_result_1 = []
        seq_result_2 = []
        quality_result = []
        node = [1]
        k = 0
        while len(node) != 0:
            k = k + 1
            if verbose:
                print("get No.", k, "alignment result......")
            i = len(self.__matrix) - 1
            j = len(self.__matrix[i]) - 1
            node = []
            seq_1 = []
            seq_2 = []
            quality = []
            while i != 0 or j != 0:
                self.__matrix[i][j].update()
                if self.__matrix[i][j].isnode == 1:
                    node.append(self.__matrix[i][j])
                if self.__matrix[i][j].state[0] == "1":
                    seq_1.append(self.__rowname[i])
                    seq_2.append("-")
                if self.__matrix[i][j].state[0] == "2":
                    seq_1.append("-")
                    seq_2.append(self.__colname[j])
                if self.__matrix[i][j].state[0] == "3":
                    seq_1.append(self.__rowname[i])
                    seq_2.append(self.__colname[j])
                if seq_1[-1] == seq_2[-1]:
                    quality.append("|")
                else:
                    quality.append(" ")
                i, j = self.__matrix[i][j].next(i, j)
            seq_result_1.append(deepcopy(seq_1))
            seq_result_2.append(deepcopy(seq_2))
            quality_result.append(deepcopy(quality))
            if len(node) != 0:
                del (node[-1].state[0])
            else:
                break
        return seq_result_1, seq_result_2, quality_result

    def get_matrix(self):
        return self.__matrix

    def get_rowname(self):
        return self.__rowname

    def get_colname(self):
        return self.__colname

    def print_dataframe(self):
        print(format(" ", "5s"), end="")
        for k in self.__colname:
            print(format(k, "5s"), end="")
        print("\n")
        for i in range(len(self.__rowname)):
            print(format(self.__rowname[i], "5s"), end="")
            for j in range(len(self.__matrix[i])):
                print(format(str(self.__matrix[i][j].score), "5s"), end="")
            print("\n")

    def get_element(self, row_index, col_index):
        return self.__matrix[self.__rowname.index(row_index)][self.__colname.index(col_index)]
