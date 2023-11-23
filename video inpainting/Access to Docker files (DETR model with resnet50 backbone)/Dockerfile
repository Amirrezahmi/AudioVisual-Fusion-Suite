# Start from NVIDIA PyTorch image
FROM nvcr.io/nvidia/pytorch:23.10-py3

# Set the working directory
WORKDIR /opt/app

# Install Miniconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && sh Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda \
    && rm Miniconda3-latest-Linux-x86_64.sh

# Add conda to PATH
ENV PATH=/opt/conda/bin:$PATH

# Install ffmpeg
RUN conda install -y -c conda-forge ffmpeg

# Install the missing dependencies for cv2
RUN apt-get update && apt-get install -y libgl1 libsm6 libxext6

# Copy requirements.txt and install Python dependencies
COPY requirements.txt /opt/app/requirements.txt
RUN pip install -r requirements.txt

# Copy Python script
COPY vi.py /opt/app/vi.py

# Set Python to run in unbuffered mode
ENV PYTHONUNBUFFERED=1

# Run the Python script
CMD [ "python", "./vi.py" ]