FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# Install uv
RUN pip install uv

# Copy the requirements files
# Ensure requirements.txt exists and includes streamlit
COPY requirements.txt ./
# If you are using pyproject.toml for dependencies with uv, copy it too
# COPY pyproject.toml ./

# Install dependencies using uv into the system Python environment
# The --system flag tells uv to install packages globally in the container's Python environment
# Make sure 'streamlit' is listed in your requirements.txt
RUN uv pip install --system -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Make port 8501 available to the world outside this container (Streamlit's default port)
EXPOSE 8501

# Define environment variable
ENV PYTHONUNBUFFERED 1

# Run the Streamlit app
# Replace 'main.py' with your actual Streamlit app file if it's different
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
