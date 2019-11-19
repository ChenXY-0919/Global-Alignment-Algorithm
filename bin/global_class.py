class GlobalTarget:
    def __init__(self, score=0):
        self.score = score
        self.state = []
        self.isnode = 0
        self.times = 1

    def update(self):
        if len(self.state) > 1:
            self.isnode = 1
        if len(self.state) == 1:
            self.isnode = 0

    def next(self, nrow, ncol):
        if self.state[0] == "1":
            return nrow - 1, ncol
        if self.state[0] == "2":
            return nrow, ncol - 1
        if self.state[0] == "3":
            return nrow - 1, ncol - 1
