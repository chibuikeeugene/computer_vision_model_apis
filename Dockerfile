# Defining our base image for which the application will run
FROM python:3.10

# Set environment variables

# PYTHONDONTWRITEBYTECODE: When set to a non-empty value, Python will 
# not write bytecode (.pyc) files on import. Bytecode files are 
# used by Python to speed up the loading of modules. However, in certain 
# environments like Docker containers, they're not necessary and can clutter the file system.
ENV PYTHONDONTWRITEBYTECODE 1

# When set to a non-empty value, Python will not buffer its standard streams (stdout and stderr). 
# This means that the output from Python processes will be sent directly to the 
# Docker logs without being buffered. This can be useful for debugging and monitoring purposes, 
# as it ensures that logs are immediately available rather than being held in memory.
ENV PYTHONUNBUFFERED 1  

# Set the working directory in the container in which our commands will be run from
WORKDIR /opt/computer-vision-apis/

# Create the user that will run the app
RUN adduser --disabled-password --gecos '' computer-vision-user 


# update and install system dependencies
RUN apt-get update \
    && apt-get install

# Update PATH to include Poetry's bin directory 
ENV PATH="${PATH}:/root/.poetry/bin"


# copy our pneumonia api folder to the container directory
COPY . computer_vision_model_api /opt/computer-vision-apis/

# Copy the poetry.lock and pyproject.toml files
COPY . poetry.lock pyproject.toml /opt/computer-vision-apis/

#  Install Poetry using pip
RUN pip install --no-cache-dir poetry

# Install project dependencies
RUN poetry config virtualenvs.create true \
    && poetry config virtualenvs.in-project true \
    && poetry install

# Grant ownership and permissions to the user for the application directory
RUN chown -R computer-vision-user:computer-vision-user /opt/computer-vision-apis
RUN chmod -R 777 /opt/computer-vision-apis
    
USER computer-vision-user 

EXPOSE 9999

CMD ["poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "9999" ]

