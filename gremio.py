import pyautogui as auto
from time import sleep as wait

auto.keyDown('win')
auto.keyDown('r')
auto.keyUp('win')
auto.keyUp('r')

auto.write('chrome')
auto.press('enter')

auto.write('www.youtube.com')
auto.press('enter')

wait(5)
auto.press('tab' , presses= 4)

auto.write('gremio mundial de 1983')
auto.press('enter')

wait(3)
#302,391
auto.click(302, 391)