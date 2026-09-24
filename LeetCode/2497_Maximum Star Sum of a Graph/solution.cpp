class Solution {
public:
    int maxStarSum(vector<int>& vals, vector<vector<int>>& edges, int k) {
        int n = vals.size();
        vector<vector<pair<int,int>>> adj(n);
        vector<vector<int>> unsort_adj(n);
        
        // Build unsorted adj lists O(E)
        for (auto& e : edges) {
            int u = e[0], v = e[1];
            unsort_adj[u].push_back(v);
            unsort_adj[v].push_back(u);
        }
        
        // For each node: sort neighbors descending, keep top k+1 O(E log d)
        int ans = *max_element(vals.begin(), vals.end());
        for (int i = 0; i < n; ++i) {
            // Get reference to this node's neighbor list to avoid copying
            vector<pair<int, int>>& node_neighbors = adj[i];

            // Add all neighbors as (value, index) pairs
            for (int neighbor_index : unsort_adj[i]) {
                int neighbor_value = vals[neighbor_index];
                node_neighbors.push_back({neighbor_value, neighbor_index});
            }
            // Sort neighbors by value DESCENDING, then by index ASC
            sort(node_neighbors.begin(), node_neighbors.end(), greater<pair<int, int>>());

            // Keep only top (k+1) neighbors (we need k max, +1 safety)
            if (node_neighbors.size() > k + 1) {
                node_neighbors.resize(k + 1);
            }
            
            // Compute star sum
            int sum = vals[i];
            for (int j = 0; j < k && j < (int)node_neighbors.size(); ++j) {
                if (node_neighbors[j].first > 0) sum += node_neighbors[j].first;
            }
            ans = max(ans, sum);
        }
        return ans;
    }
};
