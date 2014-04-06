import glob
import pygame
pygame.init()
class PaintGraph:
    WIDTH = 629
    HEIGHT = 480
    scale_height = 0
    SCALE_WIDTH = 22
    scale_times = 0
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    #print SCALE 
    def init_graph(self,window,height,width,chars,scale_w):
        pygame.draw.line(window, (0, 255, 0), (25, 10), (25, height-25))
        pygame.draw.line(window, (0, 255, 0), (25, height-25), (width-25,
                         height-25))
	font = pygame.font.SysFont("comicsansms", 25)
	x = 25
        for char in chars:
	    text = font.render(char, True, (0, 255, 0))
	    x += scale_w
	    window.blit(text,(x,458))
	pygame.display.flip()
graph = PaintGraph()
files = glob.glob("/home/gintas/pyth/files/*.txt")
characters = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
	      "p","q","r","s","t","u","v","w","x","y","z")
charcount = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in files:
    file = open(i,"r")
    while True:
        char = file.read(1)
        if char == '':
            file.close()
            break
        else:
            if char.lower() in characters:
                charcount[characters.index(char.lower())] += 1
print charcount
if max(charcount) > 10:
    graph.scale_height = 45
    graph.scale_times = 10
elif max(charcount) == 0:
    graph.scale_height == 0
    graph.scale_times = 0
else:
    graph.scale_height = (graph.HEIGHT -35) / max(charcount)
    graph.scale_times = max(charcount)
print graph.scale_height
graph.init_graph(graph.window,graph.HEIGHT,graph.WIDTH,characters,graph.SCALE_WIDTH)
inp = input("press enter")
        
