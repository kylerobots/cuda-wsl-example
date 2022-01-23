# PyTorch claims to be tied to specific versions of CUDA, so pick on of those
# for now. Test other versions in the future.
FROM nvidia/cuda:11.3.1-cudnn8-runtime-ubuntu20.04

# Install Python and Pip, plus Git to do version control
RUN apt update \
  && DEBIAN_FRONTEND=noninteractive \
  apt install -y --no-install-recommends \
  git \
  python3 \
  python3-pip \
  && rm -rf /var/lib/apt/lists/*

# Install any Python packages from the requirements.txt file.
COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
  && rm -rf /tmp/pip-tmp

CMD [ "nvidia-smi" ]