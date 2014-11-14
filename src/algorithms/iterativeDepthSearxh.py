
def iter_dfs(G,s):
    """docstring for iter_dfs"""
    S, Q = set(), []
    Q.append(s)
    while Q:
        u = Q.pop()
        if u in S: continue
        S.add(u)
        Q.extend(g[u])
        yield u
