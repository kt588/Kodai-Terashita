from OUTCARtoXSF import OUTCAR_reader
import os
import shutil

def Dataset_generator():
    datasetsize=len(os.listdir('../vasprun_directories'))

    if os.listdir('../xsfs')!=[]:
        shutil.rmtree('../xsfs')
        os.mkdir('../xsfs')

    ite=0

    for i in range(0, datasetsize):
        filename=('../OUTCARs/OUTCAR'+str(i))
        ins_OUTCAR_reader=OUTCAR_reader(OUTCAR=filename, xsffile_name='../xsfs/'+str(ite)+'.xsf')
        if ins_OUTCAR_reader.IS_OUTCAR_APPROPRIATE():
            ins_OUTCAR_reader.writing_xsf()
            ite+=1
