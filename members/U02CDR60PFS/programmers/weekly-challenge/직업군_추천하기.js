function solution(table, languages, preference) {
    let answer = '';
    let max = -1;
    const prefer = {};   
    languages.forEach((el, i)=> prefer[el] = preference[i]);
    table.forEach((row)=> {
        row = row.split(" ");
        const job = row.shift();
        let score = 0;
        row.forEach((e, i)=> {
            score += (prefer[e] || 0) * (5-i);
        });
        if (max < score){
            max = score;
            answer = job;
        }
        else if (max === score){
            answer = answer > job ? job : answer;
        }
    })
    return answer;
}