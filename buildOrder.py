ss Graph:
    def __init__(self):
        self.nodes = []
        self.maps = {}
        
    def getOrCreateNode(self, name):
        if name not in self.maps:
            node = Project(name)
            self.nodes.append(node)
            self.maps[name] = node
        return self.maps[name]

    def addEdge(self, first, second):
        start = Project(self.getOrCreateNode(first))
        end = Project(self.getOrCreateNode(second))
        start.addNeighbor(end)
    def getNodes(self):
        return self.nodes

class Project:
    def __init__(self, name):
        self.children = []
        self.maps = {}
        self.name = name
        self.dependencies = 0

    def addNeighbor(self, node):
        if node.getName() not in self.maps:
            self.children.append(node)
            self.maps[node.getName()]=node
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
    print orderProject(graph.getNodes())
    return orderProject(graph.getNodes())

def buildGraph(projects, dependencies):
    graph = Graph()
    for project in projects:
        graph.getOrCreateNode(project)

    for dependency in dependencies:
        first = dependency[0]; second = dependency[1]
        graph.addEdge(first, second)

    return graph

def orderProject(projects):
    order = [[] for i in range(len(projects))]
    print "a"
    endOfList = addNonDependent(order, projects, 0)

    toBeProcessed = 0
    while toBeProcessed < len(order):
        current = order[toBeProcessed]
        print current
        if not current: return None
        children = current.getChildren()
        for child in children:
            child.drementDependencies()
            
        endOfList = addNonDependent(order, children, endOfList)
    print order  
    return order


def addNonDependent(order, projects, offset):
    for project in projects:
        if project.getNumberDependencies() == 0:
            order[offset] = project
            offset +=1
    return offset
    
project = ['a','b','c','d','e','f']
dependencies = [['a','b'],['f','b'],['b','d'],['f','a'],['d','c']]
findBuildOrder(project, dependencies)
