class Worker:
    def __init__(self, surname, status, money):
        self.surname = surname
        self.status = status
        self.money = money
    
    def more_money(self):
        self.money = self.money * 0.15
        print(f"Money was multiply on 15% {self.money}")
    
    def worker_status(self):
        if self.surname.startswith("Іван"):
            self.status = "Engineer"
            print(f"Status of worker was switched on {self.status}")
        else:
            print("No edits")

a = Worker("Іванов", "Teacher", 1500)
b = Worker("Тимофієв", "Baker", 800)

a.more_money()
a.worker_status()

b.more_money()
b.worker_status()