class Add():
    def __init__(self,a=1,b=2):
        self.a=a
        self.b=b

    def add(self):
        return self.a+self.b

if __name__ == '__main__':
    tmp=Add()
    print tmp.add()