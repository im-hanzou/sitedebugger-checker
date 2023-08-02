import os
import requests
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore, Style

bl = Fore.BLUE
wh = Fore.WHITE
gr = Fore.GREEN
red = Fore.RED
res = Style.RESET_ALL

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0'}

def screen_clear():
    _ = os.system('cls')

def check_debugbar(url, bar_type, result_file):
    try:
        url = url.strip().replace('\n', '').replace('\r', '')
        if "://" not in url:
            url = "https://" + url
        check = requests.get(url, headers=headers, timeout=3)
        resp = check.text
        if bar_type == "yii-debug-toolbar" and bar_type in resp:
            debug_url = f"{url}/debug/default/index"
            print(f"[{gr}FOUND YII => {debug_url}]{res}\n")
            with open(result_file, "a") as f:
                f.write(f'{debug_url}\n')
        elif bar_type != "yii-debug-toolbar" and bar_type in resp:
            print(f"{gr}[FOUND DEBUG => {url}]{res}\n")
            with open(result_file, "a") as f:
                f.write(f'{url}\n')
        else:
            print(f"{red}[NotFound => {url}]{res}\n")
    except:
        pass

def filter(star):
    bar_types = [
        ("PhpDebugBar.DebugBar", "results/debuglaravel.txt"),
        ("yii-debug-toolbar", "results/debugyii.txt"),
        ("debugbar_loader", "results/debugci.txt")
    ]
    for bar_type, result_file in bar_types:
        check_debugbar(star, bar_type, result_file)

def main():
    print(f'''{gr}[ DEBUDBAR CHECKER ] | [ BY XNXXVIDOES ]''')
    list_file = input(f"{gr}Give Me Your List.txt/{red}R00T> {gr}${res} ")
    with open(list_file, 'r') as f:
        star = f.readlines()
    try:
        thread_pool = ThreadPool(50)
        thread_pool.map(filter, star)
        thread_pool.close()
        thread_pool.join()
    except:
        pass

if __name__ == '__main__':
    screen_clear()
    main()
