import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape the website and extract information
def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.find_all('div', class_='col-md-3 col-sm-6 col-xs-12 item-div')

    scraped_data = []

    for item in items:
        title = item.find('h4').text.strip()
        subscribers = item.find('p', class_='item-p').text.strip()
        subscribers = subscribers.replace(' subscribers', '').replace("members", "").replace("subscribers", "").replace(" ", "").replace(",", "")
        image_url = item.find('img')['src']
        channel = item.find('a')['href'].replace('https://tdirectory.me/channel/', 'https://t.me/').replace(".dhtml", "").replace("/channel/","")
        channel_url = "https://t.me/" + channel
        scraped_data.append((title, subscribers, image_url, channel_url))

    return scraped_data

# Function to write data to CSV file
def write_to_csv(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Title', 'Subscribers', 'Image URL', "Channel URL"])
        writer.writerows(data)

# Main function
def main():
    search = input("Enter the search term: ")
    # url = 'https://tdirectory.me/search/kids?sort=relavance#google_vignette'  # Replace 'URL_OF_THE_WEBSITE' with the actual URL
    url = 'https://tdirectory.me/search/' + search + '?sort=relavance#google_vignette'
    data = scrape_website(url)
    write_to_csv(data, 'scraped_data.csv')

if __name__ == '__main__':
    main()
