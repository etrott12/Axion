import subprocess
from numpy import *
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import scipy as spy
from scipy import spatial
from itertools import product

#missing files : ma_3_fa_6_0.dat


run_axionCAMB = True

#number of redshifts output by each run of axioncamb
numz = 301
#fiducial parameter values as given in table 3 of Planck 2015 (arxiv 1502.01589)
fv = [0.02225,0.1198,0.0001,10**-27,67.27,0.9645]
#parameter confidence intervals as given in table 3 of Planck 2015 (arxiv 1502.01589)
ci = [0.00016,0.0015,'n/a','n/a',0.66,0.0049]
#number of axioncamb runs for each parameter
runs = 9
#run values for omega_baryon
omegab = np.round(np.linspace(fv[0]-ci[0],fv[0]+ci[0],runs),5)
#run values for omega_cdm
omegac = np.round(np.linspace(fv[1]-ci[1],fv[1]+ci[1],runs),4)
#run values for omega_cdm and omega_axion used to run the desired axion fractions
#omegac2 = np.round(np.linspace(0.,fv[1],runs),5)
#omegaax = np.round(fv[1]-np.linspace(0.,fv[1]-0.0012,runs),5)
#fa = np.round([omegaax[i]/fv[1] for i in range(len(omegaax))],3)
fa = np.linspace(0.0001,0.2,9)
omegaax = fv[1]*fa
omegac2 = fv[1]-omegaax
fa_zip = zip(omegac2,omegaax)
#run values for axion mass
ma = np.logspace(-29,-24,runs)
#run values for hubble constant
h = np.round(np.linspace(fv[4]-ci[4],fv[4]+ci[4],runs),2)
#run values for scalar tilt
ns = np.round(np.linspace(fv[5]-ci[5],fv[5]+ci[5],runs),4)

params = []
params.append(omegab)
params.append(omegac)
params.append(fa)
#params.append(np.asarray(fa_zip))
params.append(ns)
params.append(h)

#print omegac2,omegaax

ma2 = np.logspace(-29,-22,11)
#print(fv[0],ma2[0])
subprocess.call('./camb params.ini 1 %s 2 %s 3 %s 4 %s 5 %s 6 %s' %(fv[0],fv[1],fv[2],ma2[3],fv[4],fv[5]), shell = True) 
#subprocess.call('./camb params_z4.ini 1 %s 2 %s 3 %s 4 %s 5 %s 6 %s' %(fv[0],omegac2[6],omegaax[6],ma[3],fv[4],fv[5]), shell = True)
#for i in range(numz):
#	subprocess.call('mv test_matterpower%s.dat ma_3_fa_6_%s.dat' %(i,i), shell = True)

