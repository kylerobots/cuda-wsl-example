"""
Runs benchmarking both with and without the GPU. Then, outputs the scores and
times of each. This does not run if no GPU is detected.
"""

import time
from ai_benchmark import AIBenchmark
from torch.cuda import is_available

if is_available():
    # Do once for GPU
    gpu_benchmark = AIBenchmark(use_CPU=False, verbose_level=1)
    start_time = time.time()
    gpu_results = gpu_benchmark.run()
    end_time = time.time()
    gpu_duration = end_time - start_time
    # And again for CPU
    # cpu_benchmark = AIBenchmark(use_CPU=True, verbose_level=1)
    # start_time = time.time()
    # cpu_results = cpu_benchmark.run()
    # end_time = time.time()
    # cpu_duration = end_time - start_time
    print(F'GPU score: {gpu_results.ai_score}')
    print(F'\tExecution time: {gpu_duration:.3f} seconds.')
    # print(F'CPU score: {cpu_results.ai_score}')
    # print(F'\tExecution time: {cpu_duration:.3f} seconds.')
else:
    print('No GPU detected, so skipping benchmarks!')
