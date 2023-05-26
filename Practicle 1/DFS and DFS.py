graph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = [];
queue = [];
def bfs(visited,graph,start,goal):
    visited.append(start);
    queue.append(start);

    while queue:
        m = queue.pop(0);
        print(m);
        if(m == goal):
            print("Goal Node Found");
            break;
        else:
            for n in graph[m]:
                if n not in visited:
                    visited.append(n);
                    queue.append(n);

print("BFS Traversal:");
bfs(visited,graph,'A','F');

print("------------------------------------------------------------------");

graph = {
    'A' : ['B','C'],
    'B' : ['D','E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = [];
stack = [];
def dfs(graph,start,goal):
    visited.append(start);
    stack.append(start);

    while stack:
        m = stack[-1];
        stack.pop();
        print(m);
        if(m == goal):
            print("Goal Node Found");
            break;
        else:
            for n in graph[m]:
                if n not in visited:
                    visited.append(n);
                    stack.append(n);

print("DFS Traversal:");
dfs(graph,'A','E');