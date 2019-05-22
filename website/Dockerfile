# Python Runtime
FROM python:3.5

# Setup Work Directory
WORKDIR /usr/website

# Copy files into app
COPY . .

# Install Requirements
RUN python3 -m pip install --trusted-host pypi.python.org -r requirements.txt

# Command executed when container launches
CMD ["python3", "-u", "start_website.py"]