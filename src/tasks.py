from config import app, logger


@app.task
def crontab_func1():
    print('在此编写任务要实现的代码')
    logger.info('coding something')


@app.task
def crontab_func2():
    print('在此调用实现了定时任务功能的函数或方法')
    logger.info('coding something again')
