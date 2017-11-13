# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

import zabbix


class HostView(mixins.ListModelMixin, ViewSet):
    """
    主机列表，根据组来查询
    """

    def list(self, request, *args, **kwargs):
        group = request.query_params.get('group', None)
        if group:
            return Response(zabbix.host_list(group))
        else:
            return Response(zabbix.host_list())


class GroupView(mixins.ListModelMixin, ViewSet):
    """
    主机组列表
    """

    def list(self, request, *args, **kwargs):
        return Response(zabbix.group_list())


class CpuView(mixins.ListModelMixin, ViewSet):
    """
    获取主机cpu监控数据
    """

    def list(self, request, *args, **kwargs):
        hostid = request.query_params.get('hostid', None)
        return Response(zabbix.cpu_list(hostid))


class MemoryView(mixins.ListModelMixin, ViewSet):
    """
    获取主机memory监控数据
    """

    def list(self, request, *args, **kwargs):
        hostid = request.query_params.get('hostid', None)
        return Response(zabbix.memory_list(hostid))


class DiskView(mixins.ListModelMixin, ViewSet):
    """
    获取主机disk监控数据
    """

    def list(self, request, *args, **kwargs):
        hostid = request.query_params.get('hostid', None)
        return Response(zabbix.disk_list(hostid))


class UsageView(mixins.ListModelMixin, ViewSet):
    """
    获取CPU,内存,磁盘使用占比
    """

    def list(self, request, *args, **kwargs):
        hostid = request.query_params.get('hostid', None)
        if hostid:
            return Response(zabbix.usage(hostid))
        else:
            return Response()


class EventView(mixins.ListModelMixin, ViewSet):
    """
    获取事件列表
    """

    def list(self, request, *args, **kwargs):
        return Response(zabbix.event_list())


class ServiceItemsView(mixins.ListModelMixin, ViewSet):
    """
    获取服务类型（如 Httpd/FTP）获取监控历史数据
    """

    def list(self, request, *args, **kwargs):
        service = request.query_params.get('service', None)
        history_list = zabbix.service_item_list(service)
        return Response(history_list)


class HistoryView(mixins.ListModelMixin, ViewSet):
    """
       根据 itemid 获取历史数据
    """

    def list(self, request, *args, **kwargs):
        itemid = request.query_params.get('itemid', None)
        history_list = zabbix.history_list(itemid)
        return Response(history_list)
