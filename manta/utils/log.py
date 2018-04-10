import logging
from logging import INFO, NOTSET, WARNING, \
                    ERROR, FATAL, CRITICAL, \
                    DEBUG

class Log(object):
    INFO = INFO
    NOTSET = NOTSET
    WARNING = WARNING
    ERROR = ERROR
    FATAL = FATAL
    CRITICAL = CRITICAL
    DEBUG = DEBUG

    _LEVEL = None
    _NAME = ""
    _LOGGER = None
    _FILE_PATH = ""
    _FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    _FORMATTER = None
    _STREAM_LOG = None

    @classmethod
    def _initialize(cls, force=False):
        if cls._LOGGER is None or force:
            cls._LEVEL = cls._LEVEL or logging.INFO
            cls._LOGGER = cls._LOGGER or logging.getLogger(cls._NAME)
            cls._FORMATTER = cls._FORMATTER or logging.Formatter(cls._FORMAT)
            cls._LOGGER.setLevel(cls._LEVEL)

            if not cls._FILE_PATH:
                cls._STREAM_LOG = logging.StreamHandler()
                cls._STREAM_LOG.setFormatter(cls._FORMATTER)
                cls._LOGGER.addHandler(cls._STREAM_LOG)
            else:
                fh = logging.FileHandler(filepath)
                fh.setFormatter(cls._FORMATTER)
                cls._LOGGER.addHandler(fh)

    @classmethod
    def set_log_redirect(cls, filepath, remove_stream_log=True):
        cls._FILE_PATH = filepath
        if remove_stream_log and cls._STREAM_LOG:
            logging.removeHandler(cls._STREAM_LOG)

    @classmethod
    def set_name(cls, name):
        cls._NAME = name

    @classmethod
    def set_level(cls, level):
        cls._LEVEL = level

    @classmethod
    def set_format(cls, fmt):
        cls._FORMAT = fmt

    @classmethod
    def _get_logger(cls):
        cls._initialize()
        return cls._LOGGER

    @classmethod
    def info(cls, msg, *args, **kwargs):
        cls._get_logger().info(msg, *args, **kwargs)

    @classmethod
    def debug(cls, msg, *args, **kwargs):
        cls._get_logger().debug(msg, *args, **kwargs)

    @classmethod
    def error(cls, msg, *args, **kwargs):
        cls._get_logger().error(msg, *args, **kwargs)

    @classmethod
    def warning(cls, msg, *args, **kwargs):
        cls._get_logger().warning(msg, *args, **kwargs)

    @classmethod
    def fatal(cls, msg, *args, **kwargs):
        cls._get_logger().fatal(msg, *args, **kwargs)

    @classmethod
    def critical(cls, msg, *args, **kwargs):
        cls._get_logger().critical(msg, *args, **kwargs)

    @classmethod
    def exception(cls, msg, *args, **kwargs):
        cls._get_logger().exception(msg, *args, **kwargs)