import glob
files = glob.glob("/home/gintas/pyth/files/*.txt")
characters = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
	      "p","q","r","s","t","u","v","w","x","y","z")
charcount = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in files:
    file = open(i,"r")
    while True:
        char = file.read(1)
        if char == '':
            break
        else:
            if char in characters:
                charcount[characters.index(char)] += 1
print charcount
