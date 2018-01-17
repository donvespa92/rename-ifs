from domain import domain,boundary
import ccl_templates as ccl

class interface:
    instances = []
    def __init__(self,name,iftype):
        self.instances.append(self)
        self.name = name
        self.type = iftype
        self.loc_side1 = []
        self.loc_side2 = []
        self.dom1 = ""
        self.dom2 = ""
        self.newname = ""
    
class if_mainloop:  
    def __init__(self,file):
        self.file = file
        self.init_ifs()
        
        self.init_doms()
        self.init_bnds()
        self.get_if_locs()
        
    def init_ifs(self):   
        self.default_if_names = []
        with open(self.file) as f:
            for line in f:
                line = line.strip()
                if 'DOMAIN INTERFACE:' in line:
                    name = line.split(': ')[1]
                    if 'Fluid Fluid' in name:
                        iftype = 'Fluid Fluid'
                    elif 'Fluid Solid' in name:
                        iftype = 'Fluid Solid'
                    elif 'Solid Solid' in name:
                        iftype = 'Solid Solid'
                    else:
                        iftype = None
                    interface(name,iftype)
                    
    def init_doms(self):
        with open(self.file) as f:
            for line in f:
                line = line.strip()
                if 'DOMAIN:' in line:
                    name = line.split(': ')[1]
                    domain(name,self.file)
                                            
    def init_bnds(self):
        for dom in domain.instances:
            for bnd in dom.boundaries:
                boundary(bnd,dom,dom.boundaries[bnd])
                
                
    def get_if_locs(self):
        for bnd in boundary.instances:
            for i in interface.instances:
                if i.name in bnd.name:
                    if 'Side 1' in bnd.name:
                        i.loc_side1 = bnd.loc
                        i.dom1 = bnd.domain
                    elif 'Side 2' in bnd.name:
                        i.loc_side2 = bnd.loc
                        i.dom2 = bnd.domain
    
    def new_name(self,tags):
        solid = tags['solid'].upper()
        fluid = tags['fluid'].upper()
        ffif = tags['ffif'].upper()
        ssif = tags['ssif'].upper()
        fsif = tags['fsif'].upper()
        
        for i in interface.instances:
            if i.type == 'Fluid Fluid':
                i.newname = '_'.join([ffif,i.dom1[len(fluid)+1:],i.dom2[len(fluid)+1:]])
            if i.type == 'Solid Solid':
                i.newname = '_'.join([ssif,i.dom1[len(solid)+1:],i.dom2[len(solid)+1:]])
            if i.type == 'Fluid Solid':
                i.newname = '_'.join([fsif,i.dom1[len(fluid)+1:],i.dom2[len(solid)+1:]])
                
    def write(self,output):
        f = open(output,'w')
        for i in interface.instances:
            s = ccl.templates('domain_interface')
            s = s.replace('!INTERFACE_NAME!',i.newname)
            s = s.replace('!IF_TYPE!',i.type)
            s = s.replace('!SIDE1!',i.newname+' Side 1')
            s = s.replace('!SIDE2!',i.newname+' Side 2')
            s = s.replace('!BND1!',','.join(i.loc_side1))
            s = s.replace('!BND2!',','.join(i.loc_side2))
            s = s.replace('!DOM1!',i.dom1)
            s = s.replace('!DOM2!',i.dom2)
            f.write(s) 
        f.close()
                     
                
# --- For testing 
#path = 'd:/BW_ES/P048_ELEC_FLAP_EGR_CHT/04_CFX_Pre/dom_and_if_data2.ccl'
#root = if_mainloop(path)

        
