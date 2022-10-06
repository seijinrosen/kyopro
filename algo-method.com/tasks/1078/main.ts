import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const range = (a: number, b?: number) =>
  b ? [...Array(b - a)].map((_, i) => a + i) : [...Array(a)].map((_, i) => i);

// input functions -------------------------------------------------------------
const inputNumberArray = () => input().split(" ").map(Number);
// input functions -------------------------------------------------------------

const main = () => {
  const [N, X] = inputNumberArray();

  const ans = range(N).filter((i) => 0 < ((1 << i) & X));

  print(ans.length);
};

main();
