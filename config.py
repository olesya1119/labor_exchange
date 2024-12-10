import os


class Config:
    """Базовые настройки приложения"""
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    DB_NAME = os.getenv('DB_NAME', 'labor_exchange')
    DB_USER = os.getenv('DB_USER', 'postgres')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'postgres')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', 5432)
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    """Настройки для разработки"""
    DEBUG = True


class TestingConfig(Config):
    """Настройки для тестирования"""
    TESTING = True


class ProductionConfig(Config):
    """Настройки для продакшена"""
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    DEBUG = False
