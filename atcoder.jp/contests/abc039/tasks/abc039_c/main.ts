import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const range = (a: number, b?: number): number[] =>
  b ? [...Array(b - a)].map((_, i) => a + i) : [...Array(a)].map((_, i) => i);

const S = input();

const X = "WBWBWWBWBWBW".repeat(2);
const Y = [
  "Do",
  "Do#",
  "Re",
  "Re#",
  "Mi",
  "Fa",
  "Fa#",
  "So",
  "So#",
  "La",
  "La#",
  "Si",
];

const map = new Map(range(12).map((i) => [X.slice(i, i + 12), Y[i]]));
const ans = map.get(S.slice(0, 12));

print(ans);
