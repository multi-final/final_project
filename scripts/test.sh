#!/usr/bin/bash


python news_project/manage.py makemigrations --settings=news_project.settings.test
python news_project/manage.py migrate --settings=news_project.settings.test

python news_project/manage.py loaddata data/article.json data/keyword.json data/press.json data/section.json --settings=news_project.settings.test

python news_project/manage.py runserver --settings=news_project.settings.test
