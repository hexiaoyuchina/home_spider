# Scrapy settings for home_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'home_spider'

SPIDER_MODULES = ['home_spider.spiders']
NEWSPIDER_MODULE = 'home_spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'home_spider (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 20
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
   'Cookie': 'lianjia_uuid=f65bed5e-0d74-455d-a264-bc5ee4a1327a; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217eeddb4129643-007ef976c92a44-576153e-2073600-17eeddb412ac84%22%2C%22%24device_id%22%3A%2217eeddb4129643-007ef976c92a44-576153e-2073600-17eeddb412ac84%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcn.bing.com%2F%22%2C%22%24latest_referrer_host%22%3A%22cn.bing.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; ke_uuid=8c2c4f0844693e1ed27178beee26be9b; _ga=GA1.2.1359747143.1644668109; select_city=320300; digv_extends=%7B%22utmTrackId%22%3A%22%22%7D; _gid=GA1.2.1795629260.1646656383; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiYTQ5NWJiYjliZGNiNzRiMWFkZWJjNTExNjk4YTgxMWQ3MzZkYmNmYzk2NzQwYjg1ZTg5Zjg3MzlmN2EzYTgzNjJmOTIwN2VhNGNmZGYxNzZhYzA4NTA0MjNkZWEyM2U4NmUyMGE4NzY4NWUzYWIwMmUzY2Q0NzI2MWJkMjQ2ZjIzY2YwOWViNDg1NWEyZTMzZmZiNWRiMDQ5YmRlNDU3YmJmNmMxZDBlM2QwZDgwNzM1MTMxNTEyMDllNGVjNzljMzYwZGM1YWYyZTY2MGE4OTkwNzVjMDYzZDc4NzdlNjljZjczZjEyZDVlOWZkYTRhMDMzMTBhNWUwMDI4ZDg5N1wiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI5ZjUwZjY3YVwifSIsInIiOiJodHRwczovL3h6LmtlLmNvbS8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ==; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1644668781,1646222056,1646655649,1646657294; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1646657294; lianjia_ssid=5deed435-1f36-4d00-8e7e-2e943202611d'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'home_spider.middlewares.HomeSpiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'home_spider.middlewares.HomeSpiderDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'home_spider.pipelines.HomeSpiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
