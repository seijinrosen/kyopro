import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const range = (a: number, b?: number) =>
  b ? [...Array(b - a)].map((_, i) => a + i) : [...Array(a)].map((_, i) => i);
const sum = (array: number[]) => array.reduce((a, b) => a + b, 0);

const main = () => {
  const N = +input();
  const ans = sum(range(1, N + 1).filter((i) => i % 3 !== 0 && i % 5 !== 0));
  console.log(ans);
};

main();
