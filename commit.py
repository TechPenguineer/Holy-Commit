import os

ip = 200000
current = 1
targed_to_push = 1000
autoPush = "n"


while(ip != -1):
	current = current+1

	if(current==targed_to_push):
		os.system("git push")
		targed_to_push = current+1000
		print("Pushed")
	# os.system('git commit --allow-empty -m "New Commit at: $(date)"')
	os.system("git commit --allow-empty -m 'Commit"+ str(current)+"'")	
	print("Commited " + str(current) + " times\nCurrent Push Target is: " + str(targed_to_push) + "\n\n")


if autoPush == "y":
	os.system('git push')