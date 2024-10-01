#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import seaborn as sns
import pandas as pd
from pandas import DataFrame as df
from pandas import Series as s


# In[4]:


names = ['DEMOGRAPHICS','REFERRAL','IMAGING','DIAGNOSIS','CANCER CARE PLAN','Staging','Surgery&other procedures','Pathology Details','chemotheropy & other drugs','Radiotherapy(Teletherapy)']
patient=pd.read_excel('Downloads/cancer_data4.xlsx',names)


# In[5]:


f1=patient['REFERRAL']['DATE_FIRST_SEEN']-patient['REFERRAL']['REFERRAL_REQUEST_RECEIVED_DATE_DF']


# In[6]:


f1


# In[23]:


df2 = pd.read_excel("Downloads/cancer_data4.xlsx", sheet_name='REFERRAL')


# In[25]:


# Convert both columns to datetime format
df2['REFERRAL_REQUEST_RECEIVED_DATE_DF'] = pd.to_datetime(df2['REFERRAL_REQUEST_RECEIVED_DATE_DF'])
df2['REFERRAL_DESION_DATE'] = pd.to_datetime(df2['REFERRAL_DESION_DATE'])

# Calculate the difference between the two dates
date_diff = df2['REFERRAL_DESION_DATE'] - df2['REFERRAL_REQUEST_RECEIVED_DATE_DF']


# In[26]:


df2


# In[28]:


# Convert both columns to datetime format
df2['REFERRAL_REQUEST_RECEIVED_DATE_DF'] = pd.to_datetime(df2['REFERRAL_REQUEST_RECEIVED_DATE_DF'])
df2['REFERRAL_DESION_DATE'] = pd.to_datetime(df2['REFERRAL_DESION_DATE'])

# Calculate the difference between the two dates
df2['date_diff'] = df2['REFERRAL_DESION_DATE'] - df2['REFERRAL_REQUEST_RECEIVED_DATE_DF']

# Display the difference
print(df2['date_diff'])


# In[30]:


# Convert the 'REFERRAL_DESION_DATE' and 'REFERRAL_REQUEST_RECEIVED_DATE_DF' columns to datetime
patient['REFERRAL_DESION_DATE'] = pd.to_datetime(patient['REFERRAL']['REFERRAL_DESION_DATE'])
patient['REFERRAL_REQUEST_RECEIVED_DATE_DF'] = pd.to_datetime(patient['REFERRAL']['REFERRAL_REQUEST_RECEIVED_DATE_DF'])

# Calculate the difference between the two dates
f2 = patient['REFERRAL']['REFERRAL_DESION_DATE'] - patient['REFERRAL']['REFERRAL_REQUEST_RECEIVED_DATE_DF']

# Display the result
print(f2)


# In[ ]:





# In[32]:


df1=df(f1)


# In[33]:


import datetime


# In[34]:


f3=pd.to_timedelta(f1)


# In[36]:


print(f3)


# In[37]:


f2=patient['REFERRAL']['REFERRAL_REQUEST_RECEIVED_DATE_DF']-patient['REFERRAL']['REFERRAL_DESION_DATE']


# In[38]:


print(f2)


# In[39]:


f3=patient['REFERRAL']['WAITING_TIME_ADJUSTMENT(FIRST_SEEN)_strg']


# In[40]:


print(f3)


# In[41]:


days = f2.astype('timedelta64[D]').astype(int)
hours = f2.astype('timedelta64[h]').astype(int)-days*24


# In[42]:


print(days.astype(str))


# In[43]:


print(hours)


# In[45]:


r1=days.astype(str) + '.' + hours.astype(str)


# In[46]:


print(r1)


# In[62]:


df2=df(f3)


# In[63]:


f3.to_csv('time adjustment.csv')


# In[61]:


f4=pd.read_csv('Downloads/time adjustment.csv')


# In[64]:


df3.dtypes


# In[ ]:





# In[55]:


df2.to_excel('WAITING_TIME_ADJUSTMENT(FIRST_SEEN)_strg.xlsx')


# In[58]:


df3 = pd.read_excel('time adjustment.xlsx')


# In[51]:


df3


# In[66]:


days = df3.astype('object[D]').astype(int)


