import numpy as np
import pandas as pd
#import matplotlib


class file:
     def __init__(self, new, previous):
             self.new=new
             self.previous=previous        
     def readMortality(sex):  #read data
             Location = r'/users/yi-peichan/desktop/pricing_program/mortality.csv'
             df = pd.read_csv(Location)
             mMortality=df['male']
             fMortality=df['female']
             if sex==0:
                  return mMortality
             else:return fMortality

##### basic information
age=25#input("Test_age= ")
#age=int(age)
#GP=0.077 #=[]

sex=0 #input("male=0, female=1: ")
ppp=20 #input("_ppp, premium payment period= ")
pt=105-age

##### rate
aIR=2.65/100 #raw_input("Test_age= ") #Assumed Interest Rate, 預定利率
ir=2.5/100 # reserve ratio 責準利率
ii=2.97/100 #投報率
ipv=2.97/100 #折現率
iKid=1.056 #則準(15歲以下退還倍數)
v=1/(1+aIR) # discount factor


##### policy
unit=1000
channel=1
exchange=30 #exchange rate
## age distribution of policyholders for profit analysis 代表年齡對照表
ageDist=[]
for i in range(0, 55):
     ageDist.append(np.floor(i/10))

################## Pricing
##### Mortality_pricing
mMortality=file.readMortality(0)
fMortality=file.readMortality(1)
popSurv=[]   #population survival (year beginning)
popDeath=[] #population death
popSurv.append(1)

if sex==0:
    popDeath.append(mMortality[age])
    for i in range(0,pt-1):
        popSurv.append(popSurv[i]-popDeath[i])   #survival at the end of the year 期末生存人數
        popDeath.append(mMortality[age+i+1]*popSurv[i+1])
else:
    popDeath.append(fMortality[age])
    for i in range(0,pt-1):
        popSurv.append(popSurv[i]-popDeath[i]) #survival at the end of the year 期末生存人數
        popDeath.append(mMortality[age+i+1]*popSurv[i+1])


###########################################################
##Mortality CDMN
mLx=[0]*112
mDx=[0]*112
mC=[0]*112
mD=[0]*112
mM=[0]*112
mN=[0]*112
fLx=[0]*112
fDx=[0]*112
fC=[0]*112
fD=[0]*112
fM=[0]*112
fN=[0]*112

mLx[0]=fLx[0]=10000000
if sex==0:
    for i in range(0,111):
        mDx[i]=(mLx[i]*mMortality[i])
        mLx[i+1]=(mLx[i]-mDx[i])
        mC[i]=mDx[i]*v**(i+0.5)
        mD[i]=mLx[i]*v**(i)
    for i in range(110,-1,-1):
        mM[i]=mC[i]+mM[i+1]
        mN[i]=mD[i]+mN[i+1]
    Dx=mD[age]
    Mx=mM[age]
    M99=mM[105]
    Nx=mN[age]
    Nx20=mN[age+20]
    px20=Mx/(Nx-Nx20)               #其他變數在修正制保費部分
else:
    for i in range(0,111):
        fDx[i]=(fLx[i]*fMortality[i])
        fLx[i+1]=(fLx[i]-fDx[i])
        fC[i]=fDx[i]*v**(i+0.5)
        fD[i]=fLx[i]*v**(i)    
    for i in range(110,-1,-1):
        fM[i]=fC[i]+fM[i+1]
        fN[i]=fD[i]+fN[i+1]
    Dx=mD[age]
    Mx=mM[age]
    M99=mM[105]
    Nx=mN[age]
    Nx20=mN[age+20]
    px20=Mx/(Nx-Nx20)

###########################################################
##### Benefit
deathB=[0]*pt #death benefit
survB=[0]*pt #annuity 生存保險金
pricingV=[0]*pt #policy value in Benefit 保價
diabilityB=[0]*pt #total diability 完全殘廢
# 因計算surNP會須多一年
popDeath.append(0) 
popSurv.append(0) 
survB.append(0)

##########################################################
#Pricing for Modified Reserve Standards 修正制純保費
survP=0
survPlist=[0]*(pt+1)  ##policy value for pricing 算保價用 
aDue=0
aDuelist=[0]*(pt+1) 
termpB=[0]*(pt+1)   #祝壽金 Endowment after the last policy year in Benefit
termP = 0
termPlist=[0]*(pt+1) # Endowment for determing policy value 算保價用 
pricingV=[0]*(pt+1) #pricing 保價


