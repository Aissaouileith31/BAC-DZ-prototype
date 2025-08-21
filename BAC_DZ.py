from flet import *
from home import *
def main(page):
    home(page)
print("ff")
try:
    
        
    app(target=main,assets_dir='assets/')
except Exception as e:
    print(e)    