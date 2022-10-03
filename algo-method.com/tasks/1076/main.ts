import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const sum = (array: number[]): number => array.reduce((a, b) => a + b, 0);

// input functions -------------------------------------------------------------
const inputNumberArray = (): number[] => input().split(" ").map(Number);
// input functions -------------------------------------------------------------

const main = () => {
  const [N, K] = inputNumberArray();
  const V = inputNumberArray();

  const ans = sum(V.map((v) => 1 << v));
  print(ans);
};

main();
