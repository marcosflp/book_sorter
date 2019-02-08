FROM python:3.6

ENV PYTHONUNBUFFERED 1

# Create the app folder
RUN mkdir /app

# Set the working directory to /app
WORKDIR /app

# Copy the project book_sorter contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
