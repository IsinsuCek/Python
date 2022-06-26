class Worker:
    worker_list = []

    def __init__(self, name, job, salary):
        self.name = name
        self.job = job
        self.salary = salary
        self.worker_list.append(self.name)

    def raise_salary(self, value):
        self.salary += value
    
    def change_job(self, new_job):
        self.job = new_job
    
    def show_income(self):
        print(self.salary)
    
    @classmethod
    def remove_worker(cls, worker_index):
        cls.worker_list.pop(worker_index)

"""c1 = Worker('Ilkay', 'dev', '3000')  
Worker.remove_worker(0)
print(Worker.worker_list)

c1 = Worker('Ilkay', 'dev', '3000')
print(c1.worker_list)
c2 = Worker('Nurcan', 'dev', '3200')
print(c1.worker_list)
"""
class Player: 
    player_list = []

    def __init__(self, player_name):
        self.player_list.append(player_name)

p1 = Player('Burcu', ['self-learner'])
"""print()
print(p1.skill_list)"""

class Graph:
    def __init__(self, graph = {}):
        self.graph = graph
    def set_connection(self, node, neigh):
        self.graph[node] = neigh
    def find_connection_distance(self, src, dest):
        pass

class MyMath:
    def __init__(self, matrix1 = [], matrix2 = []):
        self.matrix1 = matrix1
        self.matrix2 = matrix2

    @staticmethod   
    def sqr_root(self, value):
        return value ** 0.5

m = MyMath()
print(m.sqr_root(16))