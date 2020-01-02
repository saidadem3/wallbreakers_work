from linked_list import LinkedList
from queue import Queue


class Graph:
    def __init__(self, vertices):
        # Total number of vertices
        self.vertices = vertices
        # Defining a list which can hold multiple LinkedLists equal to the number of vertices in the graph
        self.array = []
        # adjacency matrix
        self.matrix = [[0]]*self.vertices
        # Creating a new LinkedList for each vertex/index of the list
        for vertex in range(vertices):
            temp = LinkedList()
            self.array.append(temp)

    def add_edge(self, source, destination):
        # As we are implementing a directed graph, (1,0) is not equal to (0,1)
        self.array[source].insert_at_head(destination)
        # If we were to implement an Undirected Graph i.e (1,0) == (0,1)
        # We would create an edge from destination towards source as well
        # i.e self.list[destination].insert_at_head(source)

    def print_graph(self):
        print(">>Adjacency List of Directed Graph<<")
        for i in range(self.vertices):
            print("|", i, end=" | => ")
            temp = self.array[i].head
            while(temp != None):
                print("[", temp.data, end=" ] -> ")
                temp = temp.next
            print("None")

    def bfs_traversal(self, source):
        result = []
        num_vertices = self.vertices
        visited = []
        for _ in range(num_vertices):
          visited.append(False)

        q = []
        q.append(source)
        visited[source] = True

        while q:
          current_node = q.pop(0)
          result.append(str(current_node))
          temp = self.array[current_node].head

          # linked list traversal adding it to the queue
          while temp:
            
            if visited[temp.data] == False:
              q.append(temp.data)
              visited[temp.data] = True

            temp = temp.next

        return "".join(result)  # O(n)


if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    print(g.bfs_traversal(0))

    
