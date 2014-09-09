from distutils.core import setup
import news

setup(
    name='djangocms-news',
    version=news.__version__,
    packages=['news', 'news.migrations'],
    url='https://github.com/h4/djangocms-news',
    license='MIT',
    author='Mikhail Baranov',
    author_email='mkhl@brnv.ru',
    description='News app',
    install_requires=[
        'django-cms>=3.0.0',
        'south>=0.7.2',
        'django-ckeditor-updated>=4.2.8',
        'django-model-utils>=2.0.0',
        'django-filer>=0.9.7',
        'django-hvad>=0.4.1',
        'django-genericadmin>=0.6',
    ],
)
