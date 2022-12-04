import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const solve = (a: number, b: number) => {
  if (a + b === 15) return "+";
  if (a * b === 15) return "*";
  return "x";
};

const main = () => {
  const [a, b] = input().split(" ").map(Number);
  console.log(solve(a, b));
};

main();
