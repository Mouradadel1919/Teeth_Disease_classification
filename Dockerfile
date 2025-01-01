FROM python:3.9-slim

# Set up environment
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY . /app/

# Ensure necessary directories exist
RUN mkdir -p /app/uploads

# Expose Flask app port
EXPOSE 8080

# Run the Flask app
CMD ["python", "app.py"]

