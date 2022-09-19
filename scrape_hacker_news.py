def create_custom_hacker_news(total_pages):  # return stories that have 100 or more points, sorted by points
    import requests
    from bs4 import BeautifulSoup
    import pprint
    from time import time, sleep

    def curate_feed():
        hacker_news = []
        for index, item in enumerate(links):
            points_present = subtext[index].select('.score')
            if points_present:
                points = int(points_present[0].getText().replace(' points', ''))
                if points > 99:
                    title = item.getText()
                    href = item.get('href', None)
                    hacker_news.append({'title': title, 'points': points, 'href': href})
        return sorted(hacker_news, key=lambda k: k['points'], reverse=True)

    links = []
    subtext = []
    final_page = total_pages
    current_page = 0
    while current_page < final_page:
        current_page += 1
        if current_page > 1:  # crawl-delay for website is 30 seconds
            time1 = time()
            time_difference = time1 - time2
            sleep(30 - time_difference)
        response = requests.get('https://news.ycombinator.com/news?p=' + str(current_page))
        if current_page != final_page:
            time2 = time()
        soup = BeautifulSoup(response.text, 'html.parser')
        links = links + soup.select('.titlelink')
        subtext = subtext + soup.select('.subtext')
    pprint.pprint(curate_feed(), sort_dicts=False)


if __name__ == '__main__':
    create_custom_hacker_news(int(input('Enter how many pages of the website you want to sort through: ')))
