# 1
def calculate_gpa():
    gpa_with_score_per = (translate_persentage(score_per)*credit)/credit
    print(gpa_with_score_per)


def translate_letter(score):
    if score == 'A+':
        score1 = 4.3
        return score1
    elif score == 'A':
        score2 = 4.0
        return score2
    elif score == 'A-':
        score3 = 3.7
        return score3
    elif score == 'B+':
        score4 = 3.3
        return score4
    elif score == 'B':
        score5 = 3.0
        return score5
    elif score == 'B-':
        score6 = 2.7
        return score6
    elif score == 'C+':
        score7 = 2.3
        return score7
    elif score == 'C':
        score8 = 2.0
        return score8
    elif score == 'C-':
        score9 = 1.7
        return score9
    elif score == 'D+':
        score10 = 1.3
        return score10
    elif score == 'D':
        score11 = 1.0
        return score11
    elif score == 'D-':
        score12 = 0.7
        return score12


def translate_persentage(score_per):
    if 95 < score_per <= 100:
        score1 = 4.3
        return score1
    elif 90 < score_per <= 94:
        score2 = 4.0
        return score2
    elif 85 < score_per <= 89:
        score3 = 3.7
        return score3
    elif 80 < score_per <= 84:
        score4 = 3.3
        return score4
    elif 75 < score_per <= 79:
        score5 = 3.0
        return score5
    elif 70 < score_per <= 74:
        score6 = 2.7
        return score6
    elif 65 < score_per <= 69:
        score7 = 2.3
        return score7
    elif 60 < score_per <= 64:
        score8 = 2.0
        return score8
    elif 55 < score_per <= 59:
        score9 = 1.7
        return score9
    elif 50 < score_per <= 54:
        score10 = 1.3
        return score10
    elif 45 < score_per <= 49:
        score11 = 1.0
        return score11
    elif 40 < score_per <= 44:
        score12 = 0.7
        return score12


score_letter = input()
score_per = int(input())
credit = int(input())


print(translate_letter(score_letter))
print(translate_persentage(score_per))
calculate_gpa()

file1 = open('D:/Grades/chemistry.txt')
print(file1.read())
file1.close()

file2 = open('D:/Grades/math.txt')
print(file2.read())
file2.close()

file3 = open('D:/Grades/credits.txt')
print(file3.read())
file3.close()

file4 = open('D:/Grades/english.txt')
print(file4.read())
file4.close()

file5 = open('D:/Grades/overall.txt')
print(file5.read())
file5.close()

# API


# SOCKET
