import umap
import umap.plot
import numpy as np
import os
import itertools
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

def _PBN(betti, gridsize, f):
    ipbn = []
    for i in betti.keys():
        pbn = []
        for x in np.arange(0, f+0.01, gridsize):
            temp = 0
            for j in range(len(betti[i])):
                #print(betti[i][j])
                if x>=betti[i][j][0] and x<=betti[i][j][1]:
                    temp += 1
            pbn.append(temp)
            #print(pbn)
        ipbn.append(pbn)
    return ipbn

def PBN(X, sym):
    MAPbX3_sym_CNPbXBetti = dict()
    for i in range(1, 1001):
        file0 = open("/mnt/c/Users/wee_j/Documents/PhD Research/PhD Codes/Vijai_Gudhi_PointCloud/MAPbX_ClassificationProblem/MAPbX3_ClassificationTest/MAPbX_Classification_CNPbX/PH_OUT_MAPb"+X+"3_"+sym+"_CNPbX/Gudhi_"+sym+"_CNXPb_L5_f"+str(i)+"_b0.txt")
        file1 = open("/mnt/c/Users/wee_j/Documents/PhD Research/PhD Codes/Vijai_Gudhi_PointCloud/MAPbX_ClassificationProblem/MAPbX3_ClassificationTest/MAPbX_Classification_CNPbX/PH_OUT_MAPb"+X+"3_"+sym+"_CNPbX/Gudhi_"+sym+"_CNXPb_L5_f"+str(i)+"_b1.txt")
        file2 = open("/mnt/c/Users/wee_j/Documents/PhD Research/PhD Codes/Vijai_Gudhi_PointCloud/MAPbX_ClassificationProblem/MAPbX3_ClassificationTest/MAPbX_Classification_CNPbX/PH_OUT_MAPb"+X+"3_"+sym+"_CNPbX/Gudhi_"+sym+"_CNXPb_L5_f"+str(i)+"_b2.txt")
        contents0 = file0.readlines()
        contents1 = file1.readlines()
        contents2 = file2.readlines()
        betti = dict()
        temp = []
        for j in range(len(contents0)):
            temp.append(list(map(float, contents0[j].strip("\n").split(","))))
        betti[0] = temp
        temp = []
        for j in range(len(contents1)):
            temp.append(list(map(float, contents1[j].strip("\n").split(","))))
        betti[1] = temp
        temp = []
        for j in range(len(contents2)):
            temp.append(list(map(float, contents2[j].strip("\n").split(","))))
        betti[2] = temp
        MAPbX3_sym_CNPbXBetti[i] = betti

    MAPbX3_sym_CNPbX_PBN = []
    for i in range(1, 1001):
        MAPbX3_sym_CNPbX_PBN.append(_PBN(MAPbX3_sym_CNPbXBetti[i], 0.1, 10))
        
    return MAPbX3_sym_CNPbX_PBN

MAPbBr3_Cubic_CNPbXdata = dict()
MAPbCl3_Cubic_CNPbXdata = dict()
MAPbI3_Cubic_CNPbXdata = dict()
MAPbBr3_Ortho_CNPbXdata = dict()
MAPbCl3_Ortho_CNPbXdata = dict()
MAPbI3_Ortho_CNPbXdata = dict()
MAPbBr3_Tetra_CNPbXdata = dict()
MAPbCl3_Tetra_CNPbXdata = dict()
MAPbI3_Tetra_CNPbXdata = dict()

for i in range(1, 1001):
    file = open("/mnt/c/Users/wee_j/Documents/PhD Research/PhD Codes/Vijai_Gudhi_PointCloud/MAPbX_ClassificationProblem/MAPbX3_PHinput_data/MAPbBr3/ElemSpecificGroup_CNPbX/MAPbBr3_Cubic_CNPbXdata/CNXPb_atmlist_L5_f"+str(i)+".txt")
    contents = file.readlines()
    temp = []
    for j in range(len(contents)):
        temp.append(list(map(float, contents[j].strip("\n").split(","))))
    MAPbBr3_Cubic_CNPbXdata[i] = temp
    

