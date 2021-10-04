import os

ip = 200000

autoPush = "n"

for i in range(ip):
	# os.system('git commit --allow-empty -m "New Commit at: $(date)"')
	os.system("git commit --allow-empty -m 'Commit"+ str(i)+"'")	

print("Commited " + str(ip) + " times")

if autoPush == "y":
	os.system('git push')