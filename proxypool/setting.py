# Redis数据库地址
REDIS_HOST = 'DataCrawl-Pool.redis.cache.chinacloudapi.cn'

# Redis端口
REDIS_PORT = 6379

# Redis密码，如无填None
REDIS_PASSWORD = None

REDIS_KEY = 'proxies'

# 代理分数
MAX_SCORE = 100
MIN_SCORE = 0

VALID_STATUS_CODES = [200]

# 代理池数量界限
POOL_UPPER_THRESHOLD = 10000

# 检查周期
TESTER_CYCLE = 20
# 获取周期
GETTER_CYCLE = 20

# 测试API，建议抓哪个网站测哪个
TEST_URL = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=2145291155&containerid=1076032145291155&page=14'

# API配置
API_HOST = '0.0.0.0'
API_PORT = 5555

# 开关
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True
