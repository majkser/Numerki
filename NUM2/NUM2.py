import numpy as np
import random

A1 = np.array([[5.8267103432, 1.0419816676, 0.4517861296, -0.2246976350, 0.7150286064], 
               [1.0419816676, 5.8150823499, -0.8642832971, 0.6610711416, -0.3874139415],
               [0.4517861296, -0.8642832971, 1.5136472691, -0.8512078774, 0.6771688230],
               [-0.2246976350, 0.6610711416, -0.8512078774, 5.3014166511, 0.5228116055],
               [0.7150286064, -0.3874139415, 0.6771688230, 0.5228116055, 3.5431433879]
               ])

A2 = np.array([[5.4763986379, 1.6846933459, 0.3136661779, -1.0597154562, 0.0083249547],
                [1.6846933459, 4.6359087874, -0.6108766748, 2.1930659258, 0.9091647433],
                [0.3136661779, -0.6108766748, 1.4591897081, -1.1804364456, 0.3985316185],
                [-1.0597154562, 2.1930659258, -1.1804364456, 3.3110327980, -1.1617171573],
                [0.0083249547, 0.9091647433, 0.3985316185, -1.1617171573, 2.1174700695],
               ])

B = np.array([[-2.8634904630],
              [-4.8216733374],
              [-4.2958468309],
              [-0.0877703331],
              [-2.0223464006]
              ])

x = np.linalg.solve(A1, B)

y = np.linalg.solve(A2, B)

print("wyniki rownanan A1y = B")
print(x)
print("wyniki rownan A2y = B")
print(y)


delta_B = np.random.randn(5, 1)
norm_delta_B = np.linalg.norm(delta_B)
delta_B = (delta_B * 1e-6) / norm_delta_B

B_i_delta_B = B + delta_B

x_2 = np.linalg.solve(A1, B_i_delta_B)

y_2 = np.linalg.solve(A2, B_i_delta_B)

print("wyniki rownan A1y = B + delta_B")
print(x_2)
print("wyniki rownan A2y = B + delta_B")
print(y_2)

print("roznica między wynikami rownan z macierzy A1")
print(x_2 - x)
print("roznica mieszy wynikami rownan z macierzy A2")
print(y_2 - y)