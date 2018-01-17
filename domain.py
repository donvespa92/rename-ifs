import re

class domain:
    instances = []
    def __init__(self,name,file):
        self.instances.append(self)
        self.name = name
        self.file = file
        
        self.read_file()
        self.get_data()
        self.get_boundaries()
        self.create_boundaries()
    
    class boundary:
        instances = []
        def __init__(self,name,domain,data):
            self.instances.append(self)
            self.name = name
            self.domain = domain.name
            self.data = domain.boundaries[name]
            
            self.get_location()
            
        def get_location(self):
            self.loc = []
            for idx,line in enumerate(self.data):
                if 'Location = ' in line:
                    self.loc = self.sformat(idx)
                    break
            
        def sformat(self,idx):
            locs = []
            self.data[idx] = self.data[idx].strip()
            self.data[idx] = re.sub(r'[\n\t]','',self.data[idx])
            if '=' in self.data[idx]:
                self.data[idx] = self.data[idx].split('=')[1]
            
            if '\\' in self.data[idx]:
                self.data[idx] = self.data[idx].replace('\\','')
                locs = locs + self.sformat(idx+1)
            
            locs = locs + self.data[idx].split(',')
            for i,l in enumerate(locs):
                locs[i] = re.sub(r'^\s+','',locs[i])
                locs[i] = re.sub(r'\s+$','',locs[i])
            return locs
                         
    
    def read_file(self):
        self.raw_data = []
        with open(self.file) as f:
            for line in f:
                self.raw_data.append(line.rstrip())
    
    def get_data(self):
        self.data = []
        
        for idx,line in enumerate(self.raw_data):
            if 'DOMAIN:' in line:
                fidx = idx
                break
        for idx,line in enumerate(self.raw_data[fidx:]):
            if re.search(r'^\s{2}END',line):
                lidx = fidx + idx
                break
        self.data = self.raw_data[fidx:lidx]
        
    def get_boundaries(self):
        self.boundaries = {}
        fidx = []
        lidx = []
        for idx,line in enumerate(self.data):
            if 'BOUNDARY:' in line:
                fidx.append(idx)
            if re.search(r'^\s{4}END',line):
                lidx.append(idx)
                
        for fid in fidx:
            for lid in lidx:
                if lid > fid:
                    self.boundaries[self.data[fid].split(': ')[1]] = self.data[fid:lid]
                    break
     
    def create_boundaries(self):
        for bnd in self.boundaries:
            self.boundary(bnd,self,self.data)

        
path = 'd:/BW_ES/P048_ELEC_FLAP_EGR_CHT/04_CFX_Pre/dom_and_if_data2.ccl'
name = 'FLD_GAS'
mydom = domain(name,path)

