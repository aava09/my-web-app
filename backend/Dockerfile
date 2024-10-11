# Use an official Python runtime as a parent image
FROM --platform=linux/amd64 python:3.8.6

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    unixodbc-dev \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* 


# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install Flask
RUN pip install pyodbc
RUN pip install flask-cors

# Make port 6010 available to the world outside this container
EXPOSE 6010

ENV SERVER_IP='146.148.86.108'
ENV DATABASE_NAME='myappdb'
ENV USERNAME='sqlserver'
ENV PASSWORD='CLFA5D0A11@'

# Run main.py when the container launches
CMD ["python", "main.py"]
