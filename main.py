from gameFile import b, f
from interface import Menus, Account

ac = Account()
menu = Menus(ac)
b.menuVar = menu
menu.mainLoop()
