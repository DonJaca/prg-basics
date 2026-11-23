###
# Prints test statistics
#
test_results = [
    False, True, False, True, True,
    True, True, False, True, True,
    False, True, True, True, False
]

# calculates the number of test questions
question_umber = len(test_results)

# calculates the number of correct answers
correct_answers = 0
for answer in test_results:
    if answer == True:
        correct_answers +=1
# calculates the number of incorrect answers
not_correct_answers = 0
for answer in test_results:
    if answer == False:
        not_correct_answers +=1

# calculates the percentage of correct answers
print((correct_answers/len(test_results))*100,end="%")
print('TEST STATISTICS')
print('===============')
print('Number of questions:', question_umber)
print('Number of correct answers:', correct_answers)
...
...