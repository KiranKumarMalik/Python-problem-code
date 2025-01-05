class seq():
    def __init__(self,start, end):
        self.start=start
        self.end=end
    def __iter__(self):
        return self
    def __next__(self):
        if self.start>self.end:
            raise StopIteration
        n=self.start
        self.start+=10
        return n
Obj=seq(10,50)
itob=iter(Obj)
print(itob)
print(list(itob))
print(next(itob))
print(next(itob))
print(next(itob))
print(next(itob))
print(next(itob))