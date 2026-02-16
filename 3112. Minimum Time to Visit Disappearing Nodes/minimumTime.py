class Solution(object):
    def minimumTime(self, n, edges, disappear):
        """
        :type n: int
        :type edges: List[List[int]]
        :type disappear: List[int]
        :rtype: List[int]
        """
        visited = [0]
        nodes = set()
        node_edges = dict()
        # get all nodes
        while len(nodes) < n:
            for edge in edges:
                nodes.update(edge[:-1])
                if edge[0] in node_edges:
                    node_edges[edge[0]].append(edge)
                else:
                    node_edges[edge[0]] = [edge]

        # keep track of visited
        visited = []
        # initialize distances
        distances = {node: float('inf') for node in nodes}
        distances[0] = 0

        # get initial distances from 0
        for edge in edges:
            if edge[0] == 0 and edge[1] != 0:
                distances[edge[1]] = edge[2]

        unvisited = dict(distances)
        unvisited.pop(0)

        # print(f"Initial distances: {distances}")
        # print(f"Initial unvisited: {unvisited}")

        while len(unvisited.keys()) > 0:
            # find node that has not been visited and has shortest distance
            unvisited_min = min(unvisited, key=unvisited.get)
            # go through all nodes reachable from current node by checking edges
            if unvisited_min in node_edges:
                for edge in node_edges[unvisited_min]:
                    # if the current node has disappeared sooner than it takes to reach, update it as unreachable
                    if distances[unvisited_min] >= disappear[unvisited_min]:
                        distances[unvisited_min] = float('inf')
                        continue
                    # if the current distance to this node is greater than from current node, update it
                    if distances[edge[1]] > distances[unvisited_min] + edge[2]:
                        # print(f'updating distance from {unvisited_min} to {edge[1]} as the sum of distance to current node ({distances[unvisited_min]}) + weight of edge ({edge[2]})')
                        distances[edge[1]] =  distances[unvisited_min] + edge[2]
            else:
                # if the current node has disappeared sooner than it takes to reach, update it as unreachable
                if distances[unvisited_min] >= disappear[unvisited_min]:
                    distances[unvisited_min] = float('inf')

            unvisited.pop(unvisited_min)


            

        # print(node_edges)
        # print(unvisited)
        # print(distances)

        return [x if x != float('inf') else -1 for x in distances.values()]
        

# print(Solution().minimumTime(3, [[0,1,2],[1,2,1],[0,2,4]], [1,1,5]))
# print(Solution().minimumTime(2, [[0,1,1]], [1,1]))
print(Solution().minimumTime(1, [[0,0,2],[0,0,2],[0,0,1],[0,0,3],[0,0,2],[0,0,4],[0,0,4]], [6]))
