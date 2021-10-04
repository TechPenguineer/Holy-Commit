import os

ip = 200000
current = 1
targed_to_push = 100
autoPush = "n"


while(ip != -1):
	current = current+1

	if(current==targed_to_push):
		os.system("git push")
		targed_to_push = current+targed_to_push
		print("Pushed")
	# os.system('git commit --allow-empty -m "New Commit at: $(date)"')
	os.system("git commit --allow-empty -m 'Commit"+ str(current)+"'")	

print("Commited " + str(ip) + " times")

if autoPush == "y":
	os.system('git push')