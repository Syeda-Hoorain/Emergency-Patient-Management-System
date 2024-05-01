import matplotlib.pyplot as plt
import networkx as nx

def draw_max_heap(max_heap):
    G = nx.Graph()

    for i, value in enumerate(max_heap):
        if value is not None:
            severity, ward, patient_id = value
            G.add_node(i, label=f"Severity: {severity}\nWard: {ward}\nPatient ID: {patient_id}")
        else:
            G.add_node(i, label="No Patient")

    for i in range(len(max_heap)):
        if i == 0:
            continue  # Root has no parent
        parent = (i - 1) // 2
        G.add_edge(parent, i)

    pos = {}
    for i in range(len(max_heap)):
        depth = i.bit_length() - 1
        pos[i] = ((i - 2 ** depth + 1) * (2 ** (len(max_heap) - depth - 1)), -depth)

    labels = nx.get_node_attributes(G, 'label')
    plt.figure(num = 'Patient Database Visualizer',figsize=(13, 7))  # Set the figure size (width, height) in inches
    nx.draw(G, pos, with_labels=True, labels=labels, node_size=5000, node_color='lightblue', font_size=10, font_weight='bold', arrows=False)
    plt.xlim(-1, 2 ** len(max_heap))  # Adjust plot limits to include all nodes
    plt.ylim(-max(pos.values(), key=lambda x: x[1])[1] - 1, 1)  # Set y limit to the depth of the heap
    plt.gca().invert_yaxis()  # Invert y-axis to display tree from top to bottom
    plt.axis('off')  # Turn off axis
    plt.show()

# Example usage:
# max_heap = [
#     (10, "Ward A", "Patient 1"),
#     (10, "Ward A", "Patient 4"),
#     (10, "Ward C", "Patient 6"),
#     (6, "Ward C", "Patient 3"),
#     (3, "Ward B", "Patient 2"),
#     (2, "Ward B", "Patient 5"),
#     None, None, None
# ]
# draw_max_heap(max_heap)
