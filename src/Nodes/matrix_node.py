class matrix_node:
    def __init__(self, row, column):
        # These are always include
        self.__row = row  # Fila
        self.__column = column  # Columna

        self.__right = None  # Derecha
        self.__left = None  # Izquierda
        self.__top = None  # Arriba
        self.__bottom = None  # Abajo

    # Getters
    def get_row(self):
        return self.__row

    def get_column(self):
        return self.__column

    def get_right(self):
        return self.__right

    def get_left(self):
        return self.__left

    def get_top(self):
        return self.__top

    def get_bottom(self):
        return self.__bottom

    # Setters
    def set_row(self, id):
        self.__row = id

    def set_column(self, id):
        self.__column = id

    def set_right(self, node):
        self.__right = node

    def set_left(self, node):
        self.__left = node

    def set_top(self, node):
        self.__top = node

    def set_bottom(self, node):
        self.__bottom = node
