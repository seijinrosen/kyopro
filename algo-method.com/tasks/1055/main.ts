import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const sum = (data: number[]) => data.reduce((a, b) => a + b);

const N = +input();
const F = input().split(" ").map(Number);

const ans = sum(F.map((f) => 1 << f));
print(ans);
