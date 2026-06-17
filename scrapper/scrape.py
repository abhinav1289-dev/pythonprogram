import requests
from bs4 import BeautifulSoup
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Using the Brave/Chrome Agent you suggested
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

url = "https://www.flipkart.com/search?q=mobiles"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

products = []

# LOGIC: Instead of one class, we look for the <a> tag that contains the product link
# These links usually have a predictable structure.
cards = soup.find_all('a', href=True)

for card in cards:
    if '/p/' in card['href']:  # '/p/' indicates a product page link
        # Look for the title inside this card
        title = card.find('div', class_=True) # Finds the first div with a class
        
        # Look for the price (usually starts with ₹)
        # We search the parent of the card to find the price nearby
        parent = card.find_parent('div')
        price_el = parent.find('div', string=lambda s: '₹' in str(s)) if parent else None
        
        if title and price_el:
            price_text = price_el.text.replace('₹', '').replace(',', '').strip()
            products.append({
                'Title': title.text.strip(),
                'Price': price_text,
                'Rating': '4.0' # Default fallback if rating is hidden
            })

# Remove duplicates (since one product might have multiple links)
df = pd.DataFrame(products).drop_duplicates(subset=['Title'])



if not df.empty:
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
    print(f"Successfully found {len(df)} products!")
    
    # Simple Plot
    sns.histplot(df['Price'], bins=12)
    plt.title('Distribution of Mobile Prices')
    plt.show()
else:
    # DEBUG: If still zero, Flipkart might be serving a "Loading" page
    print("Zero products. Let's check the Page Title:")
    print(f"Page Title: {soup.title.text if soup.title else 'No Title Found'}")
    