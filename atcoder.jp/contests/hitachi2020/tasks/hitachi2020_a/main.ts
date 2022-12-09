import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const solve = (s: string) => {
  if (s === "hi") return true;
  return s.slice(0, 2) === "hi" && solve(s.slice(2));
};

const main = () => {
  console.log(solve(input()) ? "Yes" : "No");
};

main();
