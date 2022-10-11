import requests


def get_webpage(url):
    r = requests.get(url)
    r_content = r.json()
    
    # file_html = open("home.html", "w")
    # file_html.write(f'''{r_content}''')


get_webpage('https://www.traderjoes.com/home/products/pdp/autumn-vegetable-and-white-bean-gratin-074901')