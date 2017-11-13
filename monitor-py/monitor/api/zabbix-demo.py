# coding=utf-8
import time
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

itemid = res[0]['itemid']

print itemid

t_till = int(time.time())
t_from = t_till - 2 * 24 * 60 * 60
print t_from
print t_till

# 查询cpu历史数据
history = zabbix.history.get(
    # hostids=[hostid],
    itemids=[itemid],
    history=0,
    output='extend',
    sortfield='clock',
    sortorder='ASC',
    time_from=t_from,
    time_till=t_till
)

json_dump = json.dumps(history)
print json_dump

values = ''
for item in history:
    values = values + item['value'] + ','

times = ''
for item in history:
    times = times + item['clock'] + ','
    # times.append(item['clock'])

hosts = zabbix.host.get(output='extend')

triggers = zabbix.trigger.get(
    output=['triggerid', 'description', 'priority']
)

print json.dumps(triggers)

triggerDict = {}
for trigger in triggers:
    triggerDict[trigger['triggerid']] = trigger

events = zabbix.event.get(
    output='extend',
    selectHosts=['hostid', 'host'],
    sortfield='clock',
    sortorder='DESC',
    time_from=t_from,
    time_till=t_till
)

res = [{
    'clock': event['clock'],
    'eventid': event['eventid'],
    'acknowledged': event['acknowledged'],
    'hosts': event['hosts'],
    'trigger': triggerDict.get(event['objectid'])
} for event in events]

itemids = zabbix.item.get(
    hostids=[hostid],
    output=["name",
            "key_",
            "value_type",
            "hostid",
            "status",
            "state"],
    filter={'key_': 'vfs.fs.size[/,pfree]'}
)

print itemids[0]['itemid']

history = zabbix.history.get(
    # hostids=[hostid],
    itemids=[itemids[0]['itemid']],
    history=0,
    output='extend',
    sortfield='clock',
    sortorder='ASC',
    limit=1
)

print json.dumps(history)

# 所有监控项
items = zabbix.item.get(
    output=['itemid', 'description'],
    filter={'name': 'httpd'},
    selectHosts=['name', 'host'],
)
print json.dumps(items)

for item in items:
    history = zabbix.history.get(
        itemids=[item['itemid']],
        history=3,
        output='extend',
        sortfield='clock',
        sortorder='ASC',
        time_from=t_from,
        time_till=t_till,

    )
    print json.dumps(history)
