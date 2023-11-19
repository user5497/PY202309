class Student():
    kor = 0
    math = 0
    en = 0

    def get_average(self):
        return (self.kor+self.math+self.en)/3


def loadData():
    for line in lines:
        tokens = line.strip().split(",")
        name = Student() 
        name.kor = float(tokens[1])
        name.math = float(tokens[2])
        name.en = float(tokens[3])
        print(name.get_average())

        scores[str(tokens[:1])] = tuple(tokens[1:]) 





def getAverage():
    write_fp = open("average.txt", "w",encoding = "utf8")
    for name,score in scores.items(): 
        sum = 0
        for num in score: 
             sum += float(num)
        average = sum / len(score) 
        line = (f"{name}의 평균 점수는 {average}입니다.")
        line = line.replace('[','').replace(']','').replace("'", '')
        print(line)
        write_fp.write(str(line)+"\n")
    write_fp.close()
    

lines = open("students.csv","r", encoding="utf8").readlines()
del(lines[:1]) 
# TODO 1: 학생 정보를 딕셔너리에 저장
scores={}
print("-----학생들의 평균 점수-----")
loadData()

# TODO 2: 학생 별 평균 점수를 계산

#getAverage()