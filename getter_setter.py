class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id_ = id_
        self.name = name
        self.company = company
        self.workers = []

    def add_worker(self, worker):
        if not isinstance(worker, Worker):
            raise TypeError('wrong worker')
        if worker in self.workers:
            raise ValueError('Worker already exists')
        self.workers.append(worker)

    def __repr__(self):
        return f"<Boss: name={self.name}, company={self.company}, workers={self.workers}>"


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id_ = id_
        self.name = name
        self.company = company
        self._boss = boss

    def get_boss(self):
        return self._boss

    def set_boss(self, boss):
        if not isinstance(boss, Boss) and boss is not None:
            raise TypeError('wrong boss')
        self._boss = boss

    boss = property(get_boss, set_boss)

    def __repr__(self):
        return f"<Worker: name={self.name}, company={self.company}>"


boss_1 = Boss(1,'Ilon', 'Tesla')
boss_2 = Boss(2, 'Mark', 'Meta')
rab_1 = Worker(1, 'Bob', 'Tesla', boss_1)
rab_2 = Worker(1, 'Bill', 'Tesla', boss_1)
rab_1.boss = boss_1
print(rab_1.boss.name)
rab_2.boss = boss_2
print(rab_2.boss.name)
boss_1.add_worker(rab_1)
boss_1.add_worker(rab_2)
boss_2.add_worker(rab_2)

print(boss_1.workers)
print(boss_2.workers)

