function solution(n, s, a, b, fares) {
    const INF = 10000000;
    let answer = INF;
    const floyd = Array.from(Array(n+1), () => Array(n+1).fill(INF)).map((e, i) => {e[i] = 0; return e});

    fares.forEach((e) => {
        floyd[e[0]][e[1]] = floyd[e[1]][e[0]] = e[2];
    })

    for(let k=1; k<=n; k++){
        for(let i=1; i<=n; i++){
            for(let j=1; j<=n; j++){
                if(floyd[i][k] + floyd[k][j] < floyd[i][j]){
                    floyd[i][j] = floyd[i][k] + floyd[k][j];
                }
            }
        }
    }
    
    for(let k=1; k<=n; k++){
        const dist = floyd[s][k] + floyd[k][a] + floyd[k][b];
        answer = dist > answer ? answer : dist;
    }
    
    return answer;
}