from collections import defaultdict

from jio.JsonFileIO import get_json

'''
# Root
# - children: List[Node]

# Node
# - parent: Union[Root | Node]
# - children: List[Node]
# - types: NodeType
'''


def analyze_json_types(data, type_stats):
    if isinstance(data, dict):
        type_stats['dict'] += 1
        for key, value in data.items():
            analyze_json_types(value, type_stats)
    elif isinstance(data, list):
        type_stats['list'] += 1
        for item in data:
            analyze_json_types(item, type_stats)
    elif isinstance(data, int):
        type_stats['int'] += 1
    elif isinstance(data, float):
        type_stats['float'] += 1
    elif isinstance(data, str):
        type_stats['str'] += 1
    else:
        type_stats['other'] += 1


def capture_json_stats(json_data):
    # Initialize a dictionary to hold the count of each type
    type_stats = defaultdict(int)

    # Analyze the JSON data
    analyze_json_types(json_data, type_stats)

    return type_stats


# def check_json_types(data):
#     if isinstance(data, dict):
#         for key, value in data.items():
#             print(f"Key: {key}, Type: {type(value).__name__}")
#             check_json_types(value)
#     elif isinstance(data, list):
#         for index, item in enumerate(data):
#             print(f"Index: {index}, Type: {type(item).__name__}")
#             check_json_types(item)
#     else:
#         print(f"Value: {data}, Type: {type(data).__name__}")


file_path = 'resources/raw_items.json'
raw_json_data = get_json(file_path)
# check_json_types(raw_json_data)
stats = capture_json_stats(raw_json_data)

# Print the stats
print("JSON Data Type Statistics:")
for data_type, count in stats.items():
    print(f"{data_type}: {count}")