#subprocess.call('./camb params_z4.ini 1 0.02225 2 0.1198 3 0.0001 4 10**-27 5 67.27 6 0.9645', shell = True)
#for i in range(301):
#	subprocess.call('mv test_matterpower%s.dat data/test_%s.dat' %(i,i), shell = True)
"""
if run_axionCAMB == True:
	for l in range(9,len(ma2)):
	        #run axioncamb with standard cosmology
		subprocess.call('./camb params_z4.ini 1 %s 2 %s 3 %s 4 %s 5 %s 6 %s' %(fv[0],fv[1],fv[2],ma2[l],fv[4],fv[5]), shell = True)
		for k in range(numz):
			subprocess.call('mv test_matterpower%s.dat data/ma_%s_fiducial_%s.dat' %(k,l,k), shell=True)

		for i in range(runs):
		        #run axioncamb with variable omega_baryon
			subprocess.call('./camb params_z4.ini 1 %s 2 %s 3 %s 4 %s 5 %s 6 %s' %(omegab[i],fv[1],fv[2],ma2[l],fv[4],fv[5]), shell = True)
			for j in range(numz):
				subprocess.call('mv test_matterpower%s.dat data/ma_%s_omegab_%s_%s.dat' %(j,l,i,j), shell=True)
		        #run axioncamb with variable omega_cdm
			subprocess.call('./camb params_z4.ini 1 %s 2 %s 3 %s 4 %s 5 %s 6 %s' %(fv[0],omegac[i],fv[2],ma2[l],fv[4],fv[5]), shell = True)
			for j in range(numz):
				subprocess.call('mv test_matterpower%s.dat data/ma_%s_omegac_%s_%s.dat' %(j,l,i,j), shell=True)
		        #run axioncamb with variable mass at each axion fraction
			subprocess.call('./camb params_z4.ini 1 %s 2 %s 3 %s 4 %s 5 %s 6 %s' %(fv[0],omegac2[i],omegaax[i],ma2[l],fv[4],fv[5]), shell = True)
			for j in range(numz):
				subprocess.call('mv test_matterpower%s.dat data/ma_%s_fa_%s_%s.dat' %(j,l,i,j), shell=True)
		        #run axioncamb with variable hubble constant
			subprocess.call('./camb params_z4.ini 1 %s 2 %s 3 %s 4 %s 5 %s 6 %s' %(fv[0],fv[1],fv[2],ma2[l],h[i],fv[5]), shell = True)
			for j in range(numz):
				subprocess.call('mv test_matterpower%s.dat data/ma_%sh_%s_%s.dat' %(j,l,i,j), shell=True)
		        #run axioncamb with variable scalar tilt
			subprocess.call('./camb params_z4.ini 1 %s 2 %s 3 %s 4 %s 5 %s 6 %s' %(fv[0],fv[1],fv[2],ma2[l],fv[4],ns[i]), shell = True)
			for j in range(numz):
				subprocess.call('mv test_matterpower%s.dat data/ma_%s_ns_%s_%s.dat' %(j,l,i,j), shell=True)
"""
"""
k = []
k_fiducial = []
k_fiducial.append([loadtxt('data/fiducial_%s.dat'%(y),unpack=True,usecols=[0]) for y in range(numz)])
k.append([[loadtxt('data/omegab_%s_%s.dat'%(i,y),unpack=True,usecols=[0]) for y in range(numz)] for i in range(runs)])
k.append([[loadtxt('data/omegac_%s_%s.dat'%(i,y),unpack=True,usecols=[0]) for y in range(numz)] for i in range(runs)])
k.append([[[loadtxt('data/fa_%s_ma_%s_%s.dat'%(i,j,y),unpack=True,usecols=[0]) for y in range(numz)] for j in range(runs)] for i in range(runs)])
k.append([[loadtxt('data/h_%s_%s.dat'%(i,y),unpack=True,usecols=[0]) for y in range(numz)] for i in range(runs)])
k.append([[loadtxt('data/ns_%s_%s.dat'%(i,y),unpack=True,usecols=[0]) for y in range(numz)] for i in range(runs)])


Pk = []
#Pk_fiducial = []
#Pk_fiducial.append([loadtxt('data/fiducial_%s.dat'%(y),unpack=True,usecols=[1]) for y in range(np.int(numz))])
#Pk.append([[loadtxt('data/omegab_%s_%s.dat'%(i,y),unpack=True,usecols=[1]) for y in range(numz)] for i in range(runs)])
#Pk.append([[loadtxt('data/omegac_%s_%s.dat'%(i,y),unpack=True,usecols=[1]) for y in range(numz)] for i in range(runs)])
Pk.append([[[loadtxt('data/fa_%s_ma_%s_%s.dat'%(i,j,y),unpack=True,usecols=[1]) for y in range(numz)] for j in range(runs)] for i in range(runs)])
#Pk.append([[loadtxt('data/h_%s_%s.dat'%(i,y),unpack=True,usecols=[1]) for y in range(numz)] for i in range(runs)])
#Pk.append([[loadtxt('data/ns_%s_%s.dat'%(i,y),unpack=True,usecols=[1]) for y in range(numz)] for i in range(runs)])
#Pk.append([[[loadtxt('data/fa_%s_ma_%s_%s.dat'%(i,j,y),unpack = True,usecols = [1]) for y in range(numz)] for j in range(runs)] for i in range(runs)])

Pk.append([loadtxt('data/omegab_0_%s.dat'%(y),unpack=True,usecols=[1]) for y in range(numz)])
print np.shape(Pk)
"""
#all of the fa_8... files DNE because fa = 0 -- set the floor at some very small but nonzero value
#fiducial run doesn't fit with the others because it's not run for 9 different param combos -- probably easiest to just run it 9 times (all with the same param values)
#maybe the fiducial runs don't need to go into the matrix -- not marginalized over --> just keep it separate and use as needed individually
#reverse the order of k an pk arrays
