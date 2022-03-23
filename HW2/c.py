'''
Author: Xiang Pan
Date: 2022-03-08 00:58:37
LastEditTime: 2022-03-22 13:43:41
LastEditors: Xiang Pan
Description: 
FilePath: /HW2/c.py
@email: xiangpan@nyu.edu
'''
# adalone dataset
import numpy as np

# plot p_acc_list vs C for each d with subplot
import matplotlib.pyplot as plt
res = acc_res

for i in range(len(res)):
    # plt.figure(figsize=(20,20))
    # plt.subplot(5,10,i+1)
    plt.plot(100 - res[i])
plt.legend(['d=1', 'd=2', 'd=3', 'd=4', 'd=5'])

# plt.plot(p_acc_list)
plt.title('Cross Val Error vs C')
plt.xlabel('C')
plt.ylabel('val_error')
plt.xticks([i for i in range(20)],[f"3e{i}" for i in range(-10, 10)], rotation=40)
# mark max
plt.plot(c_star_index, 100 - res.max(), 'ro')
# max lengend
plt.annotate(f'{c_star}', xy=(c_star_index, res.max()), xytext=(c_star_index+0.5, 100 - res.max()+0.5), arrowprops=dict(facecolor='black', shrink=0.01))
plt.savefig("./images/C3_cross_val_error_vs_d")



for i in range(len(res)):
    # plt.figure(figsize=(20,20))
    # plt.subplot(5,10,i+1)
    plt.plot((100 - res[i])/100))
plt.legend(['d=1', 'd=2', 'd=3', 'd=4', 'd=5'])

# plt.plot(p_acc_list)
plt.title('(Cross Val Error + std) vs C')
plt.xlabel('C')
plt.ylabel('val_error')
plt.xticks([i for i in range(20)],[f"3e{i}" for i in range(-10, 10)], rotation=40)
# mark max
plt.plot(c_star_index, 100 - res.max(), 'ro')
# max lengend
plt.annotate(f'{c_star}', xy=(c_star_index, res.max()), xytext=(c_star_index+0.5, 100 - res.max()+0.5), arrowprops=dict(facecolor='black', shrink=0.01))
plt.savefig("./images/C3_cross_val_error_vs_d")


