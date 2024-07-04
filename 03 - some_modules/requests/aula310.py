# HTTP & HTTPS

# Commands: python -m http.server -d some_modules\requests\ 3333
#                                    <path_to_the_folder>   <port>

# Web Scraping (BS4): findigin informations in the web. Read the HTML code in
# object format in python.

    # So... the REQUEST gets the HTML and the BS4 translate, interprets the HTML
    # in an object HTML.


# pip install requests types-requests bs4

# Tutorial -> https://youtu.be/Qd8JT0bnJGs
# + -> https://www.otaviomiranda.com.br/2020/normalizacao-unicode-em-python/

def main() -> None:
    """Function used to run the main code."""
    from bs4 import BeautifulSoup
    import requests
    
    url: str = 'http://localhost:3333/'
    response = requests.get(url)

    # print(type(response)) # => requests.models.Response

    raw_html:str = response.text
    
    # print(raw_html)
    
    parsed_html = BeautifulSoup(raw_html, "html.parser", from_encoding= 'utf-8')

    # print(parsed_html)

    print(parsed_html.title.text) # Navigate in to the classes HTML like an
    # object
    #! To get the precise information u need to 'COPY SELECTORS' in the Inspect
    top_3 = parsed_html.select_one('#top-3 > div > div > header > h2')
    print(top_3.text)

    print('='*100)

    content_portifolio = parsed_html.select_one('#top-3 > div')
    for p in content_portifolio.select('p'):
        text = p.text
        print(text.strip())


if __name__ == '__main__':
    main()