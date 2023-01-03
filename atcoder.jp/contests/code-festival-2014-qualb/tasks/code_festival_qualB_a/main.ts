import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const [A, B] = input().split(" ").map(Number);

const ans = Math.max(A, B);

console.log(ans);
