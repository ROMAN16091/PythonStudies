# import re
#
# from bs4 import BeautifulSoup, NavigableString


# soup = BeautifulSoup('<b class = "boldest"Extra bold</b>', 'lxml')
# tag = soup.b
# print(tag)
# print(type(tag))
# print(tag.name)
# tag.name = "a"
# print(tag)
# print(tag["class"])
# print(tag.attrs)
# print(tag.attrs.keys())
# tag['class'] = 'new attr'
# print(tag)
# tag['href'] = 'http://example.com'
# print(tag)
# del tag['class']
# print(tag)
# print(tag['class'])
# print(tag.get('class'))
# soup = BeautifulSoup('<p class = "boldest new_class"><a class = "class_a second_a">Extra</a> bold</p>', 'lxml')
# print(soup.a)
# print(soup.a['class'])
# classes_a = soup.a['class']

# soup = BeautifulSoup('<p class = "boldest new_class"><a class = "class_a second_a">Extra</a> bold</p>', 'lxml', multi_valued_attributes = None)
# print(soup.p['class'])

# soup = BeautifulSoup('<p id = "boldest new_class"><a class = "class_a second_a">Extra</a> bold</p>', 'lxml')
# print(soup.p.get_attribute_list('id'))

# soup = BeautifulSoup('<b class = "boldest">Extra bold</b>', 'lxml')

# tag = soup.b
# print(tag.string)
# print(type(tag.string))
# print(tag.text)
# print(type(tag.text))
# tag.replace_with('Replaced Text')
# print(tag)

# doc = BeautifulSoup('<body><p>Some text</p>INSERT FOOTER</body>', 'lxml')
# footer = BeautifulSoup('<footer>Footer</footer>', 'lxml')
# tag_body = doc.body
# tag_body.replace_with(footer)
# print(doc)

# comment_soup = "<p><!--Hello world--></p>"
# soup = BeautifulSoup(comment_soup, "lxml")
# print(soup.p.string)
# print(type(soup.p.string))

# html_doc = """<html><head><title>IT School</title></head>
# <body>
# <p class="title"><b>Students</b></p>
#
# <p class="python">We have three students
# <a href="http://example.com/bob" class="student" id="link1">Bob</a>,
# <a href="http://example.com/alice" class="student" id="link2">Alice</a> and
# <a href="http://example.com/john" class="student" id="link3">John</a>;
# they study.</p>
#
# <p class="python">...</p>
# """
# soup = BeautifulSoup(html_doc, 'lxml')
# print(soup.head)
# print(soup.title)
# print(soup.p)
# print(soup.a)
# print(soup.find_all('a'))
# head_tag = soup.head
# print(head_tag.contents)
# title_tag = head_tag.contents[0]
# print(title_tag.contents)
# print(soup.body.strings)
# for string in soup.body.strings:
#     print(repr(string))

# title_tag = soup.title
# print(title_tag)
# print(title_tag.parent)

# link = soup.a
# print(link.parents)
# for parent in link.parents:
#     print(parent.name)

# siblinig_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></a>",'lxml')
# print(siblinig_soup.b.next_sibling)
# print(siblinig_soup.c.next_sibling)
# print(siblinig_soup.a.next_sibling)
# print(siblinig_soup.c.previous_sibling)

# link = soup.a
# print(link.next_sibling.next_sibling)
# for s in link.next_siblings:
#     print(repr(s))

# print(link.next_element)
# for s in link.next_elements:
#     print(repr(s))




# html_doc = """<html><head><title>IT School</title></head>
# <body>
# <p class="title"><b>Students</b></p>
#
# <p class="python">We have three students
# <a href="http://example.com/bob" class="student" id="link1">Bob</a>,
# <a href="http://example.com/alice" class="student" id="link2">Alice</a> and
# <a href="http://example.com/john" class="student" id="link3">John</a>;
# they study.</p>
#
# <p class="python">...</p>
# """
# soup = BeautifulSoup(html_doc, 'lxml')

# print(soup.find_all('b'))

# for tag in soup.find_all(re.compile('^b')):
#     print(tag.name)

# for tag in soup.find_all(re.compile('t')):
#     print(tag.name)

# def has_class_but_no_id(tag):
#     return tag.has_attr('class') and not tag.has_attr('id')
# print(soup.find_all(has_class_but_no_id))

# def navigable_str(tag):
#     return (isinstance(tag.next_element, NavigableString)) and isinstance(tag.previous_element, NavigableString)
# for tag in soup.find_all(navigable_str):
#     print(tag.name)

# print(soup.find_all(['a','b']))

# print(soup.find_all('title'))
# print(soup.find_all('p', 'title'))
#
# print(soup.find_all('title'))
# print(soup.find_all('p', 'title'))
# print(soup.find_all(id = link2))

# print(soup.find(string=re.compile('students')))

# print(soup.find_all(href = re.compile('bob'), id = 'link1'))

import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
# html = driver.page_source
# with open('index2.html', 'w', encoding='utf-8') as file:
#     file.write(html)
with open('apple.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'New Price', 'Old Price', 'URL'])

    for p in range(1,3):
        url = f'https://rozetka.com.ua/ua/mobile-phones/c80003/page={p};producer=apple/'
        print(f'Load page {p}')
        driver.get(url)
        time.sleep(5)
        items = driver.find_elements(By.CSS_SELECTOR, 'div.item')
        for item in items:
            try:
                title_elem = item.find_element(By.CSS_SELECTOR, 'a.title-title')
                title = title_elem.text
                link = title_elem.get_attribute('href')

                price_elem = item.find_element(By.CSS_SELECTOR, 'div.price-wrap .price')
                price = price_elem.text.strip()

                old_price_elem = item.find_element(By.CSS_SELECTOR, 'div.price-wrap .old-price')
                old_price = old_price_elem.text.strip()

                writer.writerow([title, price, old_price, url])
            except Exception as e:
                print(f'Error: {e}')
                continue
driver.quit()
print('Done!')