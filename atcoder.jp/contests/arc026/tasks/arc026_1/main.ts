import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const [N, A, B] = input().split(" ").map(Number);

const b = Math.min(5, N);
const a = N - b;
const ans = A * a + B * b;

console.log(ans);
