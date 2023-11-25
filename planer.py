import networkx as nx
import matplotlib.pyplot as plt


def create_planar_graph():
    # Creating an empty graph
    G = nx.Graph()

    # Getting user input for each vertex and it's adjacencies
    while True:
        vertex_input = input(
            "Enter vertex and its adjacencies (e.g., a = f,d,b): ").strip()

        # Break the loop if the user enters an empty line
        if not vertex_input:
            break

        # Split the input into vertex and adjacencies
        vertex, *adjacencies = vertex_input.split('=')
        vertex = vertex.strip()
        adjacencies = [adj.strip() for adj in "".join(adjacencies).split(',')]

        # Add the vertex and its adjacencies to the graph
        G.add_node(vertex)
        G.add_edges_from((vertex, adj) for adj in adjacencies)

    try:
        # Try to create a planar embedding
        pos = nx.planar_layout(G)

        # Draw the graph
        nx.draw(G, pos, with_labels=True, font_weight='bold',
                node_color='skyblue', font_color='black')

        # Show the graph
        plt.show()

    except nx.NetworkXException as e:
        print(f"Error: {e}")
        print("The input graph is not planar.")


if __name__ == "__main__":
    # Create a planar graph
    create_planar_graph()
