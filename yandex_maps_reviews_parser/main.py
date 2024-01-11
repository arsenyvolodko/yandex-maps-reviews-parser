from yandex_maps_reviews_parser.YandexMapsReviewsParser import YandexMapsReviewsParser


def main():
    parser = YandexMapsReviewsParser()
    organisation_id = parser.get_organization_id('Санкт-Петербург, ресторан Terrassa')
    print(organisation_id)
    reviews = parser.get_reviews_by_organisation_id(organisation_id)
    for review in reviews:
        print(review)


if __name__ == '__main__':
    main()
