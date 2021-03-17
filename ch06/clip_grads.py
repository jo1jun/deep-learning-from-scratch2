# coding: utf-8
import numpy as np


dW1 = np.random.rand(3, 3) * 10
dW2 = np.random.rand(3, 3) * 10
grads = [dW1, dW2]
max_norm = 5.0 # threshold


def clip_grads(grads, max_norm):
    total_norm = 0
    for grad in grads:
        total_norm += np.sum(grad ** 2)
    total_norm = np.sqrt(total_norm)

    rate = max_norm / (total_norm + 1e-6)
    if rate < 1: # threshhold 를 초과한 경우
        for grad in grads:
            grad *= rate # 모든 grad 에 rate 곱.


print('before:', dW1.flatten())
print('before2:', dW2.flatten())
clip_grads(grads, max_norm)
print('after:', dW1.flatten())



print('after2:', dW2.flatten())
