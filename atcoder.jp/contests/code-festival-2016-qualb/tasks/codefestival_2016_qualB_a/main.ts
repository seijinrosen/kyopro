import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const S = input();
const T = "CODEFESTIVAL2016";

let ans = 0;
for (let i = 0; i < S.length; i++) if (S[i] != T[i]) ans++;

console.log(ans);
