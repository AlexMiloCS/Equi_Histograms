"AM 3045 ONOMA: ALEXANDROS MILONAKIS"

class equi_histogram:
    
    def __init__(self, bins, mylist):
        self.bins = bins
        self.mylist=mylist
        self.equi_dep = []
        self.equi_wid = []

    def create_width_histogram(self):
        bin_range = (max(self.mylist) - (min(self.mylist))) / (self.bins)
        counter = 0            
        start = min(self.mylist)
        limit = round((min(self.mylist)) + bin_range, 2)
        
        for i in range(len(self.mylist)):
            if(self.mylist[i]>=limit):
                self.equi_wid.append((start, limit, counter))
                start=limit
                limit+=bin_range                
                counter=0
            counter+=1 
        return self.equi_wid
    
    def create_depth_histogram(self):
        bin_range = (len(self.mylist))//self.bins
        start_point=self.mylist[0]
        counter = 0  

        for i in range(len(self.mylist)):
            if(counter==bin_range):
                self.equi_dep.append((start_point,self.mylist[i],counter))
                start_point = self.mylist[i]
                counter=0
            counter+=1  
        return self.equi_dep   
    
    def find_estimate(self,part,whole,numtuples):
        percentage=(part)/(whole)*100
        numt = numtuples*percentage/100
        return numt

    def find_equi_diagram_pleiades(self,a,b,pointer,equi_diagram):
        if(a<equi_diagram[0][0]):
            if(b<equi_diagram[0][1]):
                estimate= self.find_estimate(b-equi_diagram[0][0],equi_diagram[pointer][1]-equi_diagram[pointer][0],self.equi_dep[pointer][2])
                return estimate
            elif(b<equi_diagram[0][0]):
                return 0
        elif(b<equi_diagram[pointer][1]):
            estimate= self.find_estimate(b-a,equi_diagram[pointer][1]-equi_diagram[pointer][0],equi_diagram[pointer][2])
            return estimate
        elif(a>equi_diagram[len(equi_diagram)-1][0]):
            if(a>=equi_diagram[len(equi_diagram)-1][1]):
                return 0
            elif(b>equi_diagram[len(equi_diagram)-1][1]):
                estimate= self.find_estimate(equi_diagram[pointer][1]-a,equi_diagram[pointer][1]-equi_diagram[pointer][0],self.equi_dep[pointer][2])
                return estimate
        else:
            estimate= self.find_estimate(equi_diagram[pointer][1]-a,equi_diagram[pointer][1]-equi_diagram[pointer][0],equi_diagram[pointer][2])       
        
        for j in range (pointer+1,len(equi_diagram)):
            if(equi_diagram[j][1] >= b):
                estimate+=self.find_estimate(b-equi_diagram[j][0],equi_diagram[j][1]-equi_diagram[j][0],equi_diagram[j][2])
                break
            estimate+=equi_diagram[j][2]
        return estimate

    def find_pleiades(self,i,b):
        counter=0
        for j in range(i,(len(self.mylist))):
            if((self.mylist[j]>=float(b))):
               break
            counter+=1
        return counter

    
    def print_pleiades(self,a,b):
        wid_est = 0
        depth_est = 0
        actual = 0
        for i in range(len(self.mylist)):
            if(self.mylist[i]>=float(a)):
                actual = self.find_pleiades(i,b)
                bin_range = (max(self.mylist) - (min(self.mylist))) / (self.bins)
                pointer2 = (int((self.mylist[i]-(min(self.mylist)))//bin_range))
                wid_est = self.find_equi_diagram_pleiades(a,b,pointer2,self.equi_wid)
                pointer= i//self.equi_dep[0][2]
                depth_est= self.find_equi_diagram_pleiades(a,b,pointer,self.equi_dep)
                break
        print("equiwidth estimated results:",wid_est)
        print("equidepth estimated results:",depth_est)
        print("actual results:",actual)
        return 