import re
import os
import sys
from importlib import util
from inspect import getsource


def listing_method(PATH_MODULES):
    """
    служебная функция для поиска методов в  директории
    """
    about_module={}
    module_regex=re.compile("(.+)\.py")
    for i in os.listdir(PATH_MODULES):
        if module_regex.match(i):
            spec=util.spec_from_file_location(module_regex.findall(i)[0], "/".join([PATH_MODULES,i]))
            about_module[module_regex.findall(i)[0]]={}
            module = util.module_from_spec(spec)
            sys.modules[module_regex.findall(i)[0]] = module
            spec.loader.exec_module(module)
            for f in dir(module):
                if not re.match("^__",f):
                    func_describe=getattr(module,f)
                    func_source_code=getsource(func_describe)
                    func_doc=func_describe.__doc__
                    about_module[module_regex.findall(i)[0]].update({f:{"func_doc":func_doc,"func_source_code":func_source_code}})
    return about_module

def sorted_json_by_version(json_data):
    """
    служебная функция для сортировки json по версиям
    """
    list_version=[]
    sorted_map={}
    for i,v in json_data.items():
        for key,value in v.items():
            list_version.append(value['ident'])
    list_version.sort(key=lambda s: list(map(int, s.split('.'))),reverse=True)
    for i in list_version:
        for ib,v in json_data.items():
            for key,value in v.items():
                if value['ident']==i:
                    value['value']=value['value'].split()
                    sorted_map[key]=value
    return sorted_map
