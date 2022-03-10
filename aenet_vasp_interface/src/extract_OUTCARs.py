import os
import shutil

def extracting_OUTCARs():
    datasetsize=len(os.listdir('../vasprun_directories'))

    if os.listdir('../OUTCARs')!=[]:
        shutil.rmtree('../OUTCARs')
        os.mkdir('../OUTCARs')

    for i in range(0, datasetsize):
        shutil.copy('../vasprun_directories/'+str(i)+'/OUTCAR', '../OUTCARs/OUTCAR'+str(i))
