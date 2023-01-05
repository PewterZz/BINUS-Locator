/**
 *  All pair shortest path algo : Complexity O(V^2logV + VE) in case if Dijkstra uses fibonacci heap
 * 
 */
#include<bits/stdc++.h>
using namespace std;

#define V 4

#define INF INT_MAX

class MinHeapMap {
    std::vector<std::pair<int, int>> min_heap;
    std::map<int, int> vertex_position;

    // Add, Decrease, extract_min, contains
    public:
    void add(int u, int weight) {
        min_heap.push_back(std::make_pair(weight, u));
        int current_index = min_heap.size() - 1;
        int parent_index = (current_index - 1) / 2;
        while(parent_index < current_index && parent_index >= 0) {
            int parent_weight = min_heap[parent_index].first;
            if (parent_weight > weight) {
                min_heap[current_index].first = parent_weight;
                min_heap[parent_index].first = weight;
                current_index = parent_index;
                parent_index = (current_index - 1) / 2;
            } else {
                break;
            }
        }
        vertex_position.insert(std::make_pair(u, current_index));
    }

    int contains(int u) {
        auto itr = vertex_position.find(u);
        if(itr == vertex_position.end()) {
            return -1;
        } else {
            return itr->second;
        }
    }

    auto extract_min() {
        auto min = min_heap[0];
        int index = 0;
        int size = min_heap.size();
        min_heap[0] = min_heap[size-1];
        min_heap.pop_back();
        vertex_position.erase(min.second);
        int last_parent = (size - 1) / 2;
        while (index <= last_parent) {
            int left = (2 * index) + 1;
            int right = (2 * index) + 2;
            int index_compare = min_heap[left].first < min_heap[right].first ? left : right;
            if(min_heap[index].first > min_heap[index_compare].first) {
                auto t = min_heap[index];
                min_heap[index] = min_heap[index_compare];
                min_heap[index_compare] = t;
                // Update positions
                vertex_position[min_heap[index].second] = index;
                vertex_position[min_heap[index_compare].second] = index_compare;
                index = index_compare;
            } else {
                break;
            }
        }
        return min;
    }

    int get_weight(int u) {
        int index = vertex_position.find(u)->second;
        return min_heap[index].first;
    }

    void decrease(int u, int weight) {
        int index = vertex_position.find(u)->second;
        min_heap[index].first = weight;
        int parent_index = (index - 1) / 2;
        while (index > 0 && min_heap[parent_index].first > weight) {
            auto t = min_heap[index];
            min_heap[index] = min_heap[parent_index];
            min_heap[parent_index] = t;
            // Update positions
            vertex_position[min_heap[index].second] = index;
            vertex_position[min_heap[parent_index].second] = parent_index;
            index = parent_index;
            parent_index = (index - 1) / 2;
        }
    }

    void print() {
        for(auto heap: min_heap) {
            std::cout<< heap.first << " (" << heap.second << ")\t";
        }
    }

    int size() {
        return min_heap.size();
    }
};

class WeightedGraph {
    int vertices;
    int total_edges = 0;
    std::vector<std::list<std::pair<int, int>>> edges;

    public:
    WeightedGraph(int n) {
        vertices = n;
        edges.resize(n+1);
    }

    void add_edge(int u, int v, int weight) {
        edges[u].push_back(std::make_pair(v, weight));
        total_edges++;
        if (u >= vertices) {
            vertices = u;
        }
    }

    void print_graph() {
        int i = 0;
        while(i <= vertices) {
            std::cout << i;
            for(auto v : edges[i]) {
                std::cout << "-->" << v.first << " (" << v.second<< ")";
            }
            std::cout<<std::endl;
            i++;
        }
    }

    void update_adjacency_list(int src, std::list<std::pair<int, int>> adj_list) {
        edges[src] = adj_list;
    }

    int get_total_edges() {
        return this->total_edges;
    }

    auto get_edges() {
        return edges;
    }

    auto get_vertices() {
        return vertices;
    }

};

bool bellman_ford(WeightedGraph *wg, int h[V]) {
    for(int i = 0; i < V; i++) {
        // Iterate over all the edges and relax
        int src = 0, dest, weight;
        for(auto adjacency_edges : wg->get_edges()) {
            for (auto edge: adjacency_edges) {
                dest = edge.first;
                weight = edge.second;
                // Relax the edges
                if(h[src] != INF && h[dest] > h[src] + weight) {
                    h[dest] = h[src] + weight;
                }
            }
            src++;
        }
    }

    // Check negative weights and adjust the wieghts also in graph to remove negative weights
    int src = 0, dest, weight;
    for(auto adjacency_edges : wg->get_edges()) {
        list<pair<int, int>> modified_edges;
        for (auto edge: adjacency_edges) {
            dest = edge.first;
            weight = edge.second;
            modified_edges.push_back(make_pair(dest, edge.second + h[src] - h[dest]));
            // relax the edge
            if(h[src] != INF && h[dest] > h[src] + weight) {
                cout<< "Negative Weight Cycle found";
                return true;
            }
        }
        wg->update_adjacency_list(src, modified_edges);
        src++;
    }

    // wg->print_graph();

    // cout<<"h function values\n";
    // for(int i=0; i<=V; i++) {
    //     cout<<h[i]<<'\t';
    // }
    return false;
}

vector<int> dijkstra(int src, WeightedGraph *wg) {
    vector<int> dist;

    MinHeapMap min_heap;
    for(int i=0; i<V; i++) {
        min_heap.add(i, INF);
        dist.push_back(INF);
    }
    min_heap.decrease(src, 0);
    dist[src] = 0;

    while(min_heap.size() > 0) {
        auto min_extracted = min_heap.extract_min();
        int root = min_extracted.second;
        // Get adjacency list of the root
        auto adjacency_root = wg->get_edges()[root];
        for(auto adj_root_vertex : adjacency_root) {
            int distance = min_extracted.first + adj_root_vertex.second;
            if(min_heap.contains(adj_root_vertex.first) != -1 && min_heap.get_weight(adj_root_vertex.first) > distance) {
                min_heap.decrease(adj_root_vertex.first, distance);
                dist[adj_root_vertex.first] = distance;
            }
        }
    }
    return dist;
}

void johnson(WeightedGraph *wg) {
    int h[V+1];
    vector<vector<int>> dist;

    // Run Bellman ford to remove negative weights and assign a wieght value for all node from a newly added node
    // 1- add and edge from new vertex to all vertex with 0 weight
    for (int i = 0; i < V; i++) {
        wg->add_edge(V, i, 0);
        h[i] = INF;
    }

    // 2- using V as a source run Bellman ford
    h[V] = 0;
    if (bellman_ford(wg, h)) {
        // Negative Weight Cycle found
        return;
    }

    // 3 Run Dijkstra V time while treating each node as a source
    for(int i = 0; i < V; i++) {
        dist.push_back(dijkstra(i, wg));
    }

    cout<<"\nDistance Matrix is:\n"; 
    for(int i =0; i< V; i++) {
        for(int j=0; j<V; j++) {
            if (dist[i][j] == INF) {
                cout<< "INF\t";
            } else {
                cout<< dist[i][j] - h[i] + h[j] << "\t";
            }
        }
        cout<<"\n";
    }

}

int main() {
    WeightedGraph wg(V);
    wg.add_edge(0, 1, -5);
    wg.add_edge(0, 2, 2);
    wg.add_edge(0, 3, 3);
    wg.add_edge(1, 2, 4);
    wg.add_edge(2, 3, 1);

    // wg.print_graph();

    johnson(&wg);
    return 0;
}