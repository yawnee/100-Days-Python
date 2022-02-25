from bs4 import BeautifulSoup
import lxml
import requests
print("")

# Target the site
response = requests.get('https://news.ycombinator.com/')

# Convert page to HTML
yc_webpage = response.text

# Searches within the HTML and parses the HTML
soup = BeautifulSoup(yc_webpage, 'html.parser')

# Finds the anchor with a class of titlelink
article_tag = soup.find(name='a', class_='titlelink')
print(article_tag)
# Gets ONLY the text value of the anchor tag found above
article_text = article_tag.getText()
print("")

# Gets ONLY the href (URL) of the tag found above
article_link = article_tag.get('href')
print(article_link)
print("")

# Searches for the scoring system and gets the value
article_upvote = soup.find(name='span', class_='score').getText()
print(article_upvote)
print("")
#############################################

# Finds all anchor with a class of titlelink
articles = soup.find_all(name='a', class_='titlelink')
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    link = article_tag.get('href')
    article_links.append(article_link)
    article_texts.append(article_text)

# list comprehensive; same results as above
articles_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name='span', class_='score')]
highest_upvote = max(articles_upvotes)
largest_index = articles_upvotes.index(highest_upvote)

print("")

print(article_texts)
print(article_links)
print(articles_upvotes)
print("")

print(article_texts[largest_index])
print(article_links[largest_index])










