import numpy as np
import matplotlib.pyplot as plt

def f0(filename):
	data = np.genfromtxt(filename, delimiter=" ")
	n_mean  = np.mean(data[:,0])
	n_std   = np.std(data[:,0])
	b_mean  = np.mean(data[:,1])
	b_std   = np.std(data[:,1])
	m_mean  = np.mean(data[:,2])
	m_std   = np.std(data[:,2])
	bn_mean = np.mean(data[:,3])
	bn_std  = np.std(data[:,3])
	bm_mean = np.mean(data[:,4])
	bm_std  = np.std(data[:,4])
	nn_mean = np.mean(data[:,5])
	nn_std  = np.std(data[:,5])
	nv_mean = np.mean(data[:,6])
	nv_std  = np.std(data[:,6])
	mv_mean = np.mean(data[:,7])
	mv_std  = np.std(data[:,7])

	print()
	print(filename)
	print("N: ",f"{n_mean:.2E}",f"{n_std:.2E}")
	print("B: ",f"{b_mean:.2E}",f"{b_std:.2E}")
	print("M: ",f"{m_mean:.2E}",f"{m_std:.2E}")
	print("BN:",f"{bn_mean:.2E}",f"{bn_std:.2E}")
	print("BM:",f"{bm_mean:.2E}",f"{bm_std:.2E}")
	print("NN:",f"{nn_mean:.2E}",f"{nn_std:.2E}")
	print("NV:",f"{nv_mean:.2E}",f"{nv_std:.2E}")
	print("MV:",f"{mv_mean:.2E}",f"{mv_std:.2E}")


f0("ac_df_mc_mis_os.txt")
f0("ac_df_mc_proc_os.txt")
f0("ac_df_mc_all_os.txt")

f0("ac_df_mc_mis_cm.txt")
f0("ac_df_mc_proc_cm.txt")
f0("ac_df_mc_all_cm.txt")

f0("ac_df_mc_mis_vreg.txt")
f0("ac_df_mc_proc_vreg.txt")
f0("ac_df_mc_all_vreg.txt")

f0("ac_df_mc_mis_av.txt")
f0("ac_df_mc_proc_av.txt")
f0("ac_df_mc_all_av.txt")

f0("ac_df_mc_mis_pm.txt")
f0("ac_df_mc_proc_pm.txt")
f0("ac_df_mc_all_pm.txt")

f0("ac_df_mc_mis_gbw.txt")
f0("ac_df_mc_proc_gbw.txt")
f0("ac_df_mc_all_gbw.txt")

#data = np.genfromtxt("ac_df_mc_all_av.txt", delimiter=" ")
#a = data[:,0]
#_ = plt.hist(a, bins='auto')
#print(a)
#plt.show()
