from rich.console import Console
from rich.table import Table
from rich import print
from rich.padding import Padding

console = Console()
table = Table (title='filmes de açao',style = 'blue')

table.add_column ('Nome', justify='center', style = 'blue')
table.add_column ('Genero', style = 'green')
table.add_column ('Ano', style = 'yellow')

table.add_row ('Perdido em Marte', 'Ação', '2015')
table.add_row ('Missão Impossível - Nação Secreta', 'Ação', '2015')
table.add_row ('Velozes e Furiosos 7', 'Ação', '2015')
table.add_row ('Vingadores: Guerra Infinita', 'Ficção/Ação', '2018')
table.add_row ('Aquaman', 'Aventura', '2018')


console.print (table)

test = Padding ('Só Salvinho', (3,2), style='on blue', expand=False)
print (test)


