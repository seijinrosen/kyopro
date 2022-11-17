import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const A = [
  1, 1, 1, 2, 1, 2, 1, 5, 2, 2, 1, 5, 1, 2, 1, 14, 1, 5, 1, 5, 2, 2, 1, 15, 2,
  2, 5, 4, 1, 4, 1, 51,
];

const main = () => {
  const K = +input();

  const ans = A[K - 1];
  console.log(ans);
};

main();
