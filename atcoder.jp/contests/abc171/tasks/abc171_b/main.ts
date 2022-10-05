import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const sorted = <T extends number | bigint>(array: T[]) =>
  array.slice().sort((a, b) => (a < b ? -1 : a > b ? 1 : 0));
const sum = (array: number[]): number => array.reduce((a, b) => a + b, 0);

// input functions -------------------------------------------------------------
const inputNumberArray = (): number[] => input().split(" ").map(Number);
// input functions -------------------------------------------------------------

const main = () => {
  const [N, K] = inputNumberArray();
  const P = inputNumberArray();

  const ans = sum(sorted(P).slice(0, K));
  print(ans);
};

main();
