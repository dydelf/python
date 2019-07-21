from colorama import init, Fore, Back, Style

init(autoreset=True)

x = Back.GREEN
y = Fore.RED

print(y + x + 'some red text' + Fore.BLACK + 'some black text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')

print('normal text')