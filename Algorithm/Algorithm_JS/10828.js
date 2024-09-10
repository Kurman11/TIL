
// 그냥 elsem if 만 사용해봄
// const input = require('fs').readFileSync('example.txt').toString().trim().split('\n').map(line => line.trim().split(' '));
// const [n,...arr] = input;
// const arr1 =[]

// for (let i = 0; i<n; i++){
//   if (arr[i].length == 2){
//     arr1.push(arr[i][1]);
//   } else if(arr[i] == 'pop'){
//     if (arr1.length == 0){
//       console.log(-1);
//     } else {
//       console.log(arr1.pop());
//     }
//   } else if(arr[i] == 'size'){
//     console.log(arr1.length);
//   } else if(arr[i] == 'empty'){
//     if(arr1.length == 0){
//       console.log(1)
//     }else{
//       console.log(0)
//     }
//   } else if(arr[i] == 'top'){
//     if(arr1.length == 0){
//       console.log(-1)
//     } else{
//       console.log(arr1[arr1.length-1])
//     }
//   }
// }

// switch case 사용해봄
const input = require('fs').readFileSync('example.txt').toString().trim().split('\n').map(line => line.trim().split(' '));
const [n,...arr] = input;
const arr1 =[]

for(let i = 0; i < n; i++){
  switch(arr[i][0]){
    case 'pop':
      if (arr1.length != 0){
        console.log(arr1.pop())
      } else {
        console.log(-1)
      }
        break;

      case 'size':
        console.log(arr1.length)
        break;

      case 'empty':
        if (arr1.length != 0){
          console.log(0)
        } else {
          console.log(1)
        }
        break;

      case 'top':
        if (arr1.length != 0){
          console.log(arr1[arr1.length - 1])
        } else{
          console.log(-1)
        }
        break;

      default :
        arr1.push(arr[i][1])
        break;
  }
}