# In[56]:


type(f4)


# In[52]:


f4


# In[40]:


names = ['DEMOGRAPHICS','REFERRAL','IMAGING','DIAGNOSIS','CANCER CARE PLAN','Staging','Surgery&other procedures','Pathology Details','chemotheropy & other drugs','Radiotherapy(Teletherapy)','Radiotherapy(Brachytherapy)','Clinical Status Assesment','Death Details']
patient1=pd.read_excel('/home/rallypoint/Downloads/deceased_pat(1).xlsx',names)


# In[71]:


f2=patient1['REFERRAL']['REFERRAL_REQUEST_RECEIVED_DATE_DF']-patient1['REFERRAL']['REFERRAL_DESION_DATE']


# In[72]:


f2


# In[175]:


days = f2.astype('timedelta64[D]').astype(int)
hours = f2.astype('timedelta64[h]').astype(int)-days*24


# In[75]:


days


# In[211]:


days = f2.astype('timedelta64[D,h]').astype(int)


# In[76]:


hours


# In[176]:


reff_req_decs=days.astype(str) + '.' + hours.astype(str)


# In[214]:


df(reff_req_decs).rename(columns={0:"reff_req_decs_delay"})


# In[80]:


f3=patient1['REFERRAL']['WAITING_TIME_ADJUSTMENT(FIRST_SEEN)_strg']


# In[81]:


f3


# In[6]:


f3=pd.read_excel('/home/rallypoint/Downloads/time adjustment.xlsx','Sheet1')


# In[84]:


f3


# In[89]:


g1=f3['WAITING_TIME_ADJUSTMENT(FIRST_SEEN)_strg']


# In[105]:


np.timedelta64(g1)


# In[99]:





# In[ ]:


days = g1.astype('timedelta64[D]').astype(int)
hours = g1.astype('timedelta64[h]').astype(int)-days*24


# In[107]:


ref_imag=patient1['REFERRAL']['DATE_FIRST_SEEN']-patient1['IMAGING']['CLINICAL_INTERVENTION_DATES(CANCER_IMAGING)']


# In[179]:


ref_imag1=ref_imag.dropna()

days = ref_imag1.astype('timedelta64[D]').astype(int)
hours = ref_imag1.astype('timedelta64[h]').astype(int)-days*24

reff_imag=days.astype(str) + '.' + hours.astype(str)
reff_imag


# In[111]:


ref_diag=patient1['REFERRAL']['DATE_FIRST_SEEN']-patient1['DIAGNOSIS']['DIAGNOSIS DATE (CANCER)']


# In[180]:


ref_diag1=ref_diag.dropna()

days = ref_diag1.astype('timedelta64[D]').astype(int)
hours = ref_diag1.astype('timedelta64[h]').astype(int)-days*24

ref_diag=days.astype(str) + '.' + hours.astype(str)
ref_diag


# In[118]:


cncr_cr_pln_ref=(patient1['CANCER CARE PLAN']['MULTIDISCIPLINARY TEAM DISCUSSION DATE']-patient1['REFERRAL']['DATE_FIRST_SEEN'])+(patient1['CANCER CARE PLAN']['CARE PLAN AGREED DATE']-patient1['REFERRAL']['DATE_FIRST_SEEN'])


# In[181]:


cncr_cr_pln_ref1=cncr_cr_pln_ref.dropna()

days = cncr_cr_pln_ref1.astype('timedelta64[D]').astype(int)
hours = cncr_cr_pln_ref1.astype('timedelta64[h]').astype(int)-days*24

cncr_cr_pln_ref=days.astype(str) + '.' + hours.astype(str)
cncr_cr_pln_ref


# In[123]:


surj_procd_reff=(patient1['Surgery&other procedures']['DECISION TO TREAT DATE (SURGERY)']-patient1['REFERRAL']['DATE_FIRST_SEEN'])+(patient1['REFERRAL']['DATE_FIRST_SEEN']-patient1['Surgery&other procedures']['PROCEDURE DATE'])+(patient1['Surgery&other procedures']['DISCHARGE DATE (HOSPITAL PROVIDER SPELL)']-patient1['REFERRAL']['DATE_FIRST_SEEN'])


