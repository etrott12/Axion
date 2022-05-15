import numpy as np
import subprocess

# number of redshifts run by axionCAMB
numz = 301
# number of parameter values run for each parameter
num_values = 9
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
ma = np.logspace(-30,-24,100)

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
subprocess.call(['./camb params.ini 1 %s 2 %s 3 %s 4 %s 5 %s 6 %s' %(a[0][0][0],a[0][0][1],a[0][0][2],ma[0],a[0][0][3],a[0][0][4]), shell = True)
# run axionCamb for all parameter combinations
# run_count, move_count, and print statements can show what parameter combinations are run and how many times axionCAMB is run
run_count = 0
move_count = 0
#for i in range(len(ma)):
# for i in range(1):
    #for j in range(len(param_values)):
    # for j in range(1):
    #     for k in range(num_values):
    #         print(a[j][k][0],a[j][k][1],a[j][k][2],ma[i],a[j][k][3],a[j][k][4])
    #         subprocess.call('./camb params_z4.ini 1 a[j][k][0] 2 a[j][k][1] 3 a[j][k][2] 4 ma[i] 5 a[j][k][3] 6 a[j][k][4]', shell = True)
            #run_count += 1
            #for l in range(numz):
                #subprocess.call('mv test_matterpower%s.dat data/mass%s_param%s_value%s.dat' %(l,i,j,k), shell = True)
                #move_count += 1
#print('run axionCAMB ',run_count,' times and move ',move_count,' data files')
