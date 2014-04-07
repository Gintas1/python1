import glob
import sys
import pygame
import string
pygame.init()


class PaintGraph:  # class for gui
    WIDTH = 759
    HEIGHT = 480
    scale_data_value = 0
    scale_height = 0
    SCALE_WIDTH = 22
    scale_times = 0
    scale_value = 0.0
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    def init_graph(self, chars):  # initialized graph with x axis values
        pygame.draw.line(self.window, (0, 255, 0), (35, 10),
                        (35, self.HEIGHT-25))
        pygame.draw.line(self.window, (0, 255, 0), (35, self.HEIGHT-25),
                        (self.WIDTH-155, self.HEIGHT-25))
        font = pygame.font.SysFont(None, 25)
        x = 25
        for char in chars:
            text = font.render(char, True, (0, 255, 0))
            x += self.SCALE_WIDTH
            self.window.blit(text, (x, 458))
        pygame.display.flip()

    def y_value(self):  # method scales and creates y axis values
        font = pygame.font.SysFont(None, 25)
        i = 0
        if self.scale_times == 0:
            text = font.render(chr(48), True, (0, 255, 0))
            self.window.blit(text, (10, 445))
            text = font.render(chr(49), True, (0, 255, 0))
            self.window.blit(text, (10, 0))
        else:
            text = font.render("0.0", True, (0, 255, 0))
            self.window.blit(text, (0, 445))
            while i != self.scale_times:
                i += 1
                text = font.render(str(self.scale_value * i), True,
                                  (0, 255, 0))
                self.window.blit(text, (0, 445-(self.scale_height * i)))
        pygame.display.flip()

    def draw_lines(self, char_c):  # main graph is drawn
        a_coord = (0, 0)
        b_coord = (0, 0)
        x = 25
        for i in char_c.values():
            x += self.SCALE_WIDTH
            a_coord = (x, self.HEIGHT - (i*self.scale_data_value) - 25)
            if b_coord != (0, 0):
                pygame.draw.line(self.window, (0, 255, 0), b_coord, a_coord)
            b_coord = a_coord
        pygame.display.flip()

    def more_info(self, files, chars):  # additional data is provided
        font = pygame.font.SysFont(None, 20)
        text = font.render("Total letters:" + str(sum(chars.values())), True,
                          (0, 255, 0))
        self.window.blit(text, (607, 20))
        text = font.render("Total files:" + str(len(files)), True,
                          (0, 255, 0))
        self.window.blit(text, (607, 35))
        text = font.render("Letter repetitions", True, (0, 255, 0))
        self.window.blit(text, (607, 50))
        y = 50
        for i in chars.keys():
            y += 15
            text = font.render(i + "  " + str(chars[i]), True,
                               (0, 255, 0))
            self.window.blit(text, (607, y))
        pygame.display.flip()


graph = PaintGraph()
input_dir = sys.argv[1]
files = glob.glob(input_dir + "/*.txt")
characters = {}

for i in files:
    file = open(i, "r")
    while True:
        char = file.read(1)
        if char == '':
            file.close()
            break
        elif char.isalpha() and char.lower() in characters:
            characters[char.lower()] += 1
        elif char.isalpha():
            characters[char.lower()] = 1

if max(characters) > 10:  # scaling
    graph.scale_data_value = float((graph.HEIGHT - 35)) / \
        max(characters.values())
    graph.scale_height = 44
    graph.scale_times = 10
    graph.scale_value = float(max(characters.values()))/graph.scale_times
elif max(characters.values()) == 0:
    graph.scale_height == 0
else:
    graph.scale_data_value = float((graph.HEIGHT - 35)) / \
        max(characters.values())
    graph.scale_height = (graph.HEIGHT - 35) / max(characters.values())
    graph.scale_times = max(characters.values())
    graph.scale_value = 1.0

graph.init_graph(characters)
graph.y_value()
graph.draw_lines(characters)
graph.more_info(files, characters)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print event
            sys.exit(0)

