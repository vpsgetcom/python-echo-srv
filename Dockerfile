# set base image (host OS)
FROM python:3.6

# set the working directory in the container
RUN mkdir /code
WORKDIR /code

# copy the dependencies file to the working directory
#COPY requirements.txt .
#COPY index.html .

# install dependencies
#RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY src/ .

EXPOSE 4444
# command to run on container start
CMD [ "python", "./echoServer.py" ]