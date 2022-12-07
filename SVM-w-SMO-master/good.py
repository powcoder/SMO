https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
from SVM import SVM

import numpy as np
model = SVM(max_iter=10000, kernel_type='linear', C=1.0, epsilon=0.000001)

model.fit(np.array([[1, 1], [2,2], [2,0], [2,1], [0, 0], [1,0], [1,1], [-1,-1]]), np.array([1,1,1,1,-1,-1,-1,-1]))


print(model.w)

print(model.b)