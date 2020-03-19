# encoding: utf-8
"""
@author: Cheng Wang
@date: 2019/10/17
@last modified: 2019/10/17
"""

# usage: python line_chart.py path/to/log


import os
import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.append('..')

from usage_of_matplotlib.main import plot_xyy


def parse_log(filepath):
    print("locate in %s"%filepath)
    log = open(filepath)

    x = []
    y = []

    lines = log.readlines()
    last_epoch = 120
    y1, y2, y3 = [], [], []
    loss_tri, loss_xent, misclassify = [], [], []

    for line in lines:
        if line.find('loss_tri') != -1:
            start = line.find('e:') + 2
            end = start+3
            epoch = int(line[start:end])
            if epoch != last_epoch:
                # print(epoch)
                last_epoch = epoch
                y1.append(sum(loss_tri) / len(loss_tri))
                y2.append(sum(loss_xent) / len(loss_xent))
                y3.append(sum(misclassify) / len(misclassify))
                loss_tri, loss_xent, misclassify = [], [], []
            # print(epoch)

            start = line.find('loss_tri') + 9
            end = line.find('loss_weight_decay') - 1
            loss_tri.append(float(line[start:end]))
            # print(loss_tri)

            start = line.find('loss_xent') + 10
            end = line.find('misclassify') - 1
            loss_xent.append(float(line[start:end]))
            # print(loss_xent)

            start = line.find('misclassify') + 12
            misclassify.append(float(line[start:]))
            # print(misclassify)

    y1.append(sum(loss_tri) / len(loss_tri))
    y2.append(sum(loss_xent) / len(loss_xent))
    y3.append(sum(misclassify) / len(misclassify))

    return y1, y2, y3


def plot_log(x, y, output_dir):
    plt.plot(x, y)
    plt.title('loss curve')
    plt.xlabel('Iteration')
    plt.ylabel('loss')

    # plt.show()
    save_path = os.path.join(output_dir, "loss_curve.jpg")
    plt.savefig(save_path)
    print("save as %s"%save_path)


if __name__ == '__main__':
        path_to_logs = ['worklog.txt', 'fine.txt']
        baseline_tri, baseline_xent, baseline_mis = parse_log(path_to_logs[0])
        fine_tri, fine_xent, fine_mis = parse_log(path_to_logs[1])
        x = [i for i in range(120, 301)]
        plot_xyy(x, baseline_tri, fine_tri, labely='triplet_loss', output_name='tri.eps')
        plot_xyy(x, baseline_xent, fine_xent, labely='xent_loss', output_name='xent.eps')
        plot_xyy(x, baseline_mis, fine_mis, labely='misclassify', output_name='misclassify.eps')
