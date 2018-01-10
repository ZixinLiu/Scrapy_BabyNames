scrapy crawl babyName -o BabyName_output.json
scrapy crawl decade -o decade_century.json
scrapy crawl popularity -o popularity.json
scrapy crawl state -o state.json
scrapy crawl state_top_5 -o state_top_5.json
scrapy crawl territory -o territory.json
scrapy crawl top_1000 -o top_1000.json
scrapy crawl top_5 -o top_5.json
python script/merge.py
