import glob
import pygame
pygame.init()
class PaintGraph:
    WIDTH = 629
    HEIGHT = 480
    scale_height = 0
    SCALE_WIDTH = 22
    scale_times = 0
    scale_value = 0.0
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    def init_graph(self,window,height,width,chars,scale_w):
        pygame.draw.line(window, (0, 255, 0), (35, 10), (35, height-25))
        pygame.draw.line(window, (0, 255, 0), (35, height-25), (width-25,
                         height-25))
	font = pygame.font.SysFont(None, 25)
	x = 25
        for char in chars:
	    text = font.render(char, True, (0, 255, 0))
	    x += scale_w
	    window.blit(text,(x,458))
	pygame.display.flip()
    def y_value(self, window, scale_v, scale_t, scale_h):
	font = pygame.font.SysFont(None, 25)
        i = 0
        if scale_t == 0:
            text = font.render(chr(48), True, (0, 255, 0))
	    window.blit(text,(10,445))
	    text = font.render(chr(49), True, (0, 255, 0))
	    window.blit(text,(10,0))
        else:
	    text = font.render("0.0", True, (0, 255, 0))
	    window.blit(text,(0,445))
            while i != scale_t:
		i += 1
		text = font.render(str(scale_v * i), True, (0, 255, 0))
		window.blit(text,(0,445-(scale_h * i)))
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
if max(charcount) > 10:
    graph.scale_height = 44
    graph.scale_times = 10
    graph.scale_value = float(max(charcount))/graph.scale_times
elif max(charcount) == 0:
    graph.scale_height == 0
else:
    graph.scale_height = (graph.HEIGHT -35) / max(charcount)
    graph.scale_times = max(charcount)
    graph.scale_value = 1.0
graph.init_graph(graph.window,graph.HEIGHT,graph.WIDTH,characters,graph.SCALE_WIDTH)
graph.y_value(graph.window, graph.scale_value, graph.scale_times, graph.scale_height)
inp = input("press enter")
        
