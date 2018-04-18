from django.http import HttpResponse
import json
#from playbook import play
import yaml
import zabbix


def deploy_agent(request):
    agent = json.loads(request.body)
    hostname = agent['hostname']
    group = agent['group']
    host = agent['host']
    ip = agent['ip']
    template = agent['template']
    password = agent['password']

    fw = open('./host.yaml', 'w')
    new_data = [{'tasks': [{'shell': 'rm -rf /etc/yum.repos.d/*', 'name': 'clean repo'},
                           {'copy': 'src=./src/CentOS-Media.repo dest=/etc/yum.repos.d/',
                            'name': 'configure mirrors'},
                           {'shell': 'yum clean all&yum makecache', 'name': 'update repo'},
                           {'yum': 'pkg=zabbix-agent state=latest', 'name': 'install zabbix.agent'},
                           {'name': 'stop firewalld', 'service': 'name=firewalld state=stopped'},
                           {'copy': 'src=./src/zabbix_agentd.conf dest=/etc/zabbix/',
                            'name': 'copy zabbix-agent'},
                           {'hostname': 'name=' + hostname},
                           {'command': "sed -i 's/vm1/" + hostname + "/g' /etc/zabbix/zabbix_agentd.conf",
                            'name': 'configuration zabbix-agent'},
                           {'name': 'start zabbix-agent', 'service': 'name=zabbix-agent state=started'}],
                 'hosts': 'all',
                 'remote_user': 'root'}]

    yaml.dump(new_data, fw)
    fw.close()
    #play(ip, password, './host.yaml')
    zabbix.create_host(group, hostname, ip, template)
    return HttpResponse('ok')
