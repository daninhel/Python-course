import pyautogui as auto
from datetime import date
import time
#capitura o dia de hoje
data = date.today()
#inicio
auto.alert(text='O programa vai começar,não mexa em nada!', title='', button='OK')
#vai para a pagina anterior
auto.click(591,91)
#seleciona
auto.hotkey('ctrl','a')
#copiar
auto.hotkey('ctrl','c')
#ir para o chrome
auto.hotkey('win','5')
#abrir nova aba com o notion
auto.hotkey('ctrl','t')
auto.write('https://www.notion.so/Python-SENAI-3f25a148f9d24f46a0148a7afcddb9d1')
auto.press('enter')
#criar pag,X:  857 Y:  649
time.sleep(3)
auto.click(857,645)
auto.press('enter')
auto.write('/page')
auto.press('enter')
#colar
time.sleep(2)
auto.write(f'Exercicio do dia {data}')
del data
time.sleep(1)
auto.press('enter')
auto.write('/code')
auto.press('down')
auto.press('enter')
auto.hotkey('ctrl','v')
auto.alert(text='O programa terminou e foi realizado com sucesso.', title='', button='OK')