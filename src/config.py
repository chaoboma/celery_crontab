from celery import Celery
from kombu import Exchange, Queue
from loguru import logger


# celery
app = Celery('demo', broker='amqp://guest@localhost:5672//')
# Queue
queue = (
    # 定义专用的queue,定义Exchange,以及与route对应的key
    Queue('queue_demo', Exchange('exchange_demo', type='direct'),
    routing_key='queue_demo_key'),
)
# Route
route = {
    # 定义任务crontab_func1的queue,routing_key
    'tasks.crontab_func1': {'queue': 'queue_demo', 'routing_key': 'queue_demo_key'},
    'tasks.crontab_func2': {'queue': 'queue_demo', 'routing_key': 'queue_demo_key'},
}

# 指定queue和route的配置应用到celery定时任务的配置中,设置时区
app.conf.update(CELERY_QUEUES=queue, CELERY_ROUTES=route, CELERY_TIMEZONE='Asia/Shanghai', CELERY_ENABLE_UTC=False)



logger.add("/mnt/d/test/python/celery_crontab/log_{time:YYYY-MM-DD-HH:mm}.log",
           rotation="20 minutes",  # 每10分钟（设置每天试用周期长了）旋转日志文件
           retention="3 month"  # 保留3个月的日志文件
           )
