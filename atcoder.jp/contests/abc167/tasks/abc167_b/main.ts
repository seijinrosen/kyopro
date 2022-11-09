import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const main = () => {
  const [A, B, C, K] = input().split(" ").map(Number);

  const a = Math.min(A, K);
  const b = Math.min(B, K - a);
  const c = K - a - b;
  const ans = a - c;

  console.log(ans);
};

main();
