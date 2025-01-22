# Use the official Python image as the base image
FROM python:3.10-slim

# Set the working directory to Demyst in the container
WORKDIR /app/Demyst

# Copy only the requirements file first to leverage Docker's caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the Demyst folder
COPY . /app/Demyst

# Add the fixed_width_parser directory to PYTHONPATH
ENV PYTHONPATH=/app/Demyst/fixed_width_parser

# Automatically execute the desired command on container startup
CMD ["python", "-m", "src.main"]
