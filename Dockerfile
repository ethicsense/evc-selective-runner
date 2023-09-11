FROM python

WORKDIR .
ADD ./model.tar.gz ./home/

RUN apt-get update && apt-get install -y sudo
RUN chmod +w /etc/sudoers
RUN echo 'irteam ALL=(ALL) NOPASSWD:ALL' | tee -a /etc/sudoers
RUN chmod -w /etc/sudoers
RUN sudo apt-get install -y libgl1-mesa-glx
RUN sudo apt-get install -y python3-pip

# Install Packages
RUN pip install --upgrade pip
RUN pip3 install torch torchvision torchaudio
RUN pip install ultralytics
RUN pip install gradio

RUN ["chmod", "+x", "home/app.py"]
CMD ["home/app.py", "--server_name", "0.0.0.0", "--server_port", "7999"]