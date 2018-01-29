grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
# grades = [4, 7, 9, 6, 0, 1]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades: 
        total += grade
    return total
    
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
#     print "Average: " + str(average)
    return average

def grades_variance(scores):
    average = grades_average(scores)
#     print "Average: " + str(average)
#     print "Number of Grades: " + str(len(scores))
    variance = 0
    for score in scores:
        variance = variance + (average - score) ** 2
#         print (average - score) ** 2
    variance = (variance/len(scores))
    return variance

def grades_std_deviation(grades):
    for grade in grades:
        variance = grades_variance(scores)
    return (variance ** 0.5)

print "Grades: " + str(grades)
print "Grade Sum: " + str(grades_sum(grades))
print "Grade Average: " + str(grades_average(grades))
print "Grade Variance: " + str(grades_variance(grades))