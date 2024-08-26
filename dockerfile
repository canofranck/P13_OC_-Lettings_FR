FROM python:3.11

WORKDIR /app

COPY requirements.txt .

ENV PIP_NO_PROGRESS_BAR=off
RUN pip install --upgrade pip && pip install -r requirements.txt



COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "oc_lettings_site.wsgi:application"]