for i in range(1, 1001):
    file = open("/mnt/c/Users/wee_j/Documents/PhD Research/PhD Codes/Vijai_Gudhi_PointCloud/MAPbX_ClassificationProblem/MAPbX3_PHinput_data/MAPbCl3/ElemSpecificGroup_CNPbX/MAPbCl3_Cubic_CNPbXdata/CNXPb_atmlist_L5_f"+str(i)+".txt")
    contents = file.readlines()
    temp = []
    for j in range(len(contents)):
        temp.append(list(map(float, contents[j].strip("\n").split(","))))
    MAPbCl3_Cubic_CNPbXdata[i] = temp
    
for i in range(1, 1001):
    file = open("/mnt/c/Users/wee_j/Documents/PhD Research/PhD Codes/Vijai_Gudhi_PointCloud/MAPbX_ClassificationProblem/MAPbX3_PHinput_data/MAPbI3/ElemSpecificGroup_CNPbX/MAPbI3_Cubic_CNPbXdata/CNXPb_atmlist_L5_f"+str(i)+".txt")
    contents = file.readlines()
    temp = []
    for j in range(len(contents)):
        temp.append(list(map(float, contents[j].strip("\n").split(","))))
    MAPbI3_Cubic_CNPbXdata[i] = temp
    
for i in range(1, 1001):
    file = open("/mnt/c/Users/wee_j/Documents/PhD Research/PhD Codes/Vijai_Gudhi_PointCloud/MAPbX_ClassificationProblem/MAPbX3_PHinput_data/MAPbBr3/ElemSpecificGroup_CNPbX/MAPbBr3_Orthorhombic_CNPbXdata/CNXPb_atmlist_L5_f"+str(i)+".txt")
    contents = file.readlines()
    temp = []
    for j in range(len(contents)):
        temp.append(list(map(float, contents[j].strip("\n").split(","))))
    MAPbBr3_Ortho_CNPbXdata[i] = temp
    
for i in range(1, 1001):
    file = open("/mnt/c/Users/wee_j/Documents/PhD Research/PhD Codes/Vijai_Gudhi_PointCloud/MAPbX_ClassificationProblem/MAPbX3_PHinput_data/MAPbCl3/ElemSpecificGroup_CNPbX/MAPbCl3_Orthorhombic_CNPbXdata/CNXPb_atmlist_L5_f"+str(i)+".txt")
    contents = file.readlines()
    temp = []
    for j in range(len(contents)):
        temp.append(list(map(float, contents[j].strip("\n").split(","))))
    MAPbCl3_Ortho_CNPbXdata[i] = temp
    
for i in range(1, 1001):
    file = open("/mnt/c/Users/wee_j/Documents/PhD Research/PhD Codes/Vijai_Gudhi_PointCloud/MAPbX_ClassificationProblem/MAPbX3_PHinput_data/MAPbI3/ElemSpecificGroup_CNPbX/MAPbI3_Orthorhombic_CNPbXdata/CNXPb_atmlist_L5_f"+str(i)+".txt")
    contents = file.readlines()
    temp = []
    for j in range(len(contents)):
        temp.append(list(map(float, contents[j].strip("\n").split(","))))
    MAPbI3_Ortho_CNPbXdata[i] = temp
    
for i in range(1, 1001):
    file = open("/mnt/c/Users/wee_j/Documents/PhD Research/PhD Codes/Vijai_Gudhi_PointCloud/MAPbX_ClassificationProblem/MAPbX3_PHinput_data/MAPbBr3/ElemSpecificGroup_CNPbX/MAPbBr3_Tetragonal_CNPbXdata/CNXPb_atmlist_L5_f"+str(i)+".txt")
    contents = file.readlines()
    temp = []
    for j in range(len(contents)):
        temp.append(list(map(float, contents[j].strip("\n").split(","))))
    MAPbBr3_Tetra_CNPbXdata[i] = temp
    
