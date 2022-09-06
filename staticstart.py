class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1
    def printNumInstances():
        print(f"Number of instances created: {Spam.numInstances}") # Количество созданных экземпляров

X = Spam() # В python3.x можно вызывать функции в классе
Y = Spam() # Вызовам через экземпляры по - прежнему передается self

Spam.printNumInstances()
