from yandex_maps_reviews_parser.YandexMapsReviewsParser import YandexMapsReviewsParser


def main():
    parser = YandexMapsReviewsParser()
    organisation_id = parser.get_organization_id('Санкт-Петербург, ресторан Terrassa')
    print("organisation id:", organisation_id)
    reviews = parser.get_reviews_by_organisation_id(organisation_id)
    for ind, review in enumerate(reviews, start=1):
        print(f"review #{ind}:")
        print(review)
        print()


if __name__ == '__main__':
    main()
