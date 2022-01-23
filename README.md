# CUDA WSL Example #
This repository shows that the GPU can be used from within a WSL Docker container on Windows. It includes a simple
neural network plus a benchmarking test.

## Setup ##
This feature was introduced into the main Windows build in the Windows 10 21H2 version, so you must have at least that
version. To use the GPU, make sure WSL and Docker are installed:

1. To install WSL, follow this guide: https://docs.microsoft.com/en-us/windows/wsl/install
2. Then install Docker: https://docs.docker.com/desktop/windows/wsl/
3. You can also install VS Code if you want, but the commands will run from Powershell too

Technically, you can also build this container on Linux, but that defeats the purpose.

After installing everything, build the Docker container. This can be done in VS Code or manually on the command line. If
installing manually, make sure the `--gpus=all` argument is set.

**Note:** The version of CUDA is defined in the
*Dockerfile*. You may need to change it based on which GPU you are using. Right now, the default is CUDA 11.3.1, which
works for a GeForce 3080.

## Running ##
There are two examples to run.

***benchmark.py*** runs the [AI Benchmark](https://ai-benchmark.com/alpha) tool on both the GPU and CPU. It then
displays the score and time to run for each version. If the GPU is accessible, there should be a difference. The CPU
part of the code may take some time to run.

***classifier.ipynb*** creates and trains a simple image classifier on the CIFAR10 dataset using PyTorch. It also has
some code that will detect if the GPU is usable and print each GPU it finds. When training, it prints the time it takes
to train. You can explore running it on different devices, but the network is small enough that performance may be
similiar even if run on a CPU.