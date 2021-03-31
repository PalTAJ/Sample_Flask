FROM python:3.6.9




# copy source code
COPY . /app
WORKDIR /app

# install requirements
RUN pip3 install -r requirements.txt

WORKDIR /app/src

# expose the app port
EXPOSE 5000

#RUN python main.py generate-secret

# run the app server
CMD gunicorn --bind 0.0.0.0:5000 --workers=10 app:app