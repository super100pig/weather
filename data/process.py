import json
weathers = [
    'big_wind',
    'blizzard',
    'frozen_road',
    'high_temperature',
    'rain',
    'typhoon'
]
weather_id = {
    'big_wind': 'a0',
    'blizzard': 'a2',
    'frozen_road': 'a5',
    'high_temperature': 'a3',
    'rain': 'a1',
    'typhoon': 'a4'
}
node_count = 0
edge_count = 0
id_node_map = {}
old_id_node_map = {}
id_edge_map = {}
old_id_edge_map = {}

data = {}


for weather in weathers:
    node_set = set()
    new_nodes = []
    new_edges = []
    # nodes = json.load(open(weather + '_vertex.json'))
    # edges = json.load(open(weather + '_edges.json'))
    nodes = json.load(open(weather + '_vertex_rx.json'))
    edges = json.load(open(weather + '_edges_rx.json'))

    # 处理bug #############
    for edge in edges:
        if edge['src'] == 'a0':
            edge['src'] = nodes[0]['id']
    ######################
    for node in nodes:
        node['labels'] = [node['label']]
        node['showName'] = node['showname']
        node['properties'] = {}
        node['id'] = weather + node['id']
        # node['id'] = node['id']

        del node['label']
        del node['showname']
        new_nodes.append(node)
    for edge in edges:
        edge['type'] = edge['label']
        edge['showName'] = edge['label'] if edge['showname'] == 'None' else edge['showname']
        edge['properties'] = {}
        edge['linknum'] = '1'
        edge['source'] = weather + edge['src']
        edge['target'] = weather + edge['tgt']
        edge['startNode'] = weather + edge['src']
        edge['endNode'] = weather + edge['tgt']
        edge['id'] = weather + edge['id']
        # edge['source'] = edge['src']
        # edge['target'] = edge['tgt']
        # edge['startNode'] = edge['src']
        # edge['endNode'] = edge['tgt']
        # edge['id'] = edge['id']

        del edge['src']
        del edge['tgt']
        del edge['showname']
        del edge['label']
        new_edges.append(edge)
    data[weather] = {
        'nodes': new_nodes,
        'relationships': new_edges
    }

print(data)

'''
{
    ‘nodes’: [
        {
            'showname': 'rain',
            'label': '天气',
            'id': 1,
        }
    ]
}
'''
