import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const range = (a: number, b?: number): number[] =>
  b ? [...Array(b - a)].map((_, i) => a + i) : [...Array(a)].map((_, i) => i);
const yesNo = (b: boolean | number) => (b ? "Yes" : "No");

// input functions -------------------------------------------------------------
const inputNumberArray = (): number[] => input().split(" ").map(Number);
// input functions -------------------------------------------------------------

const [A, B] = inputNumberArray();

const ans = range(A, B + 1).some((i) => 100 % i === 0);
print(yesNo(ans));
