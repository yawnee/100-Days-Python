from bs4 import BeautifulSoup
import lxml

with open("website.html",  encoding="utf-8") as file:
    contents = file.read()


soup = BeautifulSoup(contents, 'html.parser')
print(soup.title.string)

# Indents the HTML
#print(soup.prettify())

# Finds the first anchor
print(soup.a)
print("")

# Find the first paragraph, you can change p to anything
print(soup.p)
print("")

# Find all anchor tags
print(soup.find_all(name='a'))
all_anchor_tags = soup.find_all(name='a')
print("")

#Print each anchor tag found
for tag in all_anchor_tags:
    print(tag.getText())
    #print each anchor's URL
    print(tag.get('href'))
print("")

# Find the header1 and ID name
heading = soup.find_all(name='h1', id='name')
print(heading)
print("")

# Find the header3 and class called heading
section_heading = soup.find(name='h3', class_='heading')
print(section_heading.get('class'))
print("")

# Find a paragraph that contains an anachor
company_url = soup.select_one(selector='p a')
print(company_url)
print("")

# Find an id with "name"
id_name = soup.select_one(selector='#name')
print(id_name)
print("")

# This converts all the headings into a list
headings = soup.select('.heading')
print(headings)
