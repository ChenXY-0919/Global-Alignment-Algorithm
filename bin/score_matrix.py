class ScoreMatrix:
    def __init__(self, gap=-5):
        self.__rowname = []
        self.__colname = []
        self.__matrix = []
        self.__dataframe = []
        self.gap = gap

    def input_matrix(self, filename):
        from copy import deepcopy
        file = open(filename)
        a = file.read()
        a = a.split("\n")
        for i in range(len(a)):
            a[i] = a[i].split(",")
        self.__dataframe = deepcopy(a)
        self.__colname = a[0]
        del a[0]
        for k in range(len(a)):
            self.__rowname.append(a[k][0])
            del a[k][0]
        self.__matrix = deepcopy(a)
        for i in range(len(self.__matrix)):
            for j in range(len(self.__matrix[i])):
                self.__matrix[i][j] = eval(self.__matrix[i][j])

    def get_matrix(self):
        return self.__matrix

    def get_rowname(self):
        return self.__rowname

    def get_colname(self):
        return self.__colname

    def print_dataframe(self):
        self.__dataframe[0].insert(0, " ")
        for k in self.__dataframe[0]:
            print(format(k, "5s"), end="")
        print("\n")
        for i in range(1, len(self.__dataframe)):
            print(format(self.__dataframe[i][0], "5s"), end="")
            for j in range(1, len(self.__dataframe[i])):
                print(format(self.__dataframe[i][j], "5s"), end="")
            print("\n")

    def get_element(self, row_index, col_index):
        return self.__matrix[self.__rowname.index(row_index)][self.__colname.index(col_index)]
