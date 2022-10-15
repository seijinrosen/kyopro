import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const sum = (array: number[]) => array.reduce((a, b) => a + b, 0);

const main = () => {
  const [N, K, M] = input().split(" ").map(Number);
  const A = input().split(" ").map(Number);

  const x = N * M - sum(A);
  const ans = K < x ? -1 : Math.max(x, 0);

  console.log(ans);
};

main();
