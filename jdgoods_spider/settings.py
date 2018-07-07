# -*- coding: utf-8 -*-

# Scrapy settings for jdgoods_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'jdgoods_spider'

SPIDER_MODULES = ['jdgoods_spider.spiders']
NEWSPIDER_MODULE = 'jdgoods_spider.spiders'

MONGO_URL = 'localhost'
MONGO_DB = 'jdgoods_info'
KEYWORD = '猫罐头'
PAGES = 100


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jdgoods_spider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'cookie': '__jdu=1437304873; xtest=862.cf6b6759; qrsc=3; pinId=rmhDM5Fu8LMaM_BVyK91KbV9-x-f3wj7; pin=jd_4af989ebc5e80; unick=%E6%99%93%E6%9A%9D_426; _tp=iLxpp9RFs7NlYZI%2BC5xpMGlpSqnxam3hMQqKMO63L4M%3D; _pst=jd_4af989ebc5e80; areaId=22; ipLoc-djd=22-1930-50944-52191; unpl=V2_ZzNtbUtQEBMlCxJQfRkOBGJRQFgSVEJAJQ8UBH9MXgUwURJZclRCFXwUR1JnGFoUZwAZXEpcQxRFCEZkexhdBGMEE1RCUnMldDhFVEsRbAViARRfQ1JKE3c4dlNLKQddN1xEDxsTE0p1CkVkeildNWczWTNDGkMQdw5EVX4QWgdXAiJe; __jda=122270672.1437304873.1527230431.1528531974.1530936550.5; __jdc=122270672; PCSYCityID=1930; TrackID=1E_PcDEIDWda-ezYaIuyeryAcTMxncyYODP68fYnIh0GkAgWFBLDUwWguJRJmweGPb43996vaU2rLvVrat2KjL17j1jaKt-YtE0JYO0wfw0w; ceshi3.com=103; __jdv=122270672|kong|t_1000560814_|tuiguang|86b7a2e571c04cc4a20da6ca5d31fc15|1530936617960; shshshfpb=21549a6c0fcb040b996018abbc215aa2c53544516117717ccab07b8f10; shshshfp=386c598f273a07df77968d92a1313442; shshshfpa=5131d409-535c-cdba-174e-131697d94eee-1530936644; 3AB9D23F7A4B3C9B=G4LKILW5TDLUOXAVCXX37N3VC4U3SNA5ES67PEL3STBKSHLKQBN74JIGJZX2RX6KFWKZVIAY67XGBSKXDUOJ33YMWY; rkv=V0300; mt_xid=V2_52007VwMXUFtaU18WTxtsBGICFgcOXFJGHE0RXRliV0VQQVBRCEpVG1QNbgMVUQkKWgkZeRpdBW4fE1RBWVRLH0oSXwBsABZiX2hSah9IHVkMbgsUVG1YV1wY; thor=C030EAD5B78A218700E6C3330ED667C83A8E1E0898D9A7F014D8C6AA0FC56A18B7221D140C87C52AF84C40BCA2E67F7500EE845D4371C98A6D40F7788A2D2F6A4521B62EE262A95A10265E4D3A62AFF62487B67FE0B0CCF0AB303D9897A0693C03FDF6A0C9CE907B0DDE48C3E310F7567EE64D1AFE3AA4BAE337BC8E7439D52C80C7D3835B527AC49B199160283ABA59A68DB7CF65A968CCC0A6052EBCCE6025',
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'jdgoods_spider.middlewares.JdgoodsSpiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'jdgoods_spider.middlewares.JdgoodsSpiderDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'jdgoods_spider.pipelines.MongoPipeline': 400,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
