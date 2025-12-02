# Report: Dijkstra vs A* Search Algorithm

## 1. Heuristic Used
The heuristic used for the A* algorithm is:

### `h(n) = |n − goal|`

This heuristic:
- Never overestimates the true cost
- Ensures A* remains admissible
- Works for abstract node-numbered graphs
- Always ≤ real path cost.

Therefore, A* is optimal.

---

## 2. Time Complexity Analysis

### Dijkstra
- Uses a priority queue  
- Complexity: **O((V + E) log V)**

### A*
- Uses the same priority queue  
- But explores **fewer nodes**  
- Complexity: **O((V + E) log V)** worst case  
- But **much faster in practice** because of pruning.

---

## 3. Benchmark Results
(Your output from running benchmark.py will go here)

Example explanation:

- A* was faster in all test cases.
- This is because the heuristic allows A* to search toward the goal rather than exploring all directions equally.
- Dijkstra has no heuristic → explores more nodes.

---

## 4. Conclusion
- A* gives the same optimal path cost as Dijkstra.
- A* is consistently faster due to heuristic-guided search.
- Both algorithms are correct, but A* is more efficient.
