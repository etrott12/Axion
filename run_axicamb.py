import numpy as np
import subprocess

# number of redshifts run by axionCAMB
numz = 301
# number of parameter values run for each parameter
num_values = 1#9
# minimum and maximum axion fraction values
fa_min,fa_max = [0.0001,0.2]
# fiducial parameter values from Planck 2015
param_values = [0.02237,0.12,fa_min,67.36,0.9649]
# 1-sigma values for each parameter from Planck 2015
sigma1 = [0.00015,0.0012,0,0.54,0.0042]
# convert 1-sigma to 2-sigma to create our prior (flat)
sigma2 = [2*sigma1[i] for i in range(len(sigma1))]
# create range of axion fractions
fa = np.linspace(fa_min,fa_max,num_values)
# convert axion fractions to axion energy densities
omega_a = param_values[1]*fa
# adjust the dark matter energy density to accommodate axions
omega_c = param_values[1]-omega_a
# axion mass list
ma = np.logspace(-30,-24,1)#100)

# array of all parameter combinations
param_array = []
for i in range(len(param_values)):
    dim = []
    if i == 2:
        dim.append(np.asarray(num_values*[param_values[0]]))
        dim.append(omega_c)
        dim.append(omega_a)
        dim.append(np.asarray(num_values*[param_values[3]]))
        dim.append(np.asarray(num_values*[param_values[4]]))
    else:
        for j in range(len(param_values)):
            if i == j:
                dim.append(np.linspace(param_values[i]-sigma2[i],param_values[i]+sigma2[i],num_values))
            else:
                dim.append(np.asarray(num_values*[param_values[j]]))
    param_array.append(dim)
# reshape parameter combination array
a = np.transpose(param_array,(0,2,1))
#print(np.shape(a))
# run axionCamb for all parameter combinations
for i in range(len(ma)):
    for j in range(len(param_values)):
        for k in range(num_values):
            print(i,j,k)
            subprocess.call('../axionCAMB/./camb params_z4.ini 1 a[j][k][0] 2 a[j][k][1] 3 a[j][k][2] 4 ma[i] 5 a[j][k][3] 6 a[j][k][4]', shell = True)
            # for l in range(numz):
            #     print(i,j,k,l)
            #     subprocess.call('mv test_matterpower%s.dat mass%s_param%s_value%s.dat' %(l,i,j,k), shell = True)

# k = []
# pk = []
# k.append([[[loadtxt('data/mass%s_param%s_value%s.dat'%(),unpack=True,usecols=[0]) for i in range(len(ma))] for j in range(len(param_values))] for k in range(len(num_values))])
# pk.append([[[loadtxt('data/mass%s_param%s_value%s.dat'%(),unpack=True,usecols=[1]) for i in range(len(ma))] for j in range(len(param_values))] for k in range(len(num_values))])
# np.save('data/k.npy',k)
# np.save('data/pk.npy',pk)