for i in range(1, 1001):
    file = open("/mnt/c/Users/wee_j/Documents/PhD Research/PhD Codes/Vijai_Gudhi_PointCloud/MAPbX_ClassificationProblem/MAPbX3_PHinput_data/MAPbCl3/ElemSpecificGroup_CNPbX/MAPbCl3_Tetragonal_CNPbXdata/CNXPb_atmlist_L5_f"+str(i)+".txt")
    contents = file.readlines()
    temp = []
    for j in range(len(contents)):
        temp.append(list(map(float, contents[j].strip("\n").split(","))))
    MAPbCl3_Tetra_CNPbXdata[i] = temp
    
for i in range(1, 1001):
    file = open("/mnt/c/Users/wee_j/Documents/PhD Research/PhD Codes/Vijai_Gudhi_PointCloud/MAPbX_ClassificationProblem/MAPbX3_PHinput_data/MAPbI3/ElemSpecificGroup_CNPbX/MAPbI3_Tetragonal_CNPbXdata/CNXPb_atmlist_L5_f"+str(i)+".txt")
    contents = file.readlines()
    temp = []
    for j in range(len(contents)):
        temp.append(list(map(float, contents[j].strip("\n").split(","))))
    MAPbI3_Tetra_CNPbXdata[i] = temp

x = ["Br", "Cl", "I"]
sym = ["Cubic", "Ortho", "Tetra"]

for (a,b) in itertools.product(x,sym):
    #print(a,b)
    vars()["MAPb"+a+"3_"+b+"_CNPbX_PBN"] = PBN(a,b)

# Check Filtered Persistent Betti Numbers for non-zero values
for (a,b) in itertools.product(x,sym):
    print((a,b))
    print(np.array(vars()["MAPb"+a+"3_"+b+"_CNPbX_PBN"])[499:1000, 0, 10:40][50])
    print(np.array(vars()["MAPb"+a+"3_"+b+"_CNPbX_PBN"])[499:1000, 1, 20:50][50])
    print(np.array(vars()["MAPb"+a+"3_"+b+"_CNPbX_PBN"])[499:1000, 2, 30:60][50])
    print("\n")

frs = 500
frd = 1000
for ndim in [0, 1, 2]:
    if ndim==0:
        spbn=10
        epbn=40
    elif ndim==1:
        spbn=20
        epbn=50
    else:
        spbn=30
        epbn=60
        

    for a in x:
        vars()["betti"+a] = np.zeros((3*(frd-frs+1), 30, 3))
        #print(frs, frd, ndim, spbn, epbn)
        vars()["betti"+a][:frd-frs+1,:30,ndim] = np.array(vars()["MAPb"+a+"3_Cubic_CNPbX_PBN"])[frs-1:frd,ndim,spbn:epbn]
        vars()["betti"+a][frd-frs+1:2*(frd-frs+1),:30,ndim] = np.array(vars()["MAPb"+a+"3_Ortho_CNPbX_PBN"])[frs-1:frd,ndim,spbn:epbn]
        vars()["betti"+a][2*(frd-frs+1):,:30,ndim] = np.array(vars()["MAPb"+a+"3_Tetra_CNPbX_PBN"])[frs-1:frd,ndim,spbn:epbn]


for a in x:
    vars()["betti"+a+"_2"] = []
    vars()["betti"+a+"_2"] = np.reshape(vars()["betti"+a], (1503, 90))
    
betti_all = np.concatenate((bettiBr_2, bettiCl_2, bettiI_2))

print(np.shape(betti_all))
np.save("betti_CNPbX.npy", betti_all)

pca = PCA(n_components=2)
values = pca.fit_transform(betti_all)

