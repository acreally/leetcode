from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        result = []
        edges = set([(prereq[0], prereq[1]) for prereq in prerequisites])
        adjacency_lists = self.build_adjacency_lists(numCourses, prerequisites)
        no_prereqs = set([i for i in range(numCourses)])
        for edge in prerequisites:
            no_prereqs.discard(edge[0])

        while no_prereqs:
            current = no_prereqs.pop()
            result.append(current)
            for node in adjacency_lists[current]["out"]:
                edges.discard((node, current))
                adjacency_lists[node]["in"].discard(current)
                if not adjacency_lists[node]["in"]:
                    no_prereqs.add(node)

        if edges:
            return []        
        return result

    def build_adjacency_lists(self, numCourses: int, prerequisites: List[List[int]]) -> dict:
        adjacency_lists = {i: {"in": set(), "out": set()} for i in range(numCourses)}
        for prereq in prerequisites:
            adjacency_lists[prereq[1]]["out"].add(prereq[0])
            adjacency_lists[prereq[0]]["in"].add(prereq[1])
        return adjacency_lists
