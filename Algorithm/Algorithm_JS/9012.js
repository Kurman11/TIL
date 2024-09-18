const input = require('fs').readFileSync('example.txt').toString().trim().split('\n');
const [n,...arr] = input;

for(let item of arr){
  const st =[]
  for(let value of item){
    if(value === '('){
      st.push('(')
    } else{
      if(st.length === 0){
        st.push(')')
      } else{
        if(st[st.length -1] === '('){
          st.pop()
        }
      }
    }
  }
  if(st.length === 0){
    console.log('YES')
  } else{
    console.log('NO')
  }
}
