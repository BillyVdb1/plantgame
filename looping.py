class LoopingVariable:
    def __init__(self, bound):
        self.bound = bound
        self.__value = 0
        
        
    @property
    def value(self):
        return self.__value

    def increase(self, amount):
        self.__value = (self.__value + amount)%self.bound

