class Solution {
public:
    int minMutation(string startGene, string endGene, vector<string>& bank) {
        unordered_set<string> hashTable; // valid genes in bank
        for (const string& valid_gene : bank) {
            hashTable.insert(valid_gene);
        }

        if (!hashTable.count(endGene)) {
            return -1;
        }

        // Helper function to get valid neighbours given a gene
        auto getNeighbour = [&](const string& gene) {
            vector<string> neighbours;

            for (int i = 0; i < gene.length(); i++) {
                for (char gene_char : string("ACGT")) {
                    if (gene[i] != gene_char) {
                        string mutated = gene;
                        mutated[i] = gene_char;

                        if (hashTable.count(mutated)) {
                            // exist in hashtable bank...
                            neighbours.push_back(mutated);
                        }
                    }
                }
            }

            return neighbours;
        };

        // BFS logic, using getNeighbour
        queue<pair<string, int>> q;
        unordered_set<string> visited;

        q.push({startGene, 0});  // FORMAT: {gene, dist}
        visited.insert(startGene);

        while (!q.empty()) {
            auto [currGene, dist] = q.front();
            q.pop();

            if (currGene == endGene) {
                // terminating condition
                return dist;
            }

            // for every valid neighbour...
            for (const string& nextGene : getNeighbour(currGene)) {
                if (!visited.count(nextGene)) {
                    visited.insert(nextGene);
                    q.push({nextGene, dist + 1});
                }
            }
        }

        return -1; // No valid solution
    }
};
