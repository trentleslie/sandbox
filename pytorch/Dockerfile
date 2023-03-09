# Set the base image
FROM pytorch/pytorch:latest

# Install additional dependencies
RUN pip install torch-geometric

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install -r requirements.txt

# Copy the application code into the container
COPY . .

# Set the default command to run when the container starts
CMD ["python", "app.py"]
