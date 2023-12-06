file1 = open('premise.txt', 'r')
Lines1 = file1.readlines()
file2 = open('hypothesis.txt', 'r')
Lines2 = file2.readlines()
file3 = open('label.txt', 'r')
Lines3 = file3.readlines()

file4 = open('modified_train_unsorted.jsonl', 'a+')
for indx in range(1,len(Lines1)):
	file4.write("{ " +Lines1[indx]+","+ Lines2[indx]+ "," + Lines3[indx]+" } \n")
	



