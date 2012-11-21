from setuptools import setup, find_packages

setup(
    name='django-jqchat',
    version="0.1",
    url="https://github.com/tomscytale/django-jqchat",
    install_requires=[
        'django-timezones',
        'pytz'
        ],
    description='An extensible instant messanger thingy for Django',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
        ],
    )
