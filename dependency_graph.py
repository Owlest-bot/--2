from graphviz import Digraph
import apt


def generate_dependency_graph(package_name, depth, repository_url):
    graph = Digraph('G', format='png')
    queue = [(package_name, 0)]
    visited = set()

    while queue:
        current_package, current_depth = queue.pop(0)
        if current_depth <= depth:
            if current_package not in visited:
                graph.node(current_package)
                dependencies = apt.get_dependencies(current_package)
                for dep in dependencies:
                    graph.edge(current_package, dep)
                    queue.append((dep, current_depth + 1))
                visited.add(current_package)

    graph.render('dependency_graph')
