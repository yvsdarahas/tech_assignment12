# Pulling the python image
FROM python:3-slim

# Switching the working directory
WORKDIR /flask_app

# Copying the required files
ADD exgRates.csv app.py /flask_app/

# Installing the dependencies and packages
RUN pip install --root-user-action=ignore Flask

# Excecuting the command
CMD ["python3", "app.py"]