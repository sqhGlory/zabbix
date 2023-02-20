import os
import time

import pandas as pd
from tqdm import *

table_list = ["./table/CFDC-G_QA-any-any-monitor.xlsx"]


def get_shell_return(ip: str):
    f = os.popen(f"nslookup {ip}")
    res = f.read()

    if "name" in res:
        print(f"{ip}:解析成功")
        return "".join(res.split("=")[1].split("\n")[0].split())
    else:
        print(f"{ip}:站点不支持反向解析不出来")
        return "站点不支持反向解析不出来"
        no_list

def change_source_data(table: str):
   
    df = pd.read_excel(table)
    dic = df.to_dict("records")
    for i in dic:
        dns = get_shell_return(i["destination.ip: Descending"])
        i['dns'] = dns
    pd.DataFrame(dic).to_excel(table)


def get_dic(table: list):
    result = []
    for i in range(len(table)):
        df = pd.read_excel(table[i])
        # df.drop("SourceZone: Descending", 1, inplace=True)
        df.drop("Count", 1, inplace=True)
        # df.drop("remark", 1, inplace=True)
        # df.drop("建议", 1, inplace=True)
        # df.drop("客户确认", 1, inplace=True)
        result.append(df)
    df = pd.concat(result)
    return df.drop_duplicates(keep=False).to_dict("records")


if __name__ == '__main__':
    # print(get_shell_return("59.111.19.11"))
    change_source_data("./table/CFDC-G_QA-any-any-monitor.xlsx")
    #db_dic = pd.read_excel("./result/source.xlsx").to_dict("records")
    #dic = get_dic(table_list)
    

    #for i in tqdm(dic):
    #    dns = get_shell_return(i["destination.ip: Descending"])
    #    for j in db_dic:
    #        if i["destination.ip: Descending"] == j["destination.ip: Descending"] and i[
    #            "DestinationPort: Descending"] == j["DestinationPort: Descending"]:
    #            j['dns'] = dns
    #            break
    #    else:
    #        print("未出现过")
    #        i['dns'] = dns
    #        db_dic.append(i)
    #pd.DataFrame(db_dic).to_excel("./result/source.xlsx")