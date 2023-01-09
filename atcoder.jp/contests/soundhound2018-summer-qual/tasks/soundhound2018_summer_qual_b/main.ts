import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const S = input();
const w = +input();

let ans = "";
for (let i = 0; i < S.length; i += w) {
  ans += S[i];
}

console.log(ans);
