# coding=utf-8
import time
from pyzabbix import ZabbixAPI
import json

# 登录zabbix
zabbix = ZabbixAPI('http://172.17.38.107/zabbix')
zabbix.session.verify = False
zabbix.login('Admin', 'zabbix')

hostid = '10112'

# 根据主机查询监控项
itemids = zabbix.item.get(
    hostids=[hostid],
    output=["name",
            "key_",
            "value_type",
            "hostid",
            "status",
            "state"],
    # filter={'key_': 'system.cpu.load[percpu,avg1]'}
)

print json.dumps(itemids)

item = zabbix.item.get(hostids=[hostid], output=["name", "key_", "value_type", "hostid", "status", "state"],
                       filter={'key_': 'vfs.fs.size[/,free]'})

print item

free_disk_itemid = item[0]['itemid']
t_till = int(time.time())
t_from = t_till - 2 * 24 * 60 * 60

free_disk_data = zabbix.history.get(itemids=[free_disk_itemid], history=3, output='extend', sortfield='clock',
                                    sortorder='ASC',
                                    time_from=t_from, time_till=t_till)

print json.dumps(free_disk_data)

item = zabbix.item.get(hostids=[hostid], output=["name", "key_", "value_type", "hostid", "status", "state"],
                       filter={'key_': 'vfs.fs.size[/,total]'})

print item

total_disk_itemid = item[0]['itemid']
t_till = int(time.time())
t_from = t_till - 2 * 24 * 60 * 60

total_disk_data = zabbix.history.get(itemids=[total_disk_itemid], history=3, output='extend', sortfield='clock',
                                     sortorder='ASC',
                                     time_from=t_from, time_till=t_till)

print json.dumps(total_disk_data)
