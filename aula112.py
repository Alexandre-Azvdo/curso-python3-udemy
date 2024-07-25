import importlib 

import aula112_m

print(aula112_m.variavel)

for i in range(10):    
    importlib.reload(aula112_m) # Somente regarregado por necessidade
    print(i)

print('Fim')