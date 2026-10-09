class Car:
    def __init__(self,model,color):
        self.model = model
        self.color = color
    class Engine:
        def __init__(self,type,emodel):
            self.type = type
            self.emodel = emodel
        def start(self):
            print("Engine Started")
        def stop(self):
            print("Engine Off")
    def getInfo(self):
        print("Model",self.model)
        print("Color",self.color)            

outer =Car("Toyota","red")
outer.getInfo()
inner = outer.Engine("Electric","Em001")
inner.start()
inner.stop()
