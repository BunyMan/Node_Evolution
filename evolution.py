import linecache

node_to_plot = input("Please insert the number of the node you want to plot: ")
o_line_to_get = int(node_to_plot) + 8
steps_to_plot = input("Please insert the number of FEM.NEU files you want to trace for that node: ")

def o_reader():
    try:
        global o_line
        o_line = linecache.getline("fem.dat", o_line_to_get)
    except:
        print("exception 1")

def o_writer():
    global new_file_name
    new_file_name = "node " + str(node_to_plot) + " evolutions.txt"
    try:
        with open(new_file_name, 'w') as nf:
            nf.write(o_line)
    except:
        print("exception 2")

def s_reader():
    steps_plotted = 0
    while steps_plotted <= int(steps_to_plot):
        steps_plotted += 1
        file_to_get = "FEM" + str(steps_plotted) + ".NEU"
        line_to_get = int(node_to_plot) + 2
        try:
            global line
            line = linecache.getline(file_to_get, line_to_get)
            with open(new_file_name, 'a') as nf:
                nf.write(line)
        except:
            print("exception 3")





o_reader()
o_writer()
s_reader()