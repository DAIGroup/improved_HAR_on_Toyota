import numpy as np
import matplotlib.pyplot as plt
import smarthome_classes as cl  # from DAIGroup/i3d repository

# CROSS-VIEW RESULTS
# filename = './results/lstm/cv/confusion_matrix_crossview_lstm_notrans_rot_wc_nods_185.csv'
# filename = './results/i3d/cv/confusion_matrix_cv_rot_wc_nt_2.csv'
# filename = './results/i3d/cv/confusion_matrix_i3d_CV_wc_fullcrop.csv'
# filename = './results/sta/cv/confusion_matrix_sta_CV_rot_cw_nods_21.csv'
# filename = './results/sta/cv/confusion_matrix_sta_CV_rot_wc_fc_18.csv'
# filename = './results/sta/cv/confusion_matrix_sta_CV_nt_rot_wc_fc_noFT_jointly_19.csv'

# CROSS-SUBJECT RESULTS
# filename = './results/lstm/cs/confusion_matrix_lstm_129.csv'
# filename = './results/lstm/cs/confusion_matrix_lstm_rot_85.csv'
# filename = './results/lstm/cs/confusion_matrix_lstm_notrans_rot_weighted_150_148.csv'
# filename = './results/lstm/cs/confusion_matrix_lstm_notrans_rot_wc_ds_290.csv'
# filename = './results/i3d/cs/confusion_matrix_cw.csv'
# filename = './results/i3d/cs/confusion_matrix_i3d_wc_fc_fixtest.csv'  # CS
# filename = './results/sta/cs/confusion_matrix_epoch26.csv'
# filename = './results/sta/cs/confusion_matrix_sta_rot_wc_nt_ds_9.csv'
# filename = './results/sta/cs/confusion_matrix_rot_cw_37.csv'
filename = './results/sta/cs/confusion_matrix_sta_rot_wc_fc_FT_jointly_34.csv'

mat = np.loadtxt(filename, delimiter=';')

# Remove rows with no tests
row_sum = mat.sum(axis=1)
indices = row_sum.nonzero()[0]
temp = mat[indices, :]
trimmed = temp[:, indices]

accuracies = np.diag(trimmed) / np.sum(trimmed, axis=1)
acc = np.diag(trimmed).sum() / trimmed.sum()

confmat = trimmed # / np.sum(trimmed, axis=1)
totals = np.sum(trimmed, axis=1)
for r in range(confmat.shape[0]):
    confmat[r, :] /= totals[r]

print('Class\tAccuracy')
a = 0
for i in indices:
    print('%5d\t  %.3f' % (i, accuracies[a]))
    a += 1

print('Mean accuracy per class: %.3f' % accuracies.mean())
print('              Std. dev.: %.2f' % accuracies.std())

print('Activity classif. accuracy: %.3f' % acc)

fig = plt.figure(figsize=(14,14))
ax = fig.add_subplot(111)
ax.imshow(confmat) # , cmap='gray_r')
h, w = confmat.shape[0], confmat.shape[0]
if h == 19:
    labels = [cl.labels_cv[i] for i in indices]
else:
    labels = [cl.labels[i] for i in indices]
plt.yticks(range(h), labels, fontsize='large')
plt.xticks(range(w), labels, rotation='vertical', fontsize='large')

for x in range(w):
    for y in range(h):
        # val = '%.1f' % (100*confmat[x, y])
        val = '%.2f' % (confmat[x, y])
        if confmat[x,y] < 1:
            val = val[1:]
        if not confmat[x,y] == 0:
            ax.annotate(val, xy=(y, x),
                        horizontalalignment='center',
                        verticalalignment='center', fontsize='large')  # , fontsize='small')

# plt.tight_layout()
plt.savefig(filename.replace('.csv', '.pdf'))
plt.show()
