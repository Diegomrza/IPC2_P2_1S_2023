from Nodes.matrix_node import matrix_node
from Nodes.double_list_node import double_list_node
from Structures.double_list import double_list

class matrix:
    def __init__(self):
        self.__row_header = double_list()
        self.__column_header = double_list()

        self.__count_rows = 0
        self.__count_columns = 0

    # Getters
    def get_row_header(self):
        return self.__row_header
    
    def get_column_header(self):
        return self.__column_header
    
    def get_count_rows(self):
        return self.__count_rows
    
    def get_count_columns(self):
        return self.__count_columns
    
    # Setters
    def set_row_header(self, row_header):
        self.__row_header = row_header

    def set_column_header(self, column_header):
        self.__column_header = column_header

    def set_count_rows(self):
        self.__count_rows += 1

    def set_count_columns(self):
        self.__count_columns += 1

    def insert(self, row, column):
        node = matrix_node(row, column)

        # Rows
        e_row = self.get_row_header().get_header(row)
        if e_row == None:
            e_row = double_list_node(row)
            e_row.set_access(node)
            self.get_row_header().insert(e_row)
            self.set_count_rows()
        else:
            if node.get_column() < e_row.get_access().get_column():
                node.set_right(e_row.get_access())
                e_row.get_access().set_left(node)
                e_row.set_access(node)
            else:
                aux = e_row.get_access()
                while aux.get_right() != None:
                    if node.get_column() < aux.get_right().get_column():
                        node.set_right(aux.get_right())
                        aux.get_right().set_left(node)
                        node.set_left(aux)
                        aux.set_right(node)
                        break
                    elif node.get_column() == aux.get_right().get_column():
                        pass # to change node
                    aux = aux.get_right()
                if aux.get_right() == None:
                    aux.set_right(node)
                    node.set_left(aux)
        
        # Columns
        e_column = self.get_column_header().get_header(column)
        if e_column == None:
            e_column = double_list_node(column)
            e_column.set_access(node)
            self.get_column_header().insert(e_column)
            self.set_count_columns()
        else:
            if node.get_row() < e_column.get_access().get_row():
                node.set_bottom(e_column.get_access())
                e_column.get_access().set_top(node)
                e_column.set_access(node)
            else:
                aux = e_column.get_access()
                while aux.get_bottom() != None:
                    if node.get_row() < aux.get_bottom().get_row():
                        node.set_bottom(aux.get_bottom())
                        aux.get_bottom().set_top(node)
                        node.set_top(aux)
                        aux.set_bottom(node)
                        break
                    elif node.get_row() == aux.get_bottom().get_row():
                        pass # to change node
                    aux = aux.get_bottom()
                if aux.get_bottom() == None:
                    aux.set_bottom(node)
                    node.set_top(aux)
    
    def show_rows(self):
        e_row = self.get_row_header().get_first()
        while e_row != None:
            current = e_row.get_access()
            print("Fila: ",e_row.get_id())
            while current != None:
                print("\tColumna: ", current.get_column())
                current = current.get_right()
            print()
            e_row = e_row.get_next()

    