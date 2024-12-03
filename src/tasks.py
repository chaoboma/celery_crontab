from config import app, Config


config_obj = Config()

@app.task
def crontab_func1():
    print('在此编写任务要实现的代码')
    config_obj.LOGGER.info('coding something')


@app.task
def crontab_func2():
    print('在此调用实现了定时任务功能的函数或方法')
    config_obj.LOGGER.info('coding something again')
