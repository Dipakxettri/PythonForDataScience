class Sum:
    def sumFun(self,*args):
        self.summ = 0
        for nums in args:
            self.summ += nums
        print(self.summ)

sum = Sum()
sum.sumFun(2,2,2,2)
