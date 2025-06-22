import networkx as nx
from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._idmap = {}

    def build_graph(self):
        self._grafo.clear()
        self._idmap.clear()
        nodi = DAO.get_nodi()
        if not nodi:
            return
        for x in nodi:
            self._idmap[int(x.object_id)] = x
        self._grafo.add_nodes_from(nodi)
        archi = DAO.get_archi()
        for id1, id2 in archi:
            if int(id1) in self._idmap and int(id2) in self._idmap:
                o1 = self._idmap[int(id1)]
                o2 = self._idmap[int(id2)]

                if self._grafo.has_edge(o1, o2):
                    # Incrementa il peso dell’arco esistente
                    self._grafo[o1][o2]['weight'] += 1
                else:
                    # Crea un nuovo arco con peso iniziale 1
                    self._grafo.add_edge(o1, o2, weight=1)


    def getGraphDetails(self):
        return self._grafo.number_of_nodes(), self._grafo.number_of_edges()

    def getConnessa(self, id):
        if int(id) in self._idmap.keys():
            component = nx.node_connected_component(self._grafo, self._idmap[int(id)])
            leng = len(component)
            return leng

    def getOptPath(source, lunInt):
        pass

