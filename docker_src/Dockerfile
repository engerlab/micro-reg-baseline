FROM tensorflow/tensorflow:latest-gpu-jupyter

ARG dir_software="/root/Software"

RUN mkdir -p $dir_software \
    && mkdir -p $dir_software/microReg-Baseline \
    && mkdir -p $dir_software/../YourLocalHome

COPY . $dir_software/microReg-Baseline

RUN pip install -r $dir_software/microReg-Baseline/requirements.txt