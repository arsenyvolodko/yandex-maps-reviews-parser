## YandexMapsReviewsParser

`BeautifulSoup` `selenium` `requests`

### Общее описание

Класс для парсинга отзывов об организации на Yandex maps по названию или по id.

### Usage

1. Активация виртуального окружения и установка зависимостей:
   ```bash
   poetry shell
   poetry install --no-root

2. Для получения отзывов по названию организации необходимо знать ее id.
   Для получения id организации необходимо для начала получить API токен для Яндекс
   карт (https://developer.tech.yandex.ru/ - на странице выберите вариант "API для поиска по организациям")

3. Вставьте токен в файл `consts.py` в переменную `YANDEX_MAPS_API_TOKEN`\
   Теперь можно получить отзывы по названию организации следующим образом:

```python
from yandex_maps_reviews_parser.YandexMapsReviewsParser import YandexMapsReviewsParser

parser = YandexMapsReviewsParser()
organisation_id = parser.get_reviews_by_organisation_name('Санкт-Петербург, ресторан Terrassa')
```

4. Если у вас уже есть id организации, то получать API токен не обязательно. Для получения отзывов об организации по id
   можно воспользоваться следующим кодом:

```python
from yandex_maps_reviews_parser.YandexMapsReviewsParser import YandexMapsReviewsParser

parser = YandexMapsReviewsParser()
reviews = parser.get_reviews_by_organisation_id(1199187387)
```

Функции `get_reviews_by_organisation_id` и `get_reviews_by_organisation_name` возвращают список экземпляров класса Review, содержащих текст отзыва и поставленную пользователем оценку.

5. Обратите внимание, что для корректного получения всех отзывов, которые отображает яндекс (яндекс отображает не более 600 отзывов) необходимо не сворачивать окно с браузером.
