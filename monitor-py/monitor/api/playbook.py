# -*- coding: utf-8 -*-
# encoding=utf-8
import fileinput
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from ansible.inventory import Inventory
from ansible.executor.playbook_executor import PlaybookExecutor


def play(vm_ip, vm_password, yaml_pathfile):
    # load yaml file
    loader = DataLoader()
    # class studio
    variable_manager = VariableManager()
    inventory = Inventory(loader=loader, variable_manager=variable_manager, host_list=[vm_ip])
    variable_manager.set_inventory(inventory)
    passwords = dict(conn_pass=vm_password)
    Options = namedtuple('Options',
                         ['connection',
                          'remote_user',
                          'ask_sudo_pass',
                          'verbosity',
                          'ack_pass',
                          'module_path',
                          'forks',
                          'become',
                          'become_method',
                          'become_user',
                          'check',
                          'listhosts',
                          'listtasks',
                          'listtags',
                          'syntax',
                          'sudo_user',
                          'sudo'])
    options = Options(connection='smart',
                      remote_user='root',
                      ack_pass=None,
                      sudo_user='root',
                      forks=5,
                      sudo='yes',
                      ask_sudo_pass=False,
                      verbosity=5,
                      module_path=None,
                      become=True,
                      become_method='sudo',
                      become_user='root',
                      check=None,
                      listhosts=None,
                      listtasks=None,
                      listtags=None,
                      syntax=None)

    playbook = PlaybookExecutor(playbooks=[yaml_pathfile], inventory=inventory,
                                variable_manager=variable_manager,
                                loader=loader, options=options, passwords=passwords)
    playbook.run()
