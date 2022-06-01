import os 

"""
CommandList:
    open : all show
    cd : number or dataname
    ls : show 
    cat : data show (yellow color)
    
    cls,clear : clear
    
"""


KeyPass = []
class show(object):

    def __init__(self,Dict):
        if len(KeyPass) != 0:
            Dict = self.PassRoute(Dict=Dict)
        self.dict_keys = Dict.keys()
        self.Dict = Dict
            
    def OPEN(self):
        for dKeys in list(self.dict_keys):
            pDict = self.Dict[dKeys]
            self.KEYPASS = []
            self.KEYPASS.append(dKeys)

            self.DICTCOUNTER(DICT=pDict,KEYS=dKeys)
        pass

    def SEARCH(self,SearchWord,KeyName):
        
        self.SearchWord = SearchWord
        self.KeyName = KeyName
        self.HitDict = []

        for dKeys in list(self.dict_keys):
            pDict = self.Dict[dKeys]
            self.KEYPASS = []
            self.KEYPASS.append(dKeys)
            self.DICTCOUNTER(DICT=pDict,KEYS=dKeys,Search=True)
        
        return self.HitDict

    def KEYWORD(self):
        
        self.KEYWORD = []
        for dKeys in list(self.dict_keys):
            pDict = self.Dict[dKeys]
            self.KEYPASS = []
            self.KEYPASS.append(dKeys)
            self.DICTCOUNTER(DICT=pDict,KEYS=dKeys,KEYWORD=True)
        
        return self.KEYWORD
        
    
    def PassRoute(self,Dict):
        count,count2 = 0,1
        dic = Dict
        for i in KeyPass:
            if count == 0:
                dic2 = dic[i]
                count += 1 
            elif count == count2:
                dic2 = dic2[i]
                count2 += 1
            elif count != count2:
                dic2 = dic2[i]
                count += 1 
        Dict = dic2
        
        return Dict


    def DICTCOUNTER(self,DICT,KEYS,Search=False,KEYWORD=False):
        
        if type(DICT) is dict:
            dict_keys = DICT.keys()
            for dKeys in list(dict_keys):
                DICT2 = DICT[dKeys]
                self.KEYPASS.append(dKeys)
                self.DICTCOUNTER(DICT=DICT2,KEYS=dKeys,Search=Search,KEYWORD=KEYWORD)
            pass
        else:
            #================================================================

            if Search:

                for KEYNAME,SEARCHWORD in zip(self.KeyName,self.SearchWord):
                    if str(KEYS) == str(KEYNAME) and str(DICT) == str(SEARCHWORD):
                        self.HitDict.append(list(self.KEYPASS)) 
                pass
            
            elif KEYWORD:
                self.KEYWORD.append(KEYS)
                pass 
            
            else:
                print('{keys} : {body}\n'.format(keys=KEYS,body=DICT))
                pass 


            #================================================================
           
            FIRSTKEYS = self.KEYPASS[0]
            self.KEYPASS.clear()
            self.KEYPASS.append(FIRSTKEYS)
            pass 
        pass 

class DictCommand(object):
    
    def __init__(self,Dict,Command):
        if Command[0] == 'ls':
            self.Ls(Dict)
        elif Command[0] == 'cd':
            self.Cd(Dict,cdCMD=Command[1])
        elif Command[0] == 'cat':
                self.Cat(Dict,catDMD=Command[1])
                        
        elif Command[0] == 'back':
            if 0 < len(KeyPass):
                del KeyPass[len(KeyPass)-1]


    def PassRoute(self,Dict):
        count,count2 = 0,1
        dic = Dict
        for i in KeyPass:
            if count == 0:
                dic2 = dic[i]
                count += 1 
            elif count == count2:
                dic2 = dic2[i]
                count2 += 1
            elif count != count2:
                dic2 = dic2[i]
                count += 1 
        dKeys = list(dic2.keys())
        Dict = dic2
        
        return dKeys,Dict


    def Ls(self,Dict):
        if len(KeyPass) == 0:
            dKeys = list(Dict.keys())
        else:
            Roter = self.PassRoute(Dict=Dict)
            dKeys = Roter[0]
            Dict = Roter[1]
        
        keyCount = []
        for d in dKeys:
            try:
                Dict[d].keys()
                keyCount.append(d)
            except:
                coloring = '\033[33m{}\033[0m'.format(d)
                keyCount.append(coloring)
        #print('   '.join(keyCount))
        count = 0 
        for i in keyCount:
            print("[{Count}] {KeyName}".format(Count=count,KeyName=i))
            
            count +=1

    def Cd(self,Dict,cdCMD):
        
        if cdCMD.isdecimal(): 

            if len(KeyPass) == 0:
                if len(list(Dict.keys())) <= int(cdCMD):
                    print("Over Num !!")
                    return 0

                cdCMD = str(list(Dict.keys())[int(cdCMD)])
            else:
                nDict = self.PassRoute(Dict=Dict)[1]
                if len(list(nDict.keys())) <= int(cdCMD):
                    print("Over Num !!")
                    return 0

                if len(nDict) != 0:
                    cdCMD = str(list(nDict.keys())[int(cdCMD)])
            pass 
        try:

            if len(KeyPass) == 0:
                
                cDict = Dict[str(cdCMD)]
            else:

                cDict = self.PassRoute(Dict=Dict)[1][str(cdCMD)]

            cDict.keys()
            KeyPass.append(str(cdCMD))
        except:
            print('No Data key !!')
        pass 

    def Cat(self,Dict,catDMD):
        if catDMD.isdecimal():
            if len(KeyPass) == 0:
                if len(list(Dict.keys())) <= int(catDMD):
                    print("Over Num !!")
                    return 0

                catDMD = str(list(Dict.keys())[int(catDMD)])
            else:
                nDict = self.PassRoute(Dict=Dict)[1]
                if len(list(nDict.keys())) <= int(catDMD):
                    print("Over Num !!")
                    return 0

                nDict = self.PassRoute(Dict=Dict)[1]
                if len(nDict) != 0:
                    catDMD = str(list(nDict.keys())[int(catDMD)])
            pass 

        try:
            if len(KeyPass) == 0:
                cDict = Dict[str(catDMD)]
            else:
                cDict = self.PassRoute(Dict=Dict)[1][str(catDMD)]
            print(cDict)
        except:
            print('No Data Key !!')
            pass  



