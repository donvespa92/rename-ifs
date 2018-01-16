class interface:
    def __init__(self,**options):
        self.name = options.get("name")
        self.bnd1 = options.get("bnd1")
        self.bnd2 = options.get("bnd2")


names = ['if1','if2','if3']

interfaces = {}
for name in names:
    interfaces[name] = interface(name=name,bnd1="",bnd2="")
