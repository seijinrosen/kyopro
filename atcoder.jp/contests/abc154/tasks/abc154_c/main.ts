import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const N = +input();
const A = input().split(" ").map(Number);

const ans = new Set(A).size === N;

console.log(ans ? "YES" : "NO");
