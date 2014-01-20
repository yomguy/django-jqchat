from setuptools import setup, find_packages

import jqchat

setup(
    name='django-jqchat',
    author='Richard Barran',
    author_email='richardb...@gmail.com',
    version=".".join(map(str, jqchat.VERSION)),
    url="https://github.com/tomscytale/django-jqchat",
    install_requires=[
        'Django>=1.0',
        'django-timezones',
        'pytz',
        'south',
        ],
    description='An extensible instant messenger thingy for Django',
    packages=find_packages(),
    include_package_data=True,
    zip_safe = False,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
        ],
    )
