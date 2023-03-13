from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from typing import List

import requests
from bs4 import BeautifulSoup
import urllib.request

app = FastAPI()

def web_scrap():
    
    response = requests.get("https://en.wikipedia.org/wiki/Spider-Man")
    soup = BeautifulSoup(response.content, 'html.parser')
    infobox = soup.find("table", {"class": "infobox"}).tbody
    personal_info_rows = infobox.find_all("tr")[2:14]
    image_url = "https://upload.wikimedia.org/wikipedia/en/2/21/Web_of_Spider-Man_Vol_1_129-1.png"
    urllib.request.urlretrieve(image_url, "spiderman.png")

    html = f"""
    <html>
        <head>
            <title>Spider-Man Personal Information</title>
        </head>
        <body>
            <h1>Spider-Man Personal Information</h1>
            <img src="spiderman.png" alt="Spider-Man">
            <table>
                <thead>
                    <tr>
                        <th>Field</th>
                        <th>Value</th>
                    </tr>
                </thead>
                <tbody>
    """
    for row in personal_info_rows:
        th = row.find("th").text.strip()
        td_elem = row.find("td")
        td = td_elem.text.strip() if td_elem is not None else ""
        html += f"""
            <tr>
                <td>{th}</td>
                <td>{td}</td>
            </tr>
        """
    html += """
                </tbody>
            </table>
        </body>
    </html>
    """
    return html

@app.get("/", response_class=HTMLResponse)
async def root():
    return web_scrap()
