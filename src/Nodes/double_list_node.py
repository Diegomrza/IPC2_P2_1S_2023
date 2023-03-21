class double_list_node:
    def __init__(self, id):
        self.__id = id

        # These are always include
        self.__next = None  # Siguiente
        self.__previous = None  # Anterior
        self.__access = None  # Acceso

    # Getters
    def get_id(self):
        return self.__id

    def get_next(self):
        return self.__next

    def get_previous(self):
        return self.__previous

    def get_access(self):
        return self.__access

    # Setters
    def set_id(self, id):
        self.__id = id

    def set_next(self, next):
        self.__next = next

    def set_previous(self, previous):
        self.__previous = previous

    def set_access(self, access):
        self.__access = access
