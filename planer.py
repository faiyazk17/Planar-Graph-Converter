import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class PlanarGraphGUI:
    def __init__(self, master):
        self.master = master
        master.title("Planar Graph Creator")

        self.G = nx.Graph()

        self.label = ttk.Label(
            master, text="Enter vertices and their adjacencies: \ne.g.\n      a = b,c\n      b = d,e\n      etc.")
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.text_area = tk.Text(master, width=30, height=10)
        self.text_area.grid(row=1, column=0, padx=10)

        self.add_button = ttk.Button(
            master, text="Add Vertices", command=self.add_vertices)
        self.add_button.grid(row=1, column=1, padx=10)

        self.canvas_frame = ttk.Frame(master)
        self.canvas_frame.grid(row=2, column=0, columnspan=2, pady=10)
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.canvas_frame)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.draw_button = ttk.Button(
            master, text="Draw Graph", command=self.draw_graph)
        self.draw_button.grid(row=3, column=0, columnspan=2, pady=10)

    def add_vertices(self):
        vertices_input = self.text_area.get("1.0", tk.END).strip()

        if not vertices_input:
            return

        vertices_dict = {}
        for line in vertices_input.splitlines():
            vertex, *adjacencies = line.split('=')
            vertex = vertex.strip()
            adjacencies = [adj.strip()
                           for adj in "".join(adjacencies).split(',')]
            vertices_dict[vertex] = adjacencies

        for vertex, adjacencies in vertices_dict.items():
            self.G.add_node(vertex)
            self.G.add_edges_from((vertex, adj) for adj in adjacencies)

        self.text_area.delete("1.0", tk.END)

    def draw_graph(self):
        try:
            pos = nx.planar_layout(self.G)

            self.ax.clear()

            nx.draw(self.G, pos, with_labels=True, font_weight='bold',
                    node_color='skyblue', font_color='black', ax=self.ax)

            self.canvas.draw()

        except nx.NetworkXException as e:
            messagebox.showerror(
                "Error", f"The input graph is not planar.\nError: {e}")


if __name__ == "__main__":
    root = tk.Tk()
    app = PlanarGraphGUI(root)
    root.mainloop()
