import Student as st

def loadData():
    write_fp = open("average.txt", "w",encoding = "utf8")
    for line in lines:
        tokens = line.strip().split(",")
        name = tokens[0]
        student = st.Student(float(tokens[1]), float(tokens[2]),float(tokens[3])) 
        line = f"{name}의 평균 점수는 {student.get_average()}입니다."
        print(line)
        write_fp.write(str(line)+"\n")
        scores[str(tokens[:1])] = tuple(tokens[1:]) 
    write_fp.close()
    

lines = open("students.csv","r", encoding="utf8").readlines()
del(lines[:1]) 
# TODO 1: 학생 정보를 딕셔너리에 저장
# TODO 2: 학생 별 평균 점수를 계산
scores={}
print("-----학생들의 평균 점수-----")
loadData()