plt.figure(dpi=200)
plt.scatter(-values[:frd-frs+1,0], values[:frd-frs+1,1], marker='^', color='white', alpha=0.75, edgecolor='tab:blue', linewidth=.5, s=20, label="Br-Cubic")
plt.scatter(-values[frd-frs+1:2*(frd-frs+1),0], values[frd-frs+1:2*(frd-frs+1),1], marker='^', color='white', alpha=0.75, edgecolor='tab:orange', linewidth=0.5, s=20, label="Br-Ortho")
plt.scatter(-values[2*(frd-frs+1):3*(frd-frs+1),0], values[2*(frd-frs+1):3*(frd-frs+1),1], marker='^', color='white', alpha=0.75, edgecolor='tab:green', linewidth=0.5, s=20, label="Br-Tetra")

plt.scatter(-values[3*(frd-frs+1):4*(frd-frs+1),0], values[3*(frd-frs+1):4*(frd-frs+1),1], marker='s', color='white', alpha=0.75, edgecolor='tab:red', linewidth=0.5, s=20, label="Cl-Cubic")
plt.scatter(-values[4*(frd-frs+1):5*(frd-frs+1),0], values[4*(frd-frs+1):5*(frd-frs+1),1], marker='s', color='white', alpha=0.75, edgecolor='tab:purple', linewidth=0.5, s=20, label="Cl-Ortho")
plt.scatter(-values[5*(frd-frs+1):6*(frd-frs+1),0], values[5*(frd-frs+1):6*(frd-frs+1),1], marker='s', color='white', alpha=0.75, edgecolor='tab:brown', linewidth=0.5, s=20, label="Cl-Tetra")

plt.scatter(-values[6*(frd-frs+1):7*(frd-frs+1),0], values[6*(frd-frs+1):7*(frd-frs+1),1], color='white', alpha=0.75, edgecolor='tab:pink', linewidth=0.5, s=20, label="I-Cubic")
plt.scatter(-values[7*(frd-frs+1):8*(frd-frs+1),0], values[7*(frd-frs+1):8*(frd-frs+1),1], color='white', alpha=0.75, edgecolor='tab:gray', linewidth=0.5, s=20, label="I-Ortho")
plt.scatter(-values[8*(frd-frs+1):9*(frd-frs+1),0], values[8*(frd-frs+1):9*(frd-frs+1),1], color='white', alpha=0.75, edgecolor='tab:olive', linewidth=0.5, s=20, label="I-Tetra")

plt.ylim(-400, 700)
plt.xlim(-1000, 1000)
plt.legend(ncol=3, loc='upper left', handlelength=.5, borderpad=.25, fontsize=10)
plt.savefig("MAPbX3_Classification_CNPbX_PCA.png", dpi=200)
plt.show()


values = TSNE(n_components=2, method='exact').fit_transform(betti_all)
plt.figure(dpi=200)
plt.scatter(values[:frd-frs+1,0], values[:frd-frs+1,1], marker='^', color='white', alpha=0.75, edgecolor='tab:blue', linewidth=.5, s=20, label="Br-Cubic")
plt.scatter(values[frd-frs+1:2*(frd-frs+1),0], values[frd-frs+1:2*(frd-frs+1),1], marker='^', color='white', alpha=0.75, edgecolor='tab:orange', linewidth=0.5, s=20, label="Br-Ortho")
plt.scatter(values[2*(frd-frs+1):3*(frd-frs+1),0], values[2*(frd-frs+1):3*(frd-frs+1),1], marker='^', color='white', alpha=0.75, edgecolor='tab:green', linewidth=0.5, s=20, label="Br-Tetra")

plt.scatter(values[3*(frd-frs+1):4*(frd-frs+1),0], values[3*(frd-frs+1):4*(frd-frs+1),1], marker='s', color='white', alpha=0.75, edgecolor='tab:red', linewidth=0.5, s=20, label="Cl-Cubic")
plt.scatter(values[4*(frd-frs+1):5*(frd-frs+1),0], values[4*(frd-frs+1):5*(frd-frs+1),1], marker='s', color='white', alpha=0.75, edgecolor='tab:purple', linewidth=0.5, s=20, label="Cl-Ortho")
plt.scatter(values[5*(frd-frs+1):6*(frd-frs+1),0], values[5*(frd-frs+1):6*(frd-frs+1),1], marker='s', color='white', alpha=0.75, edgecolor='tab:brown', linewidth=0.5, s=20, label="Cl-Tetra")

