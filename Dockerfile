FROM python:3.6.5-slim

# set the working directory in the container to /app
WORKDIR /app

# add the current directory to the container as /app
ADD . /app

# execute everyone's favorite pip command, pip install -r
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install requests
RUN pip install beautifulsoup4
RUN pip install pymongo
RUN pip install telegram
RUN pip install python-telegram-bot
# unblock port 80 for the Flask app to run on
EXPOSE 5003

# execute the Flask app
CMD ["python", "app.py"]
