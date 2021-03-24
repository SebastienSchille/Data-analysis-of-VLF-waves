import numpy as np

vlf_data_NWC = np.genfromtxt('vlf_data_NWC.txt', dtype=float, delimiter=',')
vlf_data_JJI = np.genfromtxt('vlf_data_JJI.txt', dtype=float, delimiter=',')
vlf_data_JJY = np.genfromtxt('vlf_data_JJY.txt', dtype=float, delimiter=',')

vlf_data_NWC_db = (20*np.log(vlf_data_NWC))
vlf_data_JJI_db = (20*np.log(vlf_data_JJI))
vlf_data_JJY_db = (20*np.log(vlf_data_JJY))

print(vlf_data_JJY_db)
print(np.size(vlf_data_JJY))
print(np.size(vlf_data_JJY_db))
np.savetxt('vlf_data_JJY_db.txt',vlf_data_JJY_db, delimiter=',')