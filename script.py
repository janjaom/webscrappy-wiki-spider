import requests
from bs4 import BeautifulSoup
import urllib.request

# Make a GET request to the Wikipedia page
response = requests.get("https://en.wikipedia.org/wiki/Spider-Man")

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the infobox that contains the personal information section
infobox = soup.find("table", {"class": "infobox"}).tbody

# Find the table rows that contain the personal information data
personal_info_rows = infobox.find_all("tr")[2:14]

#print(personal_info_rows)

image_url = "https://upload.wikimedia.org/wikipedia/en/2/21/Web_of_Spider-Man_Vol_1_129-1.png"

# Download the image 
urllib.request.urlretrieve(image_url, "spiderman.png")
# Create a new HTML file
with open("spiderman_2.html", "w") as f:
    f.write('<html>\n')
    f.write('  <head>\n')
    f.write('    <title>Spider-Man Personal Information</title>\n')
    f.write('  </head>\n')
    f.write('  <body>\n')
    f.write('    <h1>Spider-Man Personal Information</h1>\n')
    f.write('          <img src="spiderman.png" alt="Spider-Man">\n')
    f.write('    <table>\n')
    for row in personal_info_rows:
        th = row.find("th").text.strip()
        td_elem = row.find("td")
        td = td_elem.text.strip() if td_elem is not None else ""
        f.write('      <tr>\n')
        f.write(f'        <th>{th}</th>\n')
        f.write(f'        <td>{td}</td>\n')
        f.write('      </tr>\n')
    f.write('    </table>\n')
    f.write('  </body>\n')
    f.write('</html>')





