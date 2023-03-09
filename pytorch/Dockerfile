# Set the base image
FROM pytorch/pytorch:latest

# Install additional dependencies
RUN pip install torch-geometric torchvision scikit-learn

# Set the working directory
WORKDIR /app

# Copy the application code into the container
COPY . .

# Set the default command to run when the container starts
CMD ["python", "app.py"]
