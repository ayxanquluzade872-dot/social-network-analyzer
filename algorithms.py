from collections import deque

# BFS - shortest path
def shortest_path(graph, start, target):
    visited = set()
    queue = deque([(start, 0)])

    while queue:
        node, dist = queue.popleft()
        if node == target:
            return dist

        for nei in graph.get_neighbors(node):
            if nei not in visited:
                visited.add(nei)
                queue.append((nei, dist + 1))
    return -1


# DFS - connected components
def dfs(graph, node, visited):
    visited.add(node)
    for nei in graph.get_neighbors(node):
        if nei not in visited:
            dfs(graph, nei, visited)


def connected_components(graph):
    visited = set()
    count = 0

    for user in graph.users():
        if user not in visited:
            dfs(graph, user, visited)
            count += 1
    return count


# Most popular user
def most_popular(graph):
    return max(graph.users(), key=lambda x: len(graph.get_neighbors(x)))


# Mutual friends
def mutual_friends(graph, u, v):
    return list(set(graph.get_neighbors(u)) & set(graph.get_neighbors(v)))


# Friend recommendation
def recommend_friends(graph, user):
    recommendations = set()

    for friend in graph.get_neighbors(user):
        for friend_of_friend in graph.get_neighbors(friend):
            if friend_of_friend != user and friend_of_friend not in graph.get_neighbors(user):
                recommendations.add(friend_of_friend)

    return list(recommendations)
