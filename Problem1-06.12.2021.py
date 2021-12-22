Name=input("Enter your Name: ")
Score1=int(input("Enter your Score1: "))
Score2=int(input("Enter your Score2: "))
Score3=int(input("Enter your Score3: "))
Score_list=[Score1,Score2,Score3]
avg=sum(Score_list)/len(Score_list)
print("Scores Report For: {}".format(Name))
print("score1: {}".format(Score1))
print("score2: {}".format(Score2))
print("score3: {}".format(Score3))
print("Average Score: {}".format(avg))
      









