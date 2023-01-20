import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

input();
const P = input().split(" ").map(Number);

const cnt = P.filter((p, i) => i + 1 !== p).length;
const ans = cnt === 0 || cnt === 2;

console.log(ans ? "YES" : "NO");
