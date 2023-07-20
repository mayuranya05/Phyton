score_1 = int(input("Enter the score for test1 :"))
score_2 = int(input("Enter the score for test2 :"))
score_3 = int(input("Enter the score for test3 :"))

average = (score_1 + score_2 + score_3) /3
print("The average score is", average)

if average > 95 and 100 <= average:
    print("Congratulations!")
    print("That is a great average")
