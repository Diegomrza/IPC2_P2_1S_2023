from Nodes.double_list_node import double_list_node

class double_list:
    def __init__(self):
        self.__first = None  # private

    def get_first(self):
        return self.__first

    def set_first(self, node):
        self.__first = node

    def insert(self, node):
        #node = double_list_node(id)

        if self.get_first() == None:
            self.set_first(node)
        elif node.get_id() < self.get_first().get_id():
            node.set_next(self.get_first())
            self.get_first().set_previous(node)
            self.set_first(node)
        else:
            temp = self.get_first()
            while temp.get_next() != None:
                if node.get_id() < temp.get_next().get_id():
                    node.set_next(temp.get_next())
                    temp.get_next().set_previous(node)
                    node.set_previous(temp)
                    temp.set_next(node)
                    break
                elif node.get_id() == temp.get_next().get_id():
                    message = f'The id "{node.get_id()}" already exists'
                    print(message)
                    break
                temp = temp.get_next()

            if temp.get_next() == None:
                temp.set_next(node)
                node.set_previous(temp)

    def delete(self, id):
        temp = self.get_first()
        while temp.get_next() != None:
            if temp.get_id() == id:
                if temp.get_previous() == None:
                    self.set_first(temp.get_next())
                    temp.get_next().set_previous(None)
                else:
                    temp.get_previous().set_next(temp.get_next())
                    temp.get_next().set_previous(temp.get_previous())
                return
            temp = temp.get_next()

        if temp.get_id() == id:
            temp.get_previous().set_next(None)

    def update(self, old_id, new_id):
        temp = self.get_first()
        while temp.get_next() != None:
            if temp.get_id() == old_id:
                temp.set_id(new_id)
                break
            temp = temp.get_next()

    def read(self):
        pass

    def show_list(self):
        temp = self.get_first()
        while temp != None:
            print(temp.get_id())
            temp = temp.get_next()
        print()

    def get_header(self, id):
        aux = self.get_first()
        while aux != None:
            if aux.get_id() == id:
                return aux
            aux = aux.get_next()
        return None
