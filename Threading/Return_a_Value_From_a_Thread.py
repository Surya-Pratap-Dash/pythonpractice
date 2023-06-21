from threading import Thread
import urllib.request


class HttpRequestThread(Thread):
    def __init__(self, url: str) -> None:
        super().__init__()
        self.url = url
        self.http_status_code = None
        self.reason = None

    def run(self) -> None:
        try:
            response = urllib.request.urlopen(self.url)
            self.http_status_code = response.code
        except urllib.error.HTTPError as e:
            self.http_status_code = e.code
        except urllib.error.URLError as e:
            self.reason = e.reason


def main() -> None:
    urls = [
        'https://natabarpanda.blogspot.com/2023/05/smart-cities-project.html',
        'https://natabarpanda.blogspot.com/2023/05/dbt-data-build-tool-tutorial.html'
    ]

    # create new threads
    threads = [HttpRequestThread(url) for url in urls]

    # start the threads
    [t.start() for t in threads]

    # wait for the threads to complete
    [t.join() for t in threads]

    # display the URLs with HTTP status codes
    [print(f'{t.url}: {t.http_status_code}') for t in threads]


if __name__ == '__main__':
    main()


def main() -> None:
    urls = [
        'https://natabarpanda.blogspot.com/2023/05/smart-cities-project.html',
        'https://natabarpanda.blogspot.com/2023/05/dbt-data-build-tool-tutorial.html'
    ]

    # create new threads
    threads = [HttpRequestThread(url) for url in urls]

    # start the threads
    [t.start() for t in threads]

    # wait for the threads to complete
    [t.join() for t in threads]

    # display the URLs with HTTP status codes
    [print(f'{t.url}: {t.http_status_code}') for t in threads]

