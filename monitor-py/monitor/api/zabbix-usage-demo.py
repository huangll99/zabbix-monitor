# coding=utf-8
from pyzabbix import ZabbixAPI
import json

# 登录zabbix
zabbix = ZabbixAPI('http://172.17.38.107/zabbix')
zabbix.session.verify = False
zabbix.login('Admin', 'zabbix')

hostid = '10110'

# 根据主机查询监控项
res = zabbix.item.get(
    hostids=[hostid],
    output=["name",
            "key_",
            "value_type",
            "hostid",
            "status",
            "state"],
    # filter={'key_': 'system.cpu.load[percpu,avg1]'}
)

dump = json.dumps(res)
print dump
