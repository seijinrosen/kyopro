import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const [N, X] = input().split(" ").map(Number);

const ans = N & (1 << X) ? "Yes" : "No";
print(ans);
