import requests
from bs4 import BeautifulSoup
import csv
from time import sleep

p = 1
f = open('ebg.csv', 'w', encoding='UTF-8_sig', newline='\n')
csv_f = csv.writer(f)
csv_f.writerow(['დასახელება', 'ფასი'])

while p <= 5:
    url = f'https://ebg.ge/%E1%83%99%E1%83%90%E1%83%A2%E1%83%90%E1%83%9A%E1%83%9D%E1%83%92%E1%83%98/%E1%83%9C%E1%83%9D%E1%83%A3%E1%83%97%E1%83%91%E1%83%A3%E1%83%A5%E1%83%94%E1%83%91%E1%83%98-%E1%83%9C%E1%83%94%E1%83%97%E1%83%91%E1%83%A3%E1%83%A5%E1%83%94%E1%83%91%E1%83%98/?c=175672&p={p}'
    r = requests.get(url)
    text = r.text

    soup = BeautifulSoup(text, 'html.parser')
    full_page = soup.find('div', class_='full_pages')
    wrapper = full_page.find('section', id="wrapper")
    search_product = wrapper.find('section', id='search_product')
    container = search_product.find('div', class_='container')
    div_search = container.find('div', class_='search_product')
    row = div_search.find('div', class_='row ce-row')
    col = row.find('div', class_='col-sm-7 col-md-9')
    search_product_right = col.find('div', class_='search_product_right')
    search_row = search_product_right.find('div', class_='row')
    pull_right = search_row.find('div', class_='col-md-12 pull-right')
    pr_righttwo = pull_right.find('div', class_='pr_right_two')
    search_pr_bar = pr_righttwo.find('div', class_='col-md-12 search_pr_bar')
    search_pr_row = search_pr_bar.find('div', class_='row')
    product_bar = search_pr_row.find('div', class_='product-bar')
    product_one = product_bar.find('div', id='production_one')
    each_box = product_one.find_all('div', {'class': 'col-sm-6 col-md-3 item_ebay'})
    # print(each_box)
    for each in each_box:
        product_item = each.find('div', class_='product_item')
        product_caption = product_item.find('div', class_='productCaption')
        text = product_caption.a.p.text.split()
        delimiter = ' '
        title = delimiter.join(text)
        price_list = product_caption.find('div', class_='product_prime').div.text.split()
        price = price_list[0]
        print(price)
        csv_f.writerow([title, price])
    p += 1
    sleep(10)

f.close()