import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const N = +input();
const S = input();

for (let i = 1; i < N; i++) {
  let l = 0;

  for (let k = 0; k < N - i; k++) {
    if (S[k] === S[k + i]) break;
    l++;
  }

  console.log(l);
}
