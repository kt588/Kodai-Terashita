# VASP-AENET interface
## About this package
### aenet_vasp_interface is a Python tool for generating the XSF structure files for AENET[^1] from OUTCAR files calculated by VASP[^2][^3][^4].
## How to use this package
### 1
#### First of all, you need to prepare a set of the VASP files. It should include OUTCAR of thousands of structure. An example of the dataset  is located in the directory named "dataset_example". Please make sure that you run the calculation after preparing the directories for each structure, including POSCAR, INCAR, KPOINTS, and POTCAR. These files except POSCAR should be common for all structures.

### 2
#### After the calculation of VASP files, you need to make the directories each of which includes the OUTCAR and other VASP files for each structure such like:
#### vasp_files/
#### &emsp;&emsp;&emsp;|--structure1
#### &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|--POSCAR
#### &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|--INCAR
#### &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|--KPOINTS
#### &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|--POTCAR
#### &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|--OUTCAR
#### &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|--CONTCAR
#### &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|--XDATCAR
#### &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|--   …
#### &emsp;&emsp;&emsp;|--structure2
#### &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|--POSCAR
#### &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|--INCAR
#### &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;|--   …

### 3
#### From this step you will use this package.
#### After installing this library to arbitrary location, please copy the directories of the structures(in above case it’s equal to “vasp_file/*") to "vasprun_directories" with the command such like:
#### ```cp ~/vasp_files/* ~/aenet_vasp_interface/vasprun_directories```

### 4
#### Next, please execute “main.py” with the command such like:
#### ```cd ~/aenet_vasp_interface/src```
#### ```python main.py```

#### Then you will find in ~/aenet_vasp_interface/xsfs the XSF structure files of which data are extracted from OUTCARs.
#### Please ignore the example files located in the directories of "vasprun_directories", "OUTCARs", and "xsfs" and remove or replace them with your own file.


### Citation
[^1]: N. Artrith and A. Urban, Comput. Mater. Sci. 114 (2016) 135-150.
[^2]: G. Kresse and J. Hafner, Phys. Rev. B 47 , 558 (1993); ibid. 49 , 14 251 (1994).
[^3]: G. Kresse and J. Furthmüller, Comput. Mat. Sci. 6 , 15 (1996).
[^4]: G. Kresse and J. Furthmüller, Phys. Rev. B 54 , 11 169 (1996).
