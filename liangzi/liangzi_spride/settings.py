# liangzi_spride 项目的 Scrapy 设置
#
# 为简单起见，该文件只包含被认为重要或
# 常用的设置。更多设置请查阅文档：
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "liangzi_spride"

SPIDER_MODULES = ["liangzi_spride.spiders"]
NEWSPIDER_MODULE = "liangzi_spride.spiders"


# 通过在用户代理上标明自己（和网站）的身份，负责任地进行抓取
USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'

# 遵守 robots.txt 规则
ROBOTSTXT_OBEY = True

# 配置 Scrapy 执行的最大并发请求数（默认值：16）
CONCURRENT_REQUESTS = 16

# 配置对同一网站请求的延迟（默认值：0）
# 参见 https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# 另请参阅自动节流设置和文档
#DOWNLOAD_DELAY = 3
# 下载延迟设置只支持以下一种情况：
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# 禁用 cookie（默认已启用）
#COOKIES_ENABLED = False

# 禁用 Telnet 控制台（默认已启用）
#TELNETCONSOLE_ENABLED = False

# 覆盖默认请求标头
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# 启用或禁用蜘蛛中间件
# 参见 https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "liangzi_spride.middlewares.LiangziSprideSpiderMiddleware": 543,
#}

# 启用或禁用下载器中间件
# 参见 https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "liangzi_spride.middlewares.LiangziSprideDownloaderMiddleware": 543,
#}

# 启用或禁用扩展名
# 参见 https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# 配置项目管道
# 参见 https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # "liangzi_spride.pipelines.LiangziSpridePipeline": 300,
   # "liangzi_spride.pipelines.hanjuSpridePipeline": 299,
   "liangzi_spride.pipelines.MySqlSpridePipeline": 298,
}

# 启用并配置自动节流扩展（默认已禁用）
# 参见 https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
#初始下载延迟
#AUTOTHROTTLE_START_DELAY = 5
# 在高延迟情况下设置的最大下载延迟
#AUTOTHROTTLE_MAX_DELAY = 60
#Scrapy 应该并行发送给
# 每个远程服务器
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# 启用对收到的每个响应显示节流统计：
#AUTOTHROTTLE_DEBUG = False

# 启用并配置 HTTP 缓存（默认已禁用）
# 参见 https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# 将默认值已过时的设置设置为面向未来的值
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
