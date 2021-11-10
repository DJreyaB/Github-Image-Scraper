import requests
from bs4 import BeautifulSoup as bs

def image_url_retrieval(url):
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')
    profile_image = soup.find('img', {'alt': 'Avatar'})['src']
    return profile_image


def main():
    github_user = input('What github user would you like to find? ')
    url = f"https://github.com/{github_user}"
    print(image_url_retrieval(url))

if __name__ == '__main__':
    main()