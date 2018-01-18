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
    
    def read_file(self):
        self.raw_data = []
        with open(self.file) as f:
            for line in f:
                self.raw_data.append(line.rstrip())
    
    def get_data(self):
        self.data = []
        
        for idx,line in enumerate(self.raw_data):
            if 'DOMAIN:' in line and self.name in line:
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

class boundary:
        instances = []
        def __init__(self,name,domain,data):
            self.instances.append(self)
            self.name = name
            self.domain = domain.name
            self.data = data
            
            self.get_location()
            
        def get_location(self):
            self.loc = []
            for idx,line in enumerate(self.data):
                if 'Location = ' in line:
                    fidx = idx
                    if '\\' not in line:
                        self.loc = self.sformat(line)
                        break
                    else:
                        for idx,line in enumerate(self.data[fidx:]):
                            if 'BOUNDARY CONDITIONS:' in line:
                                lidx = idx
                                break
                        self.loc = self.sformat(''.join(self.data[fidx:fidx+lidx]))
           
        def sformat(self,s):
            locs = []
            s = re.sub(r'[\n\t]','',s)
            if '=' in s:
                s = s.split('=')[1]
            if '\\' in s:
                s = s.replace('\\','')
            locs = s.split(',')
            for i,l in enumerate(locs):
                locs[i] = re.sub(r'^\s+','',locs[i])
                locs[i] = re.sub(r'\s+$','',locs[i])
                locs[i] = re.sub(r'\s+',' ',locs[i])
            return locs                       
    

# --- For testing       
#path = 'd:/BW_ES/P048_ELEC_FLAP_EGR_CHT/04_CFX_Pre/temp/doms_ifs.ccl'
#name = 'FLD_GAS'
#mydom = domain(name,path)
#
#for bnd in mydom.boundaries:
#    boundary(bnd,mydom,mydom.boundaries[bnd])

