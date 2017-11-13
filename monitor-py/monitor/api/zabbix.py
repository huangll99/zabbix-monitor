# coding=utf-8
import time
from pyzabbix import ZabbixAPI

# 登录zabbix
zabbix = ZabbixAPI('http://172.17.38.107/zabbix')
zabbix.session.verify = False
zabbix.login('Admin', 'zabbix')


def group_list():
    return zabbix.hostgroup.get(
        output=['groupid', 'name']
    )


def host_list(group=None):
    if group:
        return zabbix.host.get(
            output=['host', 'hostid', 'name', 'available'],
            groupids=[group],
            selectGroups=['name']
        )
    else:
        return zabbix.host.get(
            output=['host', 'hostid', 'name', 'available'],
            selectGroups=['name']
        )


def cpu_list(hostid):
    if hostid:
        item = zabbix.item.get(hostids=[hostid], output=["name", "key_", "value_type", "hostid", "status", "state"],
                               filter={'key_': 'system.cpu.load[percpu,avg1]'})

        itemid = item[0]['itemid']
        t_till = int(time.time())
        t_from = t_till - 2 * 24 * 60 * 60

        return zabbix.history.get(
            # hostids=[hostid],
            itemids=[itemid],
            history=0,
            output='extend',
            sortfield='clock',
            sortorder='ASC',
            time_from=t_from,
            time_till=t_till
        )


def memory_list(hostid):
    if hostid:
        item = zabbix.item.get(hostids=[hostid], output=["name", "key_", "value_type", "hostid", "status", "state"],
                               filter={'key_': 'vm.memory.size[available]'})

        itemid = item[0]['itemid']
        t_till = int(time.time())
        t_from = t_till - 2 * 24 * 60 * 60

        return zabbix.history.get(
            # hostids=[hostid],
            itemids=[itemid],
            history=3,
            output='extend',
            sortfield='clock',
            sortorder='ASC',
            time_from=t_from,
            time_till=t_till
        )


def disk_list(hostid):
    if hostid:
        item = zabbix.item.get(hostids=[hostid], output=["name", "key_", "value_type", "hostid", "status", "state"],
                               filter={'key_': 'vfs.fs.size[/,free]'})

        itemid = item[0]['itemid']
        t_till = int(time.time())
        t_from = t_till - 2 * 24 * 60 * 60

        return zabbix.history.get(
            # hostids=[hostid],
            itemids=[itemid],
            history=3,
            output='extend',
            sortfield='clock',
            sortorder='ASC',
            time_from=t_from,
            time_till=t_till
        )


def event_list():
    t_till = int(time.time())
    t_from = t_till - 7 * 24 * 60 * 60

    triggers = zabbix.trigger.get(
        output=['triggerid', 'description', 'priority']
    )
    triggerDict = {}
    for trigger in triggers:
        triggerDict[trigger['triggerid']] = trigger

    events = zabbix.event.get(
        output='extend',
        selectHosts=['name', 'host'],
        sortfield='clock',
        sortorder='DESC',
        time_from=t_from,
        time_till=t_till
    )
    return [{
        'clock': event['clock'],
        'eventid': event['eventid'],
        'acknowledged': event['acknowledged'],
        'hosts': event['hosts'],
        'trigger': triggerDict.get(event['objectid'])
    } for event in events]


def usage(hostid):
    diskItemids = zabbix.item.get(
        hostids=[hostid],
        output=["name",
                "key_",
                "value_type",
                "hostid",
                "status",
                "state"],
        filter={'key_': 'vfs.fs.size[/,pfree]'}
    )
    diskUsage = zabbix.history.get(itemids=[diskItemids[0]['itemid']], history=0, output='extend', sortfield='clock',
                                   sortorder='ASC', limit=1)
    return [{
        'diskUsage': diskUsage,
    }]


def service_history_list(service):
    if service:
        t_till = int(time.time())
        t_from = t_till - 7 * 24 * 60 * 60
        # 所有监控项
        items = zabbix.item.get(
            output=['itemid'],
            filter={'name': service},
            selectHosts=['name', 'host'],
        )
        history = []
        for item in items:
            history.append(
                zabbix.history.get(
                    itemids=[item['itemid']],
                    history=3,
                    output='extend',
                    sortfield='clock',
                    sortorder='ASC',
                    time_from=t_from,
                    time_till=t_till,
                )
            )
        return {
            'items': items,
            'history': history
        }


def service_item_list(service):
    if service:
        # 所有监控项
        items = zabbix.item.get(
            output=['itemid'],
            filter={'name': service},
            selectHosts=['name', 'host'],
        )
        return items


def history_list(itemid):
    if itemid:
        t_till = int(time.time())
        t_from = t_till - 7 * 24 * 60 * 60
        return zabbix.history.get(
            itemids=[itemid],
            history=3,
            output='extend',
            sortfield='clock',
            sortorder='ASC',
            time_from=t_from,
            time_till=t_till,
        )
