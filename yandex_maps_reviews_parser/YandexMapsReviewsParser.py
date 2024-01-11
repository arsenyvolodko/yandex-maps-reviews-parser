import requests
import time

from bs4 import BeautifulSoup
from selenium import webdriver, common

from consts import YANDEX_MAPS_API_URL, YANDEX_MAPS_API_TOKEN, URL
from yandex_maps_reviews_parser.Review import Review


class YandexMapsReviewsParser:

    @staticmethod
    def _scroll_to_bottom(driver: webdriver.Chrome) -> None:
        bool_val = True
        last_scroll = -1
        while bool_val:
            scroll_now, scroll_height = driver.execute_script(
                f"""const scroll_element = document.getElementsByClassName('scroll__container')[0]; 
                const speed = 10000;
                scroll_element.scrollBy({{
                    top: 20000,
                    behavior: 'smooth'
                }});
                return [scroll_element.scrollTop, scroll_element.scrollHeight];
                """
            )
            bool_val = scroll_now < scroll_height
            if scroll_now == last_scroll:
                break

            last_scroll = scroll_now
            time.sleep(0.1)

    @staticmethod
    def get_organization_id(organization_name: str) -> int | None:
        response = requests.get(YANDEX_MAPS_API_URL.format(organization_name, YANDEX_MAPS_API_TOKEN))
        if response.status_code != 200:
            raise Exception(f'Bad response code: {response.status_code}')
        if len(response.json()['features']) == 0:
            return None
        return response.json()['features'][0]['properties']['CompanyMetaData']['id']

    def _parse_page(self, driver: webdriver.Chrome, url: str) -> list[Review]:
        res = []
        try:
            driver.get(url)
            self._scroll_to_bottom(driver)
            bs = BeautifulSoup(driver.page_source, 'html.parser')
            full_reviews_info = bs.find_all('div', class_='business-review-view__info')
            for elem in full_reviews_info:
                review_text = elem.find('span', class_='business-review-view__body-text').text
                rate_info = elem.find('div', class_='business-rating-badge-view__stars')
                rate = len(rate_info.find_all('span',
                                              class_='inline-image _loaded icon business-rating-badge-view__star _full _size_m'))
                res.append(Review(rate, review_text))
        except common.exceptions.WebDriverException as e:
            print(f'problems with webDriver, url {url}.\n{e}')
        return res

    def get_reviews_by_organisation_name(self, organization_name: str) -> list[Review]:
        org_id = self.get_organization_id(organization_name)
        if org_id is None:
            print("No such organisations found")
            return []
        with webdriver.Chrome() as driver:
            return self._parse_page(driver, URL.format(org_id))

    def get_reviews_by_organisation_id(self, organization_id: int) -> list[Review]:
        with webdriver.Chrome() as driver:
            return self._parse_page(driver, URL.format(organization_id))
