# Build Environment: Playwright
FROM mcr.microsoft.com/playwright/python:v1.34.3-jammy

# Define the work directory
WORKDIR $HOME/src/

# Add python script to Docker
COPY . $HOME/src/

# Update/Upgrade pip
RUN python -m pip install --upgrade pip

# Install virtualenv
RUN python pip install virtualenv

# Initiate a virtual environment instance named venv
RUN python -m virtualenv venv

# Activate virtual environement
RUN source venv/bin/activate

# Install the contents of requirements.txt
RUN pip install --no-cache-dir -r $HOME/src/requirements.txt

# run playwright install command to install webdrivers and required modules
RUN playwright install

# Run Python script
CMD [ "python", "main.py" ]
