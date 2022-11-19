import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const main = () => {
  const [A, B, C] = input().split(" ").map(Number);
  console.log(A === B && B === C ? "Yes" : "No");
};

main();
