student_scores = input("Input a list of student scores (From number 0 to 100), separated by an space \n").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

max_score = 0
for  score  in student_scores:
  if score > max_score:
    max_score = score
# print(max_score)
print(f"\nThe highest score in the class is: {max_score}")

min_score = 101
for score in student_scores:
  if score <= min_score:
    min_score = score
# print(min_score)
print(f"\nThe minumun score in the class is: {min_score}")