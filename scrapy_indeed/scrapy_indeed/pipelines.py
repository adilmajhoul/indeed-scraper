import csv

class CsvPipeline:
    def open_spider(self, spider):
        self.file = open('jobs.csv', 'w', newline='')
        self.writer = csv.DictWriter(self.file, fieldnames=['title', 'company', 'location', 'date', 'link'])
        self.writer.writeheader()

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item
