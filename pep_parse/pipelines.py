import csv
import datetime as dt

from collections import defaultdict

from pep_parse.constants import BASE_DIR, DATETIME_FORMAT


class PepParsePipeline:

    def open_spider(self, spider):
        self.status_count = defaultdict(int)

    def process_item(self, item, spider):
        status = item['status']
        self.status_count[status] += 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        time_now = dt.datetime.utcnow().strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{time_now}.csv'
        file_path = results_dir / file_name
        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Статус', 'Количество'])
            writer.writerows(self.status_count.items())
            writer.writerow(['Total', sum(self.status_count.values())])
