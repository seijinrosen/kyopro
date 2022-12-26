import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const solve = (day: string) => {
  if (day === "Monday") return 5;
  if (day === "Tuesday") return 4;
  if (day === "Wednesday") return 3;
  if (day === "Thursday") return 2;
  if (day === "Friday") return 1;
  return 0;
};

console.log(solve(input()));
