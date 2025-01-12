from heapq import heappush, heappop
import matplotlib.pyplot as plt
import numpy as np
from typing import List, Tuple, Optional


class Node:
    def __init__(self, position: Tuple[int, int], parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start to current node
        self.h = 0  # Estimated cost from current node to goal
        self.f = 0  # Total cost (g + h)

    def __lt__(self, other):
        return self.f < other.f


class MuseumEvacuation:
    def __init__(self):
        self.layout = [
            ['0', '0', '1', '0', 'E'],
            ['0', '1', '0', '1', '0'],
            ['P', '0', '0', '0', '0'],
            ['0', '1', '1', '1', '0'],
            ['0', '0', '0', '0', 'E']
        ]
        self.rows = len(self.layout)
        self.cols = len(self.layout[0])

    def find_person_and_exits(self) -> Tuple[Tuple[int, int], List[Tuple[int, int]]]:
        """Find person's position and all emergency exits"""
        # TODO: Implement this method
        person_position = None
        exits = []

        for i in range(self.rows):
            for j in range(self.cols):
                if self.layout[i][j] == 'P':
                    person_position = (i, j)
                elif self.layout[i][j] == 'E':
                    exits.append((i, j))

        return person_position, exits
        pass

    def manhattan_distance(self, pos1: Tuple[int, int], pos2: Tuple[int, int]) -> int:
        """Calculate Manhattan distance between two points"""
        # TODO: Implement this method
        return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])
        pass

    def get_neighbors(self, position: Tuple[int, int]) -> List[Tuple[int, int]]:
        """Get valid neighboring positions"""
        # TODO: Implement this method
        row, col = position
        neighbors = []

        #check direzioni
        if row > 0 and self.layout[row - 1][col] != '1':  #su
            neighbors.append((row - 1, col))
        if row < self.rows - 1 and self.layout[row + 1][col] != '1':  #giu
            neighbors.append((row + 1, col))
        if col > 0 and self.layout[row][col - 1] != '1':  #sx
            neighbors.append((row, col - 1))
        if col < self.cols - 1 and self.layout[row][col + 1] != '1':  #dx
            neighbors.append((row, col + 1))

        return neighbors
        pass

    def find_evacuation_path(self) -> Optional[List[Tuple[int, int]]]:
        """Find shortest path to nearest emergency exit"""
        # TODO: Implement this method
        person_position, exits = self.find_person_and_exits()
        if not person_position or not exits:
            return None  # Nessuna persona o uscita trovata

        #creo lista open
        open_list = [person_position]
        parent_map = {person_position: None}  #parent nodes
        while open_list:
            current_position = open_list.pop(0)
            #ricostruisco il path se sono arrivato a un nodo finale
            if current_position in exits:
                path = []
                while current_position:
                    path.append(current_position)
                    current_position = parent_map[current_position]
                return path[::-1]  #return del percorso all'inverso

            #esplorazione dei vicini
            for neighbor in self.get_neighbors(current_position):
                if neighbor not in parent_map:  # Se non è stato visitato
                    open_list.append(neighbor)
                    parent_map[neighbor] = current_position

        return None  #se non trovo nessun path
        pass

    def display_path(self, path: List[Tuple[int, int]]):
        """Display the evacuation path on the museum layout"""
        # TODO: Implement this method
        self.visualize(path)
        pass
    
    def visualize(self, path: List[Tuple[int, int]] = None):
        """
        Visualize the museum layout with matplotlib.
        If path is provided, it will be shown in green.
        """
        # Create figure with smaller size and better cell proportion
        fig, ax = plt.subplots(figsize=(6, 6))
        
        # Create color map with distinct colors
        cmap = plt.cm.colors.ListedColormap(['#FFFFFF', '#404040', '#FF4444', '#4444FF', '#FFCC00'])
        
        # Convert layout to numeric array for visualization
        numeric_layout = np.zeros((self.rows, self.cols))
        text_annotations = []  # Store text annotations for cells
        
        for i in range(self.rows):
            for j in range(self.cols):
                if self.layout[i][j] == '1':  # Wall
                    numeric_layout[i][j] = 1
                    text_annotations.append((i, j, ''))
                elif self.layout[i][j] == 'E':  # Exit
                    numeric_layout[i][j] = 2
                    text_annotations.append((i, j, 'EXIT'))
                elif self.layout[i][j] == 'P':  # Person
                    numeric_layout[i][j] = 3
                    text_annotations.append((i, j, 'P'))
                else:  # Free space
                    text_annotations.append((i, j, ''))
        
        # Add path if provided
        if path:
            for row, col in path[1:-1]:  # Skip start and end positions
                numeric_layout[row][col] = 4
                text_annotations.append((row, col, '→'))

        # Plot the layout
        im = ax.imshow(numeric_layout, cmap=cmap)
        
        # Add cell borders
        for i in range(self.rows + 1):
            ax.axhline(i - 0.5, color='black', linewidth=1)
        for j in range(self.cols + 1):
            ax.axvline(j - 0.5, color='black', linewidth=1)
        
        # Add text annotations
        for i, j, text in text_annotations:
            if text:  # Only add non-empty text
                color = 'white' if numeric_layout[i,j] in [1, 2, 3] else 'black'
                ax.text(j, i, text, ha='center', va='center', color=color, 
                       fontweight='bold', fontsize=10)
        
        # Remove ticks but keep grid lines
        ax.set_xticks([])
        ax.set_yticks([])
        
        # Add legend with smaller patches
        from matplotlib.patches import Patch
        legend_elements = [
            Patch(facecolor='#FFFFFF', edgecolor='black', label='Free Space'),
            Patch(facecolor='#404040', edgecolor='black', label='Wall'),
            Patch(facecolor='#FF4444', edgecolor='black', label='Exit'),
            Patch(facecolor='#4444FF', edgecolor='black', label='Person'),
        ]
        if path:
            legend_elements.append(Patch(facecolor='#FFCC00', edgecolor='black', label='Path'))
            
        ax.legend(handles=legend_elements, 
                 loc='center left',
                 bbox_to_anchor=(1.05, 0.5),
                 title='Legend',
                 frameon=True,
                 fontsize='small')
        
        plt.title('Museum Layout', pad=10)
        plt.tight_layout()
        plt.show()