# In[182]:


surj_procd_reff1=surj_procd_reff.dropna()

days = surj_procd_reff1.astype('timedelta64[D]').astype(int)
hours = surj_procd_reff1.astype('timedelta64[h]').astype(int)-days*24

surj_procd_reff=days.astype(str) + '.' + hours.astype(str)
surj_procd_reff


# In[126]:


path_rec_invest_reff=(patient1['Pathology Details']['SAMPLE RECEIPT DATE']-patient1['REFERRAL']['DATE_FIRST_SEEN'])+(patient1['Pathology Details']['INVESTIGATION RESULT DATE']-patient1['REFERRAL']['DATE_FIRST_SEEN'])


# In[183]:


path_rec_invest_reff1=path_rec_invest_reff.dropna()

days = path_rec_invest_reff1.astype('timedelta64[D]').astype(int)
hours = path_rec_invest_reff1.astype('timedelta64[h]').astype(int)-days*24

path_rec_invest_reff=days.astype(str) + '.' + hours.astype(str)
path_rec_invest_reff


# In[129]:


chemo_descn_reff=(patient1['chemotheropy & other drugs']['DECISION TO TREAT DATE (ANTI-CANCER DRUG REGIMEN)']-patient1['REFERRAL']['DATE_FIRST_SEEN'])+(patient1['chemotheropy & other drugs']['START DATE (ANTI-CANCER DRUG FRACTION)']-patient1['REFERRAL']['DATE_FIRST_SEEN'])


# In[184]:


chemo_descn_reff1=chemo_descn_reff.dropna()

days = chemo_descn_reff1.astype('timedelta64[D]').astype(int)
hours = chemo_descn_reff1.astype('timedelta64[h]').astype(int)-days*24

chemo_descn_reff=days.astype(str) + '.' + hours.astype(str)
chemo_descn_reff


# In[188]:


radio_descn_reff=(patient1['Radiotherapy(Teletherapy)']['DECISION TO TREAT DATE (TELETHERAPY TREATMENT COURSE)']-patient1['REFERRAL']['DATE_FIRST_SEEN'])+(patient1['Radiotherapy(Teletherapy)']['START DATE (TELETHERAPY TREATMENT COURSE)']-patient1['REFERRAL']['DATE_FIRST_SEEN'])


# In[190]:


radio_descn_reff1=radio_descn_reff.dropna()

days = radio_descn_reff1.astype('timedelta64[D]').astype(int)
hours = radio_descn_reff1.astype('timedelta64[h]').astype(int)-days*24

radio_descn_reff=days.astype(str) + '.' + hours.astype(str)
radio_descn_reff


# In[193]:


rad_bracl_reff=(patient1['Radiotherapy(Brachytherapy)']['DECISION TO TREAT DATE (BRACHYTHERAPY TREATMENT COURSE)']-patient1['REFERRAL']['DATE_FIRST_SEEN'])+((patient1['Radiotherapy(Brachytherapy)']['END DATE (BRACHYTHERAPY TREATMENT COURSE)']-patient1['Radiotherapy(Brachytherapy)']['START DATE (BRACHYTHERAPY TREATMENT COURSE)'])+(patient1['Radiotherapy(Brachytherapy)']['START DATE (BRACHYTHERAPY TREATMENT COURSE)']-patient1['REFERRAL']['DATE_FIRST_SEEN']))


# In[195]:


rad_bracl_reff1=rad_bracl_reff.dropna()

days = rad_bracl_reff1.astype('timedelta64[D]').astype(int)
hours = rad_bracl_reff1.astype('timedelta64[h]').astype(int)-days*24

rad_bracl_reff=days.astype(str) + '.' + hours.astype(str)
rad_bracl_reff


# In[139]:


patient1['Radiotherapy(Brachytherapy)']['END DATE (BRACHYTHERAPY TREATMENT COURSE)']-patient1['Radiotherapy(Brachytherapy)']['START DATE (BRACHYTHERAPY TREATMENT COURSE)']


# In[140]:


patient1['Radiotherapy(Brachytherapy)']['START DATE (BRACHYTHERAPY TREATMENT COURSE)']-patient1['REFERRAL']['DATE_FIRST_SEEN']


