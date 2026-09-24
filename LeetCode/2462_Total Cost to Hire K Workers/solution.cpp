#include <vector>
#include <deque>
#include <queue>
using namespace std;

class Solution {
public:
    long long totalCost(vector<int>& costs, int k, int candidates) {
        struct Worker {
            int cost;
            bool isFront;
        };

        struct ByCostMin {
            bool operator()(const Worker& a, const Worker& b) const {
                return a.cost > b.cost; // min-heap by cost
            }
        };

        long long total = 0;
        priority_queue<Worker, vector<Worker>, ByCostMin> pq;

        // Convert costs into a Deque for efficient pop_front() and pop_back().
        // O(n)
        deque<int> costs_dq(costs.begin(), costs.end());

        // Seed: take up to 'candidates' from front and back, without crossing
        for (int i = 0; i < candidates && !costs_dq.empty(); i++) {
            pq.push(Worker{costs_dq.front(), true});
            costs_dq.pop_front();
            if (costs_dq.empty()) break;
            pq.push(Worker{costs_dq.back(), false});
            costs_dq.pop_back();
        }

        for (int i = 0; i < k; i++) {
            Worker w = pq.top();
            pq.pop();
            total += w.cost;

            if (costs_dq.empty()) continue;

            if (w.isFront) {
                pq.push(Worker{costs_dq.front(), true});
                costs_dq.pop_front();
            } else {
                pq.push(Worker{costs_dq.back(), false});
                costs_dq.pop_back();
            }
        }

        return total;
    }
};
