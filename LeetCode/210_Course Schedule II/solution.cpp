class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> topoOrder;
        vector<int> indegrees(numCourses, 0);
        vector<vector<int>> adjList(numCourses);

        // Build graph: `[a, b]` means "take b before a"
        for (auto prerequisite : prerequisites) {
            indegrees[prerequisite[0]] += 1;
            adjList[prerequisite[1]].push_back(prerequisite[0]); // Note which is which here
        }

        // Here, instead of set we use queue so I can pop() easily
        queue<int> noPrereqs;
        for (int i = 0; i < numCourses; i++) {
            if (indegrees[i] == 0) { // check indegree, not adjList size
                noPrereqs.push(i);
            }
        }

        // Kahn's main loop
        while (!noPrereqs.empty()) {
            int currNode = noPrereqs.front();
            noPrereqs.pop();
            topoOrder.push_back(currNode);

            // For every neighbour v of u, remove edge u → v
            for (int neighbor : adjList[currNode]) {
                indegrees[neighbor] -= 1;       // "virtually remove" edge
                if (indegrees[neighbor] == 0) { // if v has no more incoming edges
                    noPrereqs.push(neighbor);   //      put v into S
                }
            }
        }

        // If cycle exists, not all courses can be finished
        if (topoOrder.size() != numCourses) return {};

        return topoOrder;
    }
};
