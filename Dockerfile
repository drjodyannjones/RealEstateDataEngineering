FROM bitnami/spark:3.5.0

USER root

# Install pip
RUN install_packages python3-pip

# Copy your requirements file into the image
COPY requirements.txt /requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r /requirements.txt

USER 1001
