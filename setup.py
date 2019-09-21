f = open("settings.conf", "w")
f.write(raw_input("please enter a path to the folder containing music: "))
system("sudo apt-get install libttspico-utils")
system("sudo apt-get install timidity")
