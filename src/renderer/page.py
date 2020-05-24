import time
from threading import Thread

from selenium import webdriver


class Page:
    """
    Class that represents rendered web page
    """
    chromedriver_path = '../renderer/chromedriver_win32/chromedriver.exe'
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument("--window-size=1280,800")
    driver = webdriver.Chrome(chromedriver_path, chrome_options=chrome_options)

    def __init__(self, url):
        """
        Renders web page located at given url

        :param url: url of the web page that needs to be rendered
        :type url: str
        """
        self.url = url
        self.shutdown = False

        thread = Thread(target=self.start_timer, args=(10,))
        thread.start()
        Page.driver.get(url)
        self.shutdown = True
        thread.join()

        self.html = Page.driver.page_source

    @staticmethod
    def change_driver():
        """
        Change chromedriver to a new instance
        """
        Page.driver = webdriver.Chrome(Page.chromedriver_path,
                                       chrome_options=Page.chrome_options)

    def start_timer(self, timeout):
        """
        After a given timeout shuts down previous driver and changes it to a new one

        :param timeout: timeout in secs after which driver will be changed
        :type timeout: int
        """
        start_time = time.time()
        while time.time() - start_time < timeout:
            if self.shutdown:
                return
            time.sleep(1)

        Page.driver.quit()
        Page.change_driver()

    @staticmethod
    def click(element):
        """
        Clicks on the given element even if its not visible in the browser window

        :param element: element to click on
        :type element: selenium.WebElement
        """
        Page.driver.execute_script("arguments[0].click();", element)
