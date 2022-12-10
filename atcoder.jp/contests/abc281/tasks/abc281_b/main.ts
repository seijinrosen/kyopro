import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const isUpper = (s: string) => isNaN(+s) && s.toUpperCase() === s;

const solve = (s: string) => {
  if (s.length !== 8) return false;
  if (!isUpper(s[0])) return false;
  if (!isUpper(s.slice(-1))) return false;
  const n = +s.slice(1, -1);
  return 100000 <= n && n <= 999999;
};

const main = () => {
  console.log(solve(input()) ? "Yes" : "No");
};

main();
