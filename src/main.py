import random
from Structures.matrix import matrix
from Graph.graph import graph

# funcion para generar numeros aleatorios
def random_number():
    return random.randint(0, 100)

if __name__ == "__main__":
    m = matrix()
    for i in range(5):
        for j in range(5):
            num1 = random_number()
            num2 = random_number()
            message = f"Num 1 = {num1} & Num 2 = {num2}"
            print(message)
            m.insert(num1,num2)

    # m.insert(1,1)
    # m.insert(2,1)
    # m.insert(3,1)

    m.show_rows()
    g = graph()
    g.matrix(m, 'report', 'grafo')
