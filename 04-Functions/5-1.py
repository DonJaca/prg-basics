###
# Calculates the final grade for a test based
# on the number of points obtained
#
def pts_to_grade(points):
    grade = ''
    if points >= 18:
        grade = 'Excellent'
    elif(points >=14 and points<18):
        print("Good")
    elif(points >=10 and points<14):
        print("Satisfactory")
    else:
        print("Fail")
    return grade

test_result = 15
final_grade = pts_to_grade(test_result)
print('You scored ... points on the test. Your final grade is ...')