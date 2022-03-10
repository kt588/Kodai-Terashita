'''Please locate the structure files for training in this directory(aenet_vasp_interface)'''


class OUTCAR_reader:

    def __init__(self, OUTCAR, xsffile_name):
        self.OUTCAR=OUTCAR
        with open(self.OUTCAR, 'r') as f1:
            self.lines=f1.readlines()

        self.savefile=xsffile_name


        self.elements=self._reading_elements()
        self.num_each_atoms=self._reading_num_each_atoms()
        self.num_all_atoms=self._reading_num_all_atoms()
        self.ENG=self._reading_ENERGY()
        self.PRIMVEC=self._reading_PRIMVEC()
        self.coordinates=self._reading_coordinates()


    def _str_group(self, string1, string2):
        line_string1=[i for i, x in enumerate(self.lines) if string1 in x][0]
        ite=0
        lines_belowstring=[]
        while (string1 in self.lines[line_string1+ite]) or (string2 in self.lines[line_string1+ite]):
            lines_belowstring+=[line_string1+ite]
            ite+=1
        return lines_belowstring

    def str_to_int_inlist(self, lst):
        lst2=[int(i) for i in lst]
        return lst2

    def _listlist_to_string(self, lst):
        string=''
        for x in lst:
            string+=' '.join(x)+'\n'
        return string

    def IS_OUTCAR_APPROPRIATE(self):
        TorF=False
        for x in self.lines:
            if 'General timing and accounting informations for this job:' in x:
                TorF=True
        return TorF


    def _reading_elements(self):
        lines_elements=self._str_group('INCAR:', 'POTCAR:')[1:]
        elements=[self.lines[i].strip().split()[2] for i in lines_elements]
        return elements

    def _reading_num_each_atoms(self):
        line_num_each_atoms=[i for i, x in enumerate(self.lines) if 'ions per type =' in x][0]
        num_each_atoms=self.lines[line_num_each_atoms].strip().split()[4:]
        return num_each_atoms

    def _reading_num_all_atoms(self):
        num_all_atoms=sum(self.str_to_int_inlist(self.num_each_atoms))
        return num_all_atoms

    def _reading_ENERGY(self):
        lines_aroundEN=[i for i, x in enumerate(self.lines) if 'FREE ENERGIE OF THE ION-ELECTRON SYSTEM (eV)' in x]
        ENG=self.lines[lines_aroundEN[-1]+2].strip().split()[4]
        return ENG

    def _reading_PRIMVEC(self):
        lines_aroundPRIMVEC=[i for i, x in enumerate(self.lines) if 'direct lattice vectors' in x]
        lines_PRIMVEC=self.lines[lines_aroundPRIMVEC[-1]+1:lines_aroundPRIMVEC[-1]+4]
        PRIMVEC=[x.strip().split()[0:3] for x in lines_PRIMVEC]
        return PRIMVEC

    def _reading_coordinates(self):
        lines_aroundcoor=[i for i, x in enumerate(self.lines) if 'TOTAL-FORCE (eV/Angst)' in x]
        lines_coor=self.lines[lines_aroundcoor[-1]+2:lines_aroundcoor[-1]+2+self.num_all_atoms]
        coors=[x.strip().split()[0:3] for x in lines_coor]
        return coors

    def _package_element_coordinate(self):
        element_coordinate=[]
        head=0
        end=0
        for s, i in zip(self.elements, self.num_each_atoms):
            end+=int(i)
            for j in range(head, end):
                element_coordinate+=[[s]+self.coordinates[j]]
            head+=int(i)
        return element_coordinate


    def _writing_energy_part(self):
        x='# total energy = {} eV'.format(self.ENG)
        return x


    def _writing_PRIMVEC_part(self):
        x='''\
CRYSTAL
PRIMVEC
{}\
        '''.format(self._listlist_to_string(self.PRIMVEC))
        return x



    def _writing_PRIMCOORD_part(self):
        x='''\
PRIMCOORD
{0} 1
{1}\
        '''.format(self.num_all_atoms, self._listlist_to_string(self._package_element_coordinate()))
        return x



    def writing_xsf(self):
        with open(self.savefile, 'w') as f1:
            x='''\
{0}

{1}
{2}\
            '''.format(self._writing_energy_part(), self._writing_PRIMVEC_part(), self._writing_PRIMCOORD_part())
            f1.write(x)
