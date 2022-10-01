import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const range = (a: number, b?: number): number[] =>
  b ? [...Array(b - a)].map((_, i) => a + i) : [...Array(a)].map((_, i) => i);
const sum = (array: number[]): number => array.reduce((a, b) => a + b, 0);

const [N, K] = input().split(" ").map(Number);

const ans = sum(
  range(1, N + 1)
    .map((i) => range(1, K + 1).map((j) => 100 * i + j))
    .flat()
);
print(ans);
