FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/runacian0221/DjangoPJT.git

WORKDIR /home/DjangoPJT

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN echo "SECRET_KEY=django-insecure-y_njd=lrob!iiz%ahm+(kqkhw1iu3zj4k#-fic7u&&4jsnb7pt" > .env

RUN python manage.py migrate

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["gunicorn", "pragmatic.wsgi", "--bind", "0.0.0.0:8000"]
