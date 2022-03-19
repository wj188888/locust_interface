# -*- coding:utf-8 -*-
import yaml
from ruamel.yaml import YAML
from ruamel import yaml

def read_yaml(yaml_path):
    with open(yaml_path, 'r', encoding='utf-8') as fp:
        yaml_func = YAML(typ='safe', pure=False)
        yaml_data = yaml_func.load(fp)
    if yaml_data is None:
        raise "当前yml文件为空，请不要引用该文件"
    if yaml_data:
        return yaml_data
    else:
        raise ValueError

def get_config():
    config = read_yaml(r'../data/Token.yml')
    config = config['config']
    return config

def get_headers():
    headers = {
        "Content-Type": "application/json",
        "Authorization": get_config['token'],
        "PROJECT-HEADER": str(get_config['project_id'])  # 把获取到的当前项目id给到headers
    }
    return dict(headers)