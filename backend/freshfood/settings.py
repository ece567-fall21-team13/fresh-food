"""Application configuration."""
import os


class Config(object):
    """Base configuration."""
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))


class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',
                                             'postgresql://localhost/fresh_food?user=postgres&password=postgres')


class DevConfig(Config):
    """Development configuration."""
    ENV = 'dev'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',
                                             'postgresql://localhost/fresh_food?user=postgres&password=postgres')