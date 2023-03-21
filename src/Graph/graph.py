from os import startfile, system
import os


class graph:
    def __init__(self):
        self.__count_graph = 0

    def get_count_graph(self):
        return self.__count_graph

    def set_count_graph(self):
        self.__count_graph += 1

    def matrix(self, matrix, path, name):
        string = """digraph G {
        label = "Matriz dispersa"
        node [shape = box]
        subgraph H {
        root [label = "Inicio", group="1"]
        edge [dir="both"]\n
        """

        group = 2

        r = "row"
        c = "column"
        n = "node"

        row_list = []
        column_list = []

        row_traversal = []
        column_traversal = []

        h_row = matrix.get_row_header().get_first()
        h_column = matrix.get_column_header().get_first()

        while h_row != None:
            current = h_row.get_access()
            row_list.append(current)
            aux_list = []

            while current != None:
                aux_list.append(current)
                current = current.get_right()

            row_traversal.append(aux_list)
            h_row = h_row.get_next()

        while h_column != None:
            current = h_column.get_access()
            column_list.append(current)
            aux_list = []

            while current != None:
                aux_list.append(current)
                current = current.get_bottom()

            column_traversal.append(aux_list)
            h_column = h_column.get_next()

        #
        for i in range(len(row_list)):
            aux_row = r + str(row_list[i].get_row())
            # Creation of a row node
            string += aux_row + '[label=' + str(row_list[i].get_row())+',group="1"'+']\n'

            if i < len(row_list) - 1:

                string += r + str(row_list[i].get_row()) + '->' + r + str(row_list[i+1].get_row()) + ';\n'

            aux = row_traversal[i]

            string += r + str(row_list[i].get_row()) + '->' + n + str(aux[0].get_row()) + '_' + str(aux[0].get_column()) + ';\n'
            rank_aux = '{rank=same;' + aux_row + ';'

            for j in range(len(aux)):



                if j < len(aux) - 1:
                    string += n + str(aux[j].get_row()) + '_' + str(aux[j].get_column()) + '->' + n + str(aux[j].get_row()) + '_' + str(aux[j+1].get_column()) + ';\n'


                rank_aux += n + str(aux[j].get_row()) + '_' + str(aux[j].get_column()) + ';'

            string += rank_aux.rstrip(';') + '}\n'
        group = 2
        rank_column = '{rank=same;root;'

        #
        for i in range(len(column_list)):
            aux_column = c + str(column_list[i].get_column())
            string += aux_column + '[label = ' + str(column_list[i].get_column()) + ',group = "' + str(group) + '"]\n'

            rank_column += aux_column + ';'

            aux = column_traversal[i]
            string += aux_column + '->' + n + str(aux[0].get_row()) + '_' + str(aux[0].get_column()) + ';\n'
            for j in range(len(aux)):
                string += n +str(aux[j].get_row()) + '_' + str(aux[j].get_column()) + '[label="'+str(aux[j].get_row())+","+str(aux[j].get_column())+'",group="' + str(group) + '"]\n'
                if j < len(aux) - 1:
                    string += n + str(aux[j].get_row()) + '_' + str(aux[j].get_column()) + '->' + n + str(aux[j+1].get_row()) + '_' + str(aux[j].get_column()) + ';\n'
            group += 1

            if i < len(column_list) - 1:

                string += c + str(column_list[i].get_column()) + '->' + c + str(column_list[i+1].get_column()) + ';\n'
        string += rank_column.rstrip(';') + '}\n'


        string += 'root->' + r + str(row_list[0].get_row()) + ';\n'
        string += 'root->' + c + str(column_list[0].get_column()) + ';\n'

        string += '''}\n}'''

        self.make_dir(path)
        self.graphviz(path+"\\"+name, string)

    def graphviz(self, name, code):
        print(name)
        file = open(name+'.dot', 'w')
        file.write(code)
        file.close()

        system('dot -Tsvg'+' '+name+'.dot -o'+name+'.svg')
        # system('cd ./matriz.png')
        startfile(name+'.svg')

    def make_dir(self, path):
        print(path)
        if not os.path.exists(path):
            os.makedirs(path)