plt.scatter(values[6*(frd-frs+1):7*(frd-frs+1),0], values[6*(frd-frs+1):7*(frd-frs+1),1], color='white', alpha=0.75, edgecolor='tab:pink', linewidth=0.5, s=20, label="I-Cubic")
plt.scatter(values[7*(frd-frs+1):8*(frd-frs+1),0], values[7*(frd-frs+1):8*(frd-frs+1),1], color='white', alpha=0.75, edgecolor='tab:gray', linewidth=0.5, s=20, label="I-Ortho")
plt.scatter(values[8*(frd-frs+1):9*(frd-frs+1),0], values[8*(frd-frs+1):9*(frd-frs+1),1], color='white', alpha=0.75, edgecolor='tab:olive', linewidth=0.5, s=20, label="I-Tetra")

plt.ylim(-80, 140)
plt.xlim(-80, 80)
plt.legend(ncol=3, loc='upper left', handlelength=.5, borderpad=.25, fontsize=10)
plt.savefig("MAPbX3_Classification_CNPbX_tSNE.png", dpi=200)
plt.show()

values = umap.UMAP(min_dist=1, metric='euclidean').fit_transform(betti_all)
plt.figure(dpi=200)
plt.scatter(values[:frd-frs+1,0], values[:frd-frs+1,1], marker='^', color='white', alpha=0.75, edgecolor='tab:blue', linewidth=.5, s=20, label="Br-Cubic")
plt.scatter(values[frd-frs+1:2*(frd-frs+1),0], values[frd-frs+1:2*(frd-frs+1),1], marker='^', color='white', alpha=0.75, edgecolor='tab:orange', linewidth=0.5, s=20, label="Br-Ortho")
plt.scatter(values[2*(frd-frs+1):3*(frd-frs+1),0], values[2*(frd-frs+1):3*(frd-frs+1),1], marker='^', color='white', alpha=0.75, edgecolor='tab:green', linewidth=0.5, s=20, label="Br-Tetra")

plt.scatter(values[3*(frd-frs+1):4*(frd-frs+1),0], values[3*(frd-frs+1):4*(frd-frs+1),1], marker='s', color='white', alpha=0.75, edgecolor='tab:red', linewidth=0.5, s=20, label="Cl-Cubic")
plt.scatter(values[4*(frd-frs+1):5*(frd-frs+1),0], values[4*(frd-frs+1):5*(frd-frs+1),1], marker='s', color='white', alpha=0.75, edgecolor='tab:purple', linewidth=0.5, s=20, label="Cl-Ortho")
plt.scatter(values[5*(frd-frs+1):6*(frd-frs+1),0], values[5*(frd-frs+1):6*(frd-frs+1),1], marker='s', color='white', alpha=0.75, edgecolor='tab:brown', linewidth=0.5, s=20, label="Cl-Tetra")

plt.scatter(values[6*(frd-frs+1):7*(frd-frs+1),0], values[6*(frd-frs+1):7*(frd-frs+1),1], color='white', alpha=0.75, edgecolor='tab:pink', linewidth=0.5, s=20, label="I-Cubic")
plt.scatter(values[7*(frd-frs+1):8*(frd-frs+1),0], values[7*(frd-frs+1):8*(frd-frs+1),1], color='white', alpha=0.75, edgecolor='tab:gray', linewidth=0.5, s=20, label="I-Ortho")
plt.scatter(values[8*(frd-frs+1):9*(frd-frs+1),0], values[8*(frd-frs+1):9*(frd-frs+1),1], color='white', alpha=0.75, edgecolor='tab:olive', linewidth=0.5, s=20, label="I-Tetra")

plt.ylim(-10, 35)
#plt.xlim(-80, 80)
plt.legend(ncol=3, loc='upper left', handlelength=.25, borderpad=.25, fontsize=10)
plt.savefig("MAPbX3_Classification_CNPbX_UMAP.png", dpi=200)
plt.show()