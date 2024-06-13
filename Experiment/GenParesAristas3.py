import json
data ={
  "1": {"goal": False, "deadend": False, "heuristic": 16, "Adj": [{"name": "1", "A": {"N": 1, "W": 1}}, {"name": "5", "A": {"S": 1}}, {"name": "2", "A": {"E": 1}}]},
  "2": {"goal": False, "deadend": False, "heuristic": 16, "Adj": [{"name": "2", "A": {"N": 1}}, {"name": "1", "A": {"W": 1}}, {"name": "3", "A": {"E": 1}},{"name": "6", "A": {"S": 1}}]},
  "3": {"goal": False, "deadend": False, "heuristic": 16, "Adj": [{"name": "3", "A": {"N": 1}}, {"name": "2", "A": {"W": 1}}, {"name": "4", "A": {"E": 1}},{"name": "7", "A": {"S": 1}}]},
  "4": {"goal": False, "deadend": True, "heuristic": 16, "Adj": [{"name": "4", "A": {"N": 1, "E":1}}, {"name": "3", "A": {"W": 1}}, {"name": "8", "A": {"S": 1}}]},
  "5": {"goal": False, "deadend": False, "heuristic": 16, "Adj": [{"name": "1", "A": {"N": 1}},{"name": "5", "A": {"W": 1}}, {"name": "9", "A": {"S": 1}}, {"name": "6", "A": {"E": 1}}]},
  "6": {"goal": False, "deadend": False, "heuristic": 16, "Adj": [{"name": "2", "A": {"N": 1}},{"name": "5", "A": {"W": 1}}, {"name": "10", "A": {"S": 1}}, {"name": "7", "A": {"E": 1}}]},
  "7": {"goal": False, "deadend": False, "heuristic": 16, "Adj": [{"name": "3", "A": {"N": 1}},{"name": "6", "A": {"W": 1}}, {"name": "11", "A": {"S": 1}}, {"name": "8", "A": {"E": 1}}]},
  "8": {"goal": False, "deadend": False, "heuristic": 16, "Adj": [{"name": "4", "A": {"N": 1}},{"name": "7", "A": {"W": 1}}, {"name": "12", "A": {"S": 1}}, {"name": "8", "A": {"E": 1}}]},
  "9": {"goal": False, "deadend": False, "heuristic": 16, "Adj": [{"name": "5", "A": {"N": 1}},{"name": "9", "A": {"W": 1}}, {"name": "13", "A": {"S": 1}}, {"name": "10", "A": {"E": 1}}]},
  "10": {"goal": False, "deadend": False, "heuristic": 16, "Adj": [{"name": "6", "A": {"N": 1}},{"name": "9", "A": {"W": 1}}, {"name": "14", "A": {"S": 1}}, {"name": "11", "A": {"E": 1}}]},
  "11": {"goal": False, "deadend": False, "heuristic": 16, "Adj": [{"name": "7", "A": {"N": 1}},{"name": "10", "A": {"W": 1}}, {"name": "15", "A": {"S": 1}}, {"name": "12", "A": {"E": 1}}]},
  "12": {"goal": False, "deadend": False, "heuristic": 16, "Adj": [{"name": "8", "A": {"N": 1}},{"name": "11", "A": {"W": 1}}, {"name": "16", "A": {"S": 1}}, {"name": "12", "A": {"E": 1}}]},
  "13": {"goal": False, "deadend": False, "heuristic": 16, "Adj": [{"name": "9", "A": {"N": 1}},{"name": "13", "A": {"W": 1,"S":1}}, {"name": "14", "A": {"E": 1}}]},
  "14": {"goal": False, "deadend": False, "heuristic": 16, "Adj": [{"name": "10", "A": {"N": 1}},{"name": "13", "A": {"W": 1}}, {"name": "14", "A": {"S": 1}}, {"name": "15", "A": {"E": 1}}]},
  "15": {"goal": False, "deadend": False, "heuristic": 16, "Adj": [{"name": "11", "A": {"N": 1}},{"name": "14", "A": {"W": 1}}, {"name": "15", "A": {"S": 1}}, {"name": "16", "A": {"E": 1}}]},
  "16": {"goal": True, "deadend": False, "heuristic": 16, "Adj": [{"name": "12", "A": {"N": 0}},{"name": "15", "A": {"W": 0}}, {"name": "16", "A": {"S": 1, "E":1}}]}
}

# Function to extract all pairs of edges
def extract_edges(data):
    edges = []
    for node, details in data.items():
        for adj in details['Adj']:
            edges.append((node, adj['name']))
    return edges

# Extract and print all pairs of edges
edges = extract_edges(data)
for edge in edges:
    print(edge)