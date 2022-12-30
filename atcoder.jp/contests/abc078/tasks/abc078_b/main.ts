import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const div = (x: number, y: number) => Math.floor(x / y);

const [X, Y, Z] = input().split(" ").map(Number);

const ans = div(X - Z, Y + Z);

console.log(ans);
