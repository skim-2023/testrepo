import requests
import re
import json
from bs4 import BeautifulSoup

# Function to find all the p tags with "class" attributes
def has_class_in_p(tag):
    return tag.has_attr('class')

URL = "https://slack.com/resources"
my_URL = requests.get(URL)
#print(my_URL.status_code)

#print(my_URL.text)
soup = BeautifulSoup(my_URL.text, "html.parser")

#titles = soup.find('a')[0]('data-clog-params')

#print(titles)

data = {}
json_data = json.load(data)


# Find all the p tag with "class" attribute
#soup.find_all("p","c-entry__kicker")
for tag in soup.find_all("p","c-entry__kicker"):
    
    white_paper_category = tag.get_text()
    print(white_paper_category)
    h_tag = tag.next_sibling
    a_tag = soup.find('a')
        #if a_tag['data-clog-params'] is not null:
        #    print(a_tag['data-clog-params'])
        #content = a_tag.select('href')
    print(h_tag.get_text())
    white_paper_name = h_tag.get_text()
    if data[white_paper_category] is null:
        data[white_paper_category] = []
    else:
        data[white_paper_category].append(white_paper_name)
    #json_data.update({white_paper_category:white_paper_name})



print (json.dumps(data, indent=4))
        
        


#for tag in soup.find_all(re.compile('p')):
 #   print(tag.name)

#namelist = soup.find('p',{'class':'c-entry__kicker'})
#print(namelist.get_text())
#for i in namelist:
#        print(i.get_text())


#for sibling in soup.p.contents:
#    print(sibling)
#    break


    
#print(soup.find_all(has_class_in_p))




#for tag in soup.find_all(re.compile('a')):
#    print(tag.text)
    
