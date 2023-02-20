from pyzabbix import ZabbixAPI

zabbix_server = "http://172.16.66.80/api_jsonrpc.php?"  
zabbix_username = "Admin"
zabbix_password = "zabbix"
zapi = ZabbixAPI(url=zabbix_server, user=zabbix_username, password=zabbix_password)
token = zapi.user.login(user=zabbix_username, password=zabbix_password)

print(token)
