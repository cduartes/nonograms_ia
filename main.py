import numpy as np
# cduartes
# mcampusano

if __name__ == "__main__":
    print("---- nonograms ----")
    #read board file (clues)
    lines = [line.rstrip('\n') for line in open('input.txt')]
    dim = eval(lines[0]) #dimension
    h_clues = eval(lines[1]) #horizontal clues
    v_clues = eval(lines[1]) #vertical clues

