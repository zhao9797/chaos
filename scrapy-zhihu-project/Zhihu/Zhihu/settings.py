# -*- coding: utf-8 -*-

# Scrapy settings for Zhihu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Zhihu'

SPIDER_MODULES = ['Zhihu.spiders']
NEWSPIDER_MODULE = 'Zhihu.spiders'


USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"
RANDOM_UA_TYPE = "random"

ROBOTSTXT_OBEY = False


DOWNLOAD_DELAY = 10

COOKIES_ENABLED = False


DOWNLOADER_MIDDLEWARES = {
   'Zhihu.middlewares.RandomProxyMiddleware': 3,
    'Zhihu.middlewares.RandomUserAgentMiddlware': 5,
}


ITEM_PIPELINES = {
   'Zhihu.pipelines.MysqlTwistedPipline': 1,
}


AUTOTHROTTLE_ENABLED = True


SQL_DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
SQL_DATE_FORMAT = "%Y-%m-%d"

MYSQL_HOST = "127.0.0.1"
MYSQL_DBNAME = "zhihuwz"
MYSQL_USER = "root"
MYSQL_PASSWORD = "****"
