import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const [_N, P, Q, R, S] = input().split(" ").map(Number);
const A = input().split(" ").map(Number);

const ans = A.slice(0, P - 1)
  .concat(A.slice(R - 1, S))
  .concat(A.slice(Q, R - 1))
  .concat(A.slice(P - 1, Q))
  .concat(A.slice(S));

console.log(ans.join(" "));
