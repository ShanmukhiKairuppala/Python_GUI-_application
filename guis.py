
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt

class GraphGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Data Visualization")
        
        # Create button to select data file
        self.file_button = tk.Button(self.master, text="Select Data File", command=self.load_data)
        self.file_button.pack()
        
        # Create buttons to generate different types of graphs
        self.pie_button = tk.Button(self.master, text="Generate Pie Chart", command=self.generate_pie_chart, state=tk.DISABLED)
        self.pie_button.pack()
        self.hist_button = tk.Button(self.master, text="Generate Histogram", command=self.generate_histogram, state=tk.DISABLED)
        self.hist_button.pack()
        self.bar_button = tk.Button(self.master, text="Generate Bar Graph", command=self.generate_bar_graph, state=tk.DISABLED)
        self.bar_button.pack()
        self.line_button = tk.Button(self.master, text="Generate Line Graph", command=self.generate_line_graph, state=tk.DISABLED)
        self.line_button.pack()
        self.scatter_button = tk.Button(self.master, text="Generate Scatter Plot", command=self.generate_scatter_plot, state=tk.DISABLED)
        self.scatter_button.pack()
        
    def load_data(self):
        # Open file dialog to select data file
        file_path = filedialog.askopenfilename()
        
        # Load data from selected file into pandas dataframe
        self.data = pd.read_csv(file_path)
        
        # Enable graph buttons
        self.pie_button.config(state=tk.NORMAL)
        self.hist_button.config(state=tk.NORMAL)
        self.bar_button.config(state=tk.NORMAL)
        self.line_button.config(state=tk.NORMAL)
        self.scatter_button.config(state=tk.NORMAL)
        
    def generate_pie_chart(self):
        # Group data by categories and sum values
        grouped_data = self.data.groupby('Category').sum()
        
        # Create pie chart using matplotlib
        plt.pie(grouped_data['Value'], labels=grouped_data.index, autopct='%1.1f%%')
        plt.axis('equal')
        plt.title('Pie Chart')
        plt.show()
        
    def generate_histogram(self):
        # Create histogram using matplotlib
        plt.hist(self.data['Value'], bins=10)
        plt.title('Histogram')
        plt.show()
        
    def generate_bar_graph(self):
        # Group data by categories and sum values
        grouped_data = self.data.groupby('Category').sum()
        
        # Create bar graph using matplotlib
        plt.bar(grouped_data.index, grouped_data['Value'])
        plt.title('Bar Graph')
        plt.show()
        
    def generate_line_graph(self):
        # Group data by categories and sum values
        grouped_data = self.data.groupby('Category').sum()
        
        # Create line graph using matplotlib
        plt.plot(grouped_data.index, grouped_data['Value'])
        plt.title('Line Graph')
        plt.show()
        
    def generate_scatter_plot(self):
        # Create scatter plot using matplotlib
        plt.scatter(self.data['Category'], self.data['Value'])
        plt.title('Scatter Plot')
        plt.show()

# Create tkinter root window and run application
root = tk.Tk()
app = GraphGUI(root)
root.mainloop()
