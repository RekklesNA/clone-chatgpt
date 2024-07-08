# Use the official Python base image
FROM python:3.9-slim
# Set the working directory
WORKDIR /app
# Copy the requirements.txt file to the working directory
COPY requirements.txt /app/
# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt
# Copy the content of the current directory to the working directory
COPY . /app
# Expose the default port for Streamlit
EXPOSE 8501
# Run the application
CMD ["streamlit", "run", "main.py"]