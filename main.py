from tkinter import Tk,Label
import math

class Board:
    def __init__(self, fen):
        self.board = self.toBoard(fen)
    def toBoard(self,fen):
        board = []
        for v in fen:
            if v=="":
                pass

class Piece:
    def __init__(self,type,color):
        self.type = type
        self.color = color
        self.value = self.getValue(type)
    @staticmethod
    def getValue(type):
        values = {"K":0,"P":1,"N":3,"B":3,"R":5,"Q":9}
        return values[type]

class App(Tk):
    def __init__(self, board:Board):
        super().__init__()
        self.build()
    def build(self):
        self.mainloop()


if __name__=="__main__":
    a = App()