# In[149]:


clincl_stats_asses=(patient1['Clinical Status Assesment']['CLINICAL STATUS ASSESSMENT DATE (CANCER)']-patient1['REFERRAL']['DATE_FIRST_SEEN'])


# In[196]:


clincl_stats_asses1=clincl_stats_asses.dropna()

days = clincl_stats_asses1.astype('timedelta64[D]').astype(int)
hours = clincl_stats_asses1.astype('timedelta64[h]').astype(int)-days*24

clincl_stats_asses=days.astype(str) + '.' + hours.astype(str)
clincl_stats_asses


# In[152]:


patnt_death_reff=(patient1['Death Details']['PERSON DEATH DATE']-patient1['REFERRAL']['DATE_FIRST_SEEN'])


# In[197]:


patnt_death_reff1=patnt_death_reff.dropna()


days = patnt_death_reff1.astype('timedelta64[D]').astype(int)
hours = patnt_death_reff1.astype('timedelta64[h]').astype(int)-days*24

patnt_death_reff=days.astype(str) + '.' + hours.astype(str)
patnt_death_reff


# In[226]:


dg1=df(reff_req_decs).rename(columns={0:"reff_req_decs_delay"})


# In[253]:


dg1


# In[229]:


dg2=df(reff_imag).rename(columns={0:"reff_imag_delay"})


# In[230]:


dg2


# In[231]:


dg3=df(ref_diag).rename(columns={0:"ref_diag_delay"})
dg3


# In[232]:


dg4=df(cncr_cr_pln_ref).rename(columns={0:"cncr_cr_pln_ref_delay"})
dg4


# In[233]:


dg5=df(surj_procd_reff).rename(columns={0:"surj_procd_reff_delay"})
dg5


# In[234]:


dg6=df(path_rec_invest_reff).rename(columns={0:"path_rec_invest_reff_delay"})
dg6


# In[235]:


dg7=df(chemo_descn_reff).rename(columns={0:"chemo_descn_reff_delay"})
dg7


# In[236]:


dg8=df(radio_descn_reff).rename(columns={0:"radio_descn_reff_delay"})
dg8


# In[237]:


dg9=df(rad_bracl_reff).rename(columns={0:"rad_bracl_reff_delay"})
dg9


# In[238]:


dg10=df(clincl_stats_asses).rename(columns={0:"clincl_stats_asses_delay"})
dg10


# In[240]:


dg11=df(patnt_death_reff).rename(columns={0:"patnt_death_reff_delay"})
dg11


# In[260]:


frames = [dg1, dg2, dg3, dg4, dg5, dg6, dg7, dg8, dg9, dg10, dg11]
dgg=pd.concat(frames,axis=1,join_axes=[dg1.index])


# In[263]:


dgg.to_excel('delay.xlsx',sheet_name='delays')


# In[271]:


delay1=patient1['DIAGNOSIS']['DIAGNOSIS DATE (CANCER)']-patient1['REFERRAL']['REFERRAL_DESION_DATE']
ds1=df(delay1).rename(columns={0:"reff_diagn_date_delay"})
ds1


# In[272]:


delay2=patient1['REFERRAL']['REFERRAL_REQUEST_RECEIVED_DATE_DF']-patient1['REFERRAL']['REFERRAL_DESION_DATE']
ds2=df(delay2).rename(columns={0:"reff_requ_date_delay"})
ds2


# In[277]:


delay3=patient1['IMAGING']['CLINICAL_INTERVENTION_DATES(CANCER_IMAGING)']-patient1['REFERRAL']['REFERRAL_REQUEST_RECEIVED_DATE_DF']
ds3=df(delay3).rename(columns={0:"clinicl_reff_requ_date_delay"})
ds3=ds3.dropna()
ds3


# In[278]:


delay4=patient1['REFERRAL']['DATE_FIRST_SEEN']-patient1['IMAGING']['CLINICAL_INTERVENTION_DATES(CANCER_IMAGING)']
ds4=df(delay4).rename(columns={0:"dt_frst_clinicl_intervntn_date_delay"})
ds4=ds4.dropna()
ds4


# In[279]:


