import numpy as np

logits = [2.0, 1.0, 0.1]
# logits = [24.0, 25.0, 25.1]
exps = [np.exp(i) for i in logits]
print(exps)
sum_of_exps = sum(exps)
print(sum_of_exps)
softmax = [j/sum_of_exps for j in exps]

print(softmax)
print(np.zeros((2,2)))

print(sum(softmax))