#身故全殘_保價deathPV
loading=10/100
deathPV=0             #for pricing death V
deathPVlist=[0]*(pt+1)    #for pricing death V
NP=0
deathBV=0  #for Benefit death V
deathBV=[0]*(pt)  #for Benefit death V
pricingVs=[0]*(pt+1) #pricing 保價 含年金 因為deathBV最後一年所以+1 但最後會蓋掉
p1=0
p2=0
p1D=0
NPt=2
GP=0
j=0 #計算收斂
while True:
     j=j+1
     termpB[pt-1]= 1.06*np.ceil(GP*unit)/unit*ppp    
     for i in range(0,pt):
          if i>0:
               pricingVs[i]=pricingV[i]+termpB[i-1]+survB[i-1]  #pricing 保價含生存保險金
               pricingV[i]=max((deathPVlist[i]+termPlist[i]+survPlist[i])-aDuelist[i]*p2,0)
               if i<=ppp-1:deathBV[i]=(pricingV[i]+pricingVs[i+1]+p2)/2
               else: deathBV[i]=(pricingV[i]+pricingVs[i+1])/2
               #else: deathBV[i]=(pricingV[i]+survB[i]+termpB[i])/2
          else: #i=0
               pricingV[i]=max((deathPVlist[i]+termPlist[i]+survPlist[i])-aDuelist[i]*NP,0)
               deathBV[i]=(pricingV[i]+pricingVs[i+1]+p1)/2     
          if i<=ppp-1:  ###death benefit with premium included to take max.
               deathB[i]=max(deathBV[i],1.06*np.ceil(GP*unit)/unit*(i+1),3)
               survB[i]=np.ceil(GP*unit*0.05)/unit
          else:
               deathB[i]=max(deathBV[i],1.06*np.ceil(GP*unit)/unit*ppp,1)
               survB[i]=np.ceil(GP*unit*0.5)/unit
     deathBV[pt-1]=(pricingV[pt-1]+termpB[pt-1]+survB[pt-1])/2  
     for i in range(pt-1,-1,-1):
          survP= (survB[i]*(popSurv[i]-popDeath[i])*v+survPlist[i+1]*popSurv[i+1]*v)/popSurv[i]
          termP=(termpB[i]*(popSurv[i]-popDeath[i])*v+termPlist[i+1]*popSurv[i+1]*v)/popSurv[i] 
          if i>=ppp: aDue=0
          else: aDue=(popSurv[i]+aDue*popSurv[i+1]*v)/popSurv[i]
          aDuelist[i]=aDue
          termPlist[i]=termP
          survPlist[i]=survP     
          deathPV= (deathB[i]*popDeath[i]*v**0.5+deathPVlist[i+1]*popSurv[i+1]*v)/popSurv[i]  ##pricing death value of the policy   
          deathPVlist[i]=deathPV
     ########NP items
     uPV=0
     survNP=survP/aDue   #NP of annuity
     termPNP=termP/aDue  #termPNP: 祝壽 np of endowment premium 
     p1SAH=p2SAH=npSAH=survNP  
     ##NP items                
     deathNP=deathPV/aDue
     npD=deathNP+uPV+termPNP #uPV: 未到期 unexpired premium value; termPNP: 祝壽 endowment premium np
     pfD=(deathPVlist[0]+termPlist[0])-(deathPVlist[1]+termPlist[1])*popSurv[1]*v
     h=deathPV*Dx/(Mx-M99)
     h20Px=h*px20
     if ppp==1:
          p1D=pfD+npD
          p2D=0
     else:
          p2D=(aDue*npD-p1D)/(aDue-1)
          if npD>h20Px:p1D=npD-h20Px+pfD
          else: p1D=pfD  
     p1=p1SAH+p1D
     p2=p2SAH+p2D
     NP=(deathPVlist[0]+termP+survP)/aDue
     GP=NP/(1-loading)
     if j<=100:
          print(NP)
     #error=np.absolute(GP-GPt)     
     error=np.absolute(NP-NPt)
     if error<0.00000001:
          print('NP=',NP)
          print('GP=',NP/(1-loading))
          break
     elif j>2500:
          print('The net premium does not converge')
          break
     else:
          NPt=NP


          

 








