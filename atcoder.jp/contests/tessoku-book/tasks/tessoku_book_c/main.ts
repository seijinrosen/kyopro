import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const yesNo = (b: boolean | number) => (b ? "Yes" : "No");

// input functions -------------------------------------------------------------
const inputNumberArray = (): number[] => input().split(" ").map(Number);
// input functions -------------------------------------------------------------

const [N, K] = inputNumberArray();
const P = inputNumberArray();
const Q = inputNumberArray();

let ans = false;
for (const p of P) for (const q of Q) if (p + q === K) ans = true;

print(yesNo(ans));
