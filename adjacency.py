from collections import deque

class MetroNetwork:
    def __init__(self, stations):
        self.stations = stations
        self.n = len(stations)

        # Adjacency Matrix (n x n), sab 0 se initialize
        self.matrix = [[0] * self.n for _ in range(self.n)]

    # Station name → index
    def get_index(self, name):
        return self.stations.index(name)

    # Add direct connection (undirected)
    def add_connection(self, s1, s2):
        i = self.get_index(s1)
        j = self.get_index(s2)
        self.matrix[i][j] = 1
        self.matrix[j][i] = 1   # undirected

    # Display Adjacency Matrix
    def show_matrix(self):
        print("\n📊 Adjacency Matrix:")
        print(" " * 16, end="")
        for i in range(self.n):
            print(f"[{i}]", end=" ")
        print()

        for i in range(self.n):
            print(f"[{i}] {self.stations[i]:<12}", end="")
            for j in range(self.n):
                print(f" {self.matrix[i][j]} ", end="")
            print()

    # Check direct connection
    def is_connected(self, s1, s2):
        i = self.get_index(s1)
        j = self.get_index(s2)
        return self.matrix[i][j] == 1

    # Find neighbors (direct connected stations)
    def get_neighbors(self, station):
        i = self.get_index(station)
        neighbors = []
        for j in range(self.n):
            if self.matrix[i][j] == 1:
                neighbors.append(self.stations[j])
        return neighbors

    # Degree of a station (kitne direct connections)
    def degree(self, station):
        i = self.get_index(station)
        return sum(self.matrix[i])

    # BFS — shortest route (number of stops)
    def shortest_route(self, start, end):
        start_i = self.get_index(start)
        end_i = self.get_index(end)

        visited = [False] * self.n
        queue = deque([(start_i, [start])])
        visited[start_i] = True

        while queue:
            curr, path = queue.popleft()
            if curr == end_i:
                return path

            for j in range(self.n):
                if self.matrix[curr][j] == 1 and not visited[j]:
                    visited[j] = True
                    queue.append((j, path + [self.stations[j]]))

        return None  # No route


# ---------- MAIN ----------
if __name__ == "__main__":
    stations = [
        "Rajiv Chowk",
        "Karol Bagh",
        "Mandi House",
        "Patel Nagar",
        "Pragati Maidan",
        "Kirti Nagar"
    ]

    metro = MetroNetwork(stations)

    # Connections add karo
    metro.add_connection("Rajiv Chowk", "Karol Bagh")
    metro.add_connection("Rajiv Chowk", "Mandi House")
    metro.add_connection("Karol Bagh", "Patel Nagar")
    metro.add_connection("Patel Nagar", "Kirti Nagar")
    metro.add_connection("Mandi House", "Pragati Maidan")

    print("=== 🚇 Metro Rail Network (Adjacency Matrix) ===")

    # Matrix display
    metro.show_matrix()

    # Direct connection check
    print("\n🔍 Connection Checks:")
    print(f"Rajiv Chowk ↔ Karol Bagh    : {metro.is_connected('Rajiv Chowk', 'Karol Bagh')}")
    print(f"Rajiv Chowk ↔ Kirti Nagar   : {metro.is_connected('Rajiv Chowk', 'Kirti Nagar')}")
    print(f"Mandi House ↔ Pragati Maidan: {metro.is_connected('Mandi House', 'Pragati Maidan')}")

    # Neighbors
    print("\n🔗 Direct Connections (Neighbors):")
    for s in stations:
        print(f"  {s:<16} → {metro.get_neighbors(s)}")

    # Degree
    print("\n📈 Station Degree (Number of Connections):")
    for s in stations:
        print(f"  {s:<16} : {metro.degree(s)}")

    # Shortest Route
    print("\n🛤️ Shortest Route:")
    route = metro.shortest_route("Kirti Nagar", "Pragati Maidan")
    if route:
        print(f"  Kirti Nagar → Pragati Maidan:")
        print(f"  {' → '.join(route)}")
        print(f"  Total stops: {len(route) - 1}")
    else:
        print("  No route found")