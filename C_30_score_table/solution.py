class Solution(object):
    def solve(self, inputStr):
        inputList = inputStr.split('\n')
        inputInfo = inputList[0].split()
        studentCount = int(inputInfo[0])
        subjectCount = int(inputInfo[1])
        subjects = inputList[1].split()[:subjectCount]
        students = [s.split() for s in inputList[2:studentCount+2]]
        gradeInfo = []
        for student in students:
            studentGrades = [int(g) for g in student[1:subjectCount+1]]
            gradeInfo.append([student[0]] + studentGrades + [sum(studentGrades)])
        subjectIndex = -1
        if len(inputList) > (studentCount + 2):
            try:
                subjectIndex = subjects.index(inputList[studentCount+2]) + 1
            except:
                pass
        gradeInfo = sorted(gradeInfo, key=lambda x: x[subjectIndex], reverse=True)
        return ' '.join([g[0] for g in gradeInfo])