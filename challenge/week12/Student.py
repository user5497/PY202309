class Student():

    def __init__(self,kor,math,en):
        self.kor = kor
        self.math = math
        self.en = en

    def get_average(self):
        return (self.kor+self.math+self.en)/3
