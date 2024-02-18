import logging
from logging import handlers



# 日志系统
class Logger(object):
    level_relations = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'crit': logging.CRITICAL
    }  # 日志级别关系映射

    def __init__(self, filename, level='info', msg_level='info',msg='', when='D', backCount=3,
                 fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)

        format_str = logging.Formatter(fmt)  # 设置日志格式
        self.logger.setLevel(self.level_relations.get(level))  # 指定日志级别，低于WARN级别的日志将被忽略

        streamhandler = logging.StreamHandler()  # 往屏幕上输出
        streamhandler.setFormatter(format_str)  # 设置屏幕上显示的格式


     # 实例化TimedRotatingFileHandler
        # interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backCount,encoding='utf-8')  # 往文件里写入#指定间隔时间自动生成文件的处理器
        th.setFormatter(format_str)  # 设置文件里写入的格式


        self.logger.addHandler(streamhandler)  # 把对象加到logger里
        self.logger.addHandler(th)

        ########################按照信息级别进行记录
        if msg_level=="debug":
            self.logger.debug(msg)
        elif msg_level=="info":
            self.logger.info(msg)
        elif msg_level=="error":
            self.logger.error(msg)

        ##############################解决日志中多次重复记录信息，记录前移除之前的 handler 信息
        self.logger.removeHandler(streamhandler)
        self.logger.removeHandler(th)