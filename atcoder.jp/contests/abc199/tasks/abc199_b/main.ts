import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const max = (array: number[]) => array.reduce((a, b) => Math.max(a, b));
const min = (array: number[]) => array.reduce((a, b) => Math.min(a, b));

const inputNumberArray = () => input().split(" ").map(Number);

const main = () => {
  const N = +input();
  const A = inputNumberArray();
  const B = inputNumberArray();

  const ans = Math.max(0, min(B) - max(A) + 1);
  console.log(ans);
};

main();
