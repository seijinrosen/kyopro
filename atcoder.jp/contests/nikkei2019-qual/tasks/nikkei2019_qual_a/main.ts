import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const main = () => {
  const [N, A, B] = input().split(" ").map(Number);
  console.log(Math.min(A, B), Math.max(0, A + B - N));
};

main();
