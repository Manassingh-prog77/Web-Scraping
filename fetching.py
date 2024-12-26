import os
from bs4 import BeautifulSoup
import pandas as pd

d = {'imageLinks': []}
# Loop through all files in the "data" directory
for file in os.listdir('data'):
    try:
        # Open and read each file
        with open(f"data/{file}", 'r', encoding='utf-8') as f:
            html_doc = f.read()

            # Parse the HTML content
            soup = BeautifulSoup(html_doc, 'html.parser')

            # Find the first <img> tag
            img = soup.find('img')

            if img and 'src' in img.attrs:
                # Get the 'src' attribute
                src = img['src']
                print(src)
                d['imageLinks'].append(src)
            else:
                print(f"No <img> tag or 'src' attribute found in {file}")
    except Exception as e:
        print(f"Error processing {file}: {e}")

pd.DataFrame(d).to_csv('image_links.csv', index=False)