class DictEditor(object):
     
    def __init__(self,Dict,Path=None):
        self.kDict = Dict.keys()
        self.Path = Path
        self.Dict = Dict

    
    def PassRoute(self):

        path = self.Path.split("/")
        count,count2 = 0,1
        dic = self.Dict
        for i in path:
            if count == 0:
                dic2 = dic[i]
                count += 1 
            elif count == count2:
                dic2 = dic2[i]
                count2 += 1
            elif count != count2:
                dic2 = dic2[i]
                count += 1 
    
        return dic2


    def DictDelete(self):
        
        DELETE_DICT_KEY_NAME = ""
        self.Dict.pop("")
        print(self.Dict)
        

        pass 
    
    def DictMkdir(self):
        path = self.Path.split("/")
        if type(path) is list:
            Dict = self.PassRoute()

        else:
            Dict = self.Dict
        try:
            Dict.keys()
            DictName = input()
            if len([i for i in DictName]) != 0:
            
                MkDict = {str(DictName):{}}

                Dict.update(MkDict)
                print(Dict)
            
            else:
                print("please in DictName !! ")
            return 0 

        except:
            print("please in DictFolder pass !!  ")
            return 0 

    def DictRename(self):
        pass  



def Controle(DICT):
    while True:
        PASS = '/'.join(KeyPass)
        IN = input('[$]INPUT /{Pass} : '.format(Pass=PASS))
        IN_SPLIT = IN.split(' ')
        if IN_SPLIT[0] == 'open':
            show(DICT).OPEN()

        elif IN_SPLIT[0] == 'ls':
            DictCommand(Dict=DICT,Command=['ls'])

        elif IN_SPLIT[0] == 'cd':
            if len(IN_SPLIT) == 2:
                if IN_SPLIT[1] == '../' or IN_SPLIT[1] == '..':
                    DictCommand(Dict=DICT,Command=['back'])

                elif  IN_SPLIT[1] == '~' or IN_SPLIT[1] == '~/':
                    KeyPass.clear() 

                else:
                    DictCommand(Dict=DICT,Command=['cd',IN_SPLIT[1]])
        
        elif IN_SPLIT[0] == 'cat':
            if len(IN_SPLIT) == 2:
                DictCommand(Dict=DICT,Command=['cat',IN_SPLIT[1]])
            pass
                    

        elif IN_SPLIT[0] == 'clear' or IN_SPLIT[0] == 'cls':
                os.system('clear')

        elif IN_SPLIT[0] == 'q!' or IN_SPLIT[0] == 'quit' or IN_SPLIT[0] == '!':
            break

def SelectPass(Dict,Path):

    if type(Path) is list:

        rDict = {}
        for i in Path:
            PATH = i.split('/')
            DATANAME = PATH[len(PATH)-1]
            count,count2 = 0,1
            dic = Dict
            try:
                for i in PATH:
                    if count == 0:
                        dic2 = dic[i]
                        count += 1 
                    elif count == count2:
                        dic2 = dic2[i]
                        count2 += 1
                    elif count != count2:
                        dic2 = dic2[i]
                        count += 1 
                i = dic2
                uDict = {str(DATANAME):i}
                rDict.update(uDict)
            except:
                print("Specified path does not exist")
                pass 
        
        return rDict
        quit()

    PATH = Path.split('/')
    DATANAME = PATH[len(PATH)-1]
    count,count2 = 0,1
    dic = Dict
    try:
        for i in PATH:
            if count == 0:
                dic2 = dic[i]
                count += 1 
            elif count == count2:
                dic2 = dic2[i]
                count2 += 1
            elif count != count2:
                dic2 = dic2[i]
                count += 1 
        Dict = dic2
        return {'dict':Dict,'dataname':DATANAME,'dictpass':Path}

    except:
        print('Specified path does not exist')
        pass


def DictSearch(Dict,SearchWord,KeyName):
    Key = show(Dict = Dict).KEYWORD()
    print(Key)
       
    pass 

if __name__ == "__main__":
   
    ##################################### TEST

    
    DICT = {'A1':'A_DICT','B1':{'BB':'BB_DICT','BB2':'BB2_DICT'},'C1':{'CC':{'CCC':'CCC_dict'}},'D1':{'DD':{'DDD':{'DDDD':'DDDD_dict'}},'DD2':'DD2_DICT'}}
    Controle(DICT=DICT)
    

    ######################################
