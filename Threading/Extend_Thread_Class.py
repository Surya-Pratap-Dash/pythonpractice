from threading import Thread
import urllib.request

class HttpRequestThread(Thread):
    def __init__(self, url:str) -> None:
        super().__init__()
        self.url = url

    def run(self):
        print(f'Checking {self.url} ...')
        try:
            response = urllib.request.urlopen(self.url)
            print(response.code)
        except urllib.error.HTTPError as e:
            print(e.code)
        except urllib.error.URLError as e:
            print(e.reason)

def main() -> None:
    urls = [
        'https://natabarpanda.blogspot.com/2023/05/smart-cities-project.html',
        'https://natabarpanda.blogspot.com/2023/05/dbt-data-build-tool-tutorial.html'

    ]

    threads = [HttpRequestThread(url) for url in urls]

    [t.start() for t in threads]

    [t.join() for t in threads]

if __name__ == '__main__':
    main()

