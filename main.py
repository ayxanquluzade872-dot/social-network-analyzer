import json
from graph import Graph
import algorithms as algo

# Load data
def load_graph(filename):
    g = Graph()
    with open(filename) as f:
        data = json.load(f)

    for user in data:
        for friend in data[user]:
            g.add_connection(user, friend)
    return g


def menu():
    print("\n--- Social Network Analyzer ---")
    print("1. Show users")
    print("2. Shortest connection")
    print("3. Most popular user")
    print("4. Mutual friends")
    print("5. Friend recommendation")
    print("6. Connected components")
    print("0. Exit")


def main():
    graph = load_graph("data.json")

    while True:
        menu()
        choice = input("Select: ")

        if choice == "1":
            print("Users:", graph.users())

        elif choice == "2":
            u = input("From: ")
            v = input("To: ")
            print("Distance:", algo.shortest_path(graph, u, v))

        elif choice == "3":
            print("Most popular:", algo.most_popular(graph))

        elif choice == "4":
            u = input("User 1: ")
            v = input("User 2: ")
            print("Mutual:", algo.mutual_friends(graph, u, v))

        elif choice == "5":
            u = input("User: ")
            print("Recommendations:", algo.recommend_friends(graph, u))

        elif choice == "6":
            print("Connected components:", algo.connected_components(graph))

        elif choice == "0":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
