class Graph:
    def __init(self):
        self.nodes = []
        self.maps = {}
        
        def getOrCreateNode(self, name):
            if name not in self.map:
                node = Project(name)
                self.nodes.append(node)
                self.map[name] = node
            return self.map[name]

        def addEdge(self, fisrt, second):
            start = Project(self.getOrCreateNode(first))
            end = Project(self.getOrCreateNode(second))
            start.addNeighbor(end)

        deg getNodes(self):
            return self.nodes

class Project:
    def __init__(self, name):
        self.children = []
        self.map = {}
        self.name = name
        self.dependencies = 0

        def addNeighbor(self, node):
            if node.getName() not in self.map:
                self.children.append(node)
                map[node.getName()]=node
                node.increaseDependencies()

        def increaseDependencies(self):
            self.dependencies+=1

        def decrementDependencies(self):
            self.dependencies-=1

        def getName(self):
            return self.name
        
        def getChildren(self):
            return self.children
    
        def getNumberDependencies(self):
            return self.dependencies

def findBuildOrder(projects, dependencies):
    graph = buildGraph(projects, dependencies)
    return orderProjects(graph.getNodes())

def buildGraph(projects, dependencies):
    graph = Graph()
    for project in projects:
        graph.getOrCreateNode(project)

    for dependency in dependencies:
        first = dependency[0]; second = dependency[1]
        graph.addEdge(first, second)

    return graph

def orderProject(projects):
    order = []
    endOfList = addNonDependent(order, projects, 0)

    toBeProcessed = 0
    while toBeProcessed < len(order):
        current = order[toBeProcessed]
        
        if not current: return None
        children = current.getChildren()
        for child in children:
            child.drementDependencies()

        endOfList = addNonDependent(order, children, endOfList)
        
    return order


def addNonDependent(order, projects, offset):
    for project in projects:
        if project.getNumberDependencies() == 0:
            order[offset] = project
            offset +=1
    return offset
    
project = [a,b,c,d,e,f]
dependencies = [[a,b],[f,b],[b,d],[f,a],[d,c]]
findBuildOrder(project, dependencies)