delay5=patient1['CANCER CARE PLAN']['MULTIDISCIPLINARY TEAM DISCUSSION DATE']-patient1['REFERRAL']['DATE_FIRST_SEEN']
ds5=df(delay5).rename(columns={0:"mltidisplnry_discsn_date_frst_delay"})
ds5=ds5.dropna()
ds5


# In[280]:


delay6=patient1['CANCER CARE PLAN']['CARE PLAN AGREED DATE']-patient1['CANCER CARE PLAN']['MULTIDISCIPLINARY TEAM DISCUSSION DATE']
ds6=df(delay6).rename(columns={0:"cr_pln_agre_mltidisplnry_discsn_date_delay"})
ds6=ds6.dropna()
ds6


# In[281]:


frames1 = [ds1,ds2,ds3,ds4,ds5,ds6]
dss=pd.concat(frames1,axis=1,join_axes=[ds1.index])
dss


# In[282]:


dss.to_excel('improved_delay.xlsx',sheet_name='delays')


# In[9]:


gf=pd.read_excel('/home/rallypoint/Downloads/secondLevelDelay.xlsx','Sheet1')
gf


# In[10]:


import sklearn as skl


# In[11]:


from sklearn import datasets, linear_model


# In[44]:


names = ['DEMOGRAPHICS','REFERRAL','IMAGING','DIAGNOSIS','CANCER CARE PLAN','Staging','Surgery&other procedures','Pathology Details','chemotheropy & other drugs','Radiotherapy(Teletherapy)','Radiotherapy(Brachytherapy)','Clinical Status Assesment','Death Details']
patient1=pd.read_excel('/home/rallypoint/Downloads/deceased_pat.xlsx',names)


# In[45]:


delay11=patient1['REFERRAL']['REFERRAL_DESION_DATE']-patient1['DIAGNOSIS']['DIAGNOSIS DATE (CANCER)']


# In[47]:


delay11


# In[46]:


delay12=patient1['REFERRAL']['REFERRAL_REQUEST_RECEIVED_DATE_DF']-patient1['REFERRAL']['REFERRAL_DESION_DATE']


# In[48]:


delay12


# In[49]:


delay13=patient1['IMAGING']['CLINICAL_INTERVENTION_DATES(CANCER_IMAGING)']-patient1['REFERRAL']['REFERRAL_REQUEST_RECEIVED_DATE_DF']


# In[50]:


delay13


# In[33]:


delay14=patient1['REFERRAL']['DATE_FIRST_SEEN']-patient1['IMAGING']['CLINICAL_INTERVENTION_DATES(CANCER_IMAGING)']


# In[34]:


delay14


# In[53]:


delay15=patient1['CANCER CARE PLAN']['MULTIDISCIPLINARY TEAM DISCUSSION DATE']-patient1['REFERRAL']['DATE_FIRST_SEEN']
delay15


# In[55]:


delay16=patient1['CANCER CARE PLAN']['CARE PLAN AGREED DATE']-patient1['CANCER CARE PLAN']['MULTIDISCIPLINARY TEAM DISCUSSION DATE']


# In[56]:


delay16


# In[57]:


ds11=df(delay11).rename(columns={0:"Delay1_decisionDate&DiagnosisDate"})
ds11=ds11.dropna()

ds12=df(delay12).rename(columns={0:"delay2_ReceivedDate&decisionDate"})
ds12=ds12.dropna()

ds13=df(delay13).rename(columns={0:"delay3_clinicalIntrvnt&ReqReceivedDate"})
ds13=ds13.dropna()

ds14=df(delay14).rename(columns={0:"delay4_dateFirstSeen&ClinicalIntervention"})
ds15=ds15.dropna()

ds15=df(delay15).rename(columns={0:"delay5_discussionDate&DateFirstSeen"})
ds15=ds15.dropna()

ds16=df(delay16).rename(columns={0:"delay6_carePlanAgreedDate&DiscussionDate"})
ds16=ds16.dropna()


# In[ ]:





# In[58]:


frames11 = [ds11,ds12,ds13,ds14,ds15,ds16]
dss1=pd.concat(frames11,axis=1,join_axes=[ds11.index])
dss1


# In[ ]:


dss1.to_excel('deseased_delay.xlsx',index=None)

