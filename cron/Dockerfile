# Create Debian
FROM debian

# Working Directory
WORKDIR /usr/app

# Copy files into app
COPY . .

# Commands to Update and Install needs
RUN apt-get -y update
RUN apt-get install -y cron python3 python3-pip
RUN python3 -m pip install --trusted-host pypi.python.org -r requirements.txt

# Crontab setup
ADD crontab /etc/cron.d/pgatour
RUN chmod 0755 /etc/cron.d/pgatour
RUN chmod +x /app/pgaScores.py
RUN crontab /etc/cron.d/pgatour

CMD ["cron", "-f"]