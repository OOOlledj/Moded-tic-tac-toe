from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.label import Label

Config.set("graphics","resizable","1")
Config.set("graphics","width","300")
Config.set("graphics","height","300")

choice = ['X', 'O']; switch = 0

class MainApp(App):

    def tic_tac_toe(self, arg):
        global switch

        arg.disabled = True
        arg.text = choice[switch]

        if not switch:
            switch = 1
            self.status.text = 'O Turn'
        else:
            switch = 0
            self.status.text = 'X Turn'
        self.turns+= 1



        coordinate = (
            (0,1,2),(3,4,5),(6,7,8), # X
            (0,3,6),(1,4,7),(2,5,8), # Y
            (0,4,8),(2,4,6),         # D
        )

        vector = (
            [self.button[x].text for x in (0,1,2)],
            [self.button[x].text for x in (3,4,5)],
            [self.button[x].text for x in (6,7,8)],

            [self.button[y].text for y in (0,3,6)],
            [self.button[y].text for y in (1,4,7)],
            [self.button[y].text for y in (2,5,8)],

            [self.button[d].text for d in (0,4,8)],
            [self.button[d].text for d in (2,4,6)],
        )

        win = False
        color = [0,1,0,1] # Green

        for index in range(8):
            if vector[index].count('X') == 3\
            or vector[index].count('O') == 3:
                win = True
                for i in coordinate[index]:
                    self.button[i].color = color
                break

        if win:
            self.status.text = 'WE HAVE WINNER!'
            for index in range(9):
                self.button[index].disabled = True
        elif self.turns == 9:
            self.status.text = 'WOOOPS! Nobody won. Try once more'
        
    def restart(self, arg):
        global switch; switch = 0
        for index in range(9):
            self.turns = 0
            self.button[index].color = [0,0,0,1]
            self.button[index].text = ""
            self.button[index].disabled = False
            self.status.text = 'X starts the game'

    def build(self):
        self.title = "Крестики-нолики"
        
        root = BoxLayout(orientation = "vertical", padding = 6)

        grid = GridLayout(cols = 3)
        self.button = [0 for _ in range(9)]
        for index in range(9):
            self.button[index] = Button(
                    color = [0,0,0,1], #font color
                    font_size = 24,
                    disabled = False,
                    on_press = self.tic_tac_toe
                )
            grid.add_widget(self.button[index])
        root.add_widget(grid)

        root.add_widget(
            Button(
                text = "Restart",
                size_hint = [1,.1],
                on_press = self.restart
            )
        )

        self.turns = 0
        self.status = Label(
                text = 'X Starts the game',
                size_hint=[1, .1]
                )
        root.add_widget(
            self.status
        )

        return root

if __name__ == "__main__":
    MainApp().run()