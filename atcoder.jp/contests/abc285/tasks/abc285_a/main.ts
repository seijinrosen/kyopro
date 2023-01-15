import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const div = (x: number, y: number) => Math.floor(x / y);

const [a, b] = input().split(" ").map(Number);

const ans = a === div(b, 2);

console.log(ans ? "Yes" : "No");
