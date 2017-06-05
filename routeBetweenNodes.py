Class State:
    Unvisited, Visited, Visiting = Range(3)

Class Solutions:
    def search(graph, start, end):
        if start == end: return True
        q = []
        for g in graph.getNodes():
            g.state = State.Unvisited
        start.state = State.Visiting
        q.append(start)
        while q:
            u = q.pop(0)
            if u:
                for n in u.getAdjacent():
                    if n.state == State.Unvisited:
                        if n == end:
                            return True
                        else:
                            n.state = State.Visiting
                u.state = State.Visited
        return False
