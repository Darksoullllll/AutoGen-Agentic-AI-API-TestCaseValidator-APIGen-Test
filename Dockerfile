FROM python:3.10-slim

# Set work directory inside container
WORKDIR /app

# Copy dependency file into container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files into container
COPY . .

# Default command to run your script
CMD ["python", "app.py"]