import json

import requests


class ZabbixAPI():
    
    #request请求到zabbix server获取数据
    def getRequest(self,postdata):
        postdata = json.dumps(postdata)
        try:
            request = requests.post(url=self.url, data=postdata, headers=self.headers)
            print(request.content)
            content = request.json()
            # content  = json.loads(reponse.decode('utf8'))
            return content
        except Exception as ErrorMsg:
            print(str(ErrorMsg))

    def get_token(self):
        res = self.getRequest(self.authdata)

        print(res)
        # if 'result' in res:
        #     token = res['result']
        #     return token
        # else:
        #     return res['error']['data']




if __name__=="__main__":
    # zbx = ZabbixAPI()
    # zbx.get_token()            
    
    url = "http://172.16.66.80/api_jsonrpc.php"
    headers = {
        'Content-Type':'application/json'
        }
    data = {
        "jsonrpc":"2.0",
        "method":"user.login",
        "params": {
            "user":"Admin",
            "password":"zabbix"
        },
        "id":0
    }
    print(json.dumps(data))
    #request = requests.get(url=url, data=json.dumps(data), headers=headers)
    request = requests.post(url=url, data=json.dumps(data), headers=headers)

    print(json.loads(request.content).get("result"))
    print(request.content)