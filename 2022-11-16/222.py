import pandas as pd
import os

def get_certificate_subject_cn(host):
    cert = os.popen(" curl -v -k -s -N --max-time 60 'https://%s' 2>&1  | grep subject | awk -F '=' {'print $NF'}" % host).read()
    print(cert)
    return cert
df = pd.read_excel(
    r'./table/cloudfrot第二批.csv', encoding='utf-8', keep_default_na=False
)
for device in df.itertuples():
    host = device.destination
    df.loc[device.Index, 'dns'] = get_certificate_subject_cn(host)
    pd.DataFrame(df).to_csv(r'./table/cloudfrot第二批.csv', index=False, encoding='utf-8')

 #get_certificate_subject_cn('151.101.0.167')
 df = pd.read_excel