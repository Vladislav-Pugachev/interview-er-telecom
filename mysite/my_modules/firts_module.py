def sorted_version(data):
    """
    функция для сортировки версии
    """
    list_version=[]
    sorted_map={}
    for i,v in data.items():
        print(i,v)
        list_version.append(v['ident'])
    list_version.sort(key=lambda s: list(map(int, s.split('.'))),reverse=True)
    for i in list_version:
        for k,v in data.items():
            if v['ident']==i:
                v['value']=v['value'].split()
                sorted_map[k]=v
    return sorted_map


def second_func():
    """
    вторая функция из первого модуля
    """
    return "вторая функция из первого модуля"