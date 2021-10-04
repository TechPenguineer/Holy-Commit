import os

ip = int(input("How many times do you want to commit? \n"))

autoPush = input("Auto git push when commited? (y/n) \n")

for i in range(ip):
	# os.system('git commit --allow-empty -m "New Commit at: $(date)"')
	os.system("git commit --allow-empty -m 'Commit"+ str(i)+"'")	

print("Commited " + str(ip) + " times")

if autoPush == "y":
	os.system('git push')