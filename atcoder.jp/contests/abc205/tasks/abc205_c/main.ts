import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const solve = (a: number, b: number, c: number) => {
  if (c % 2 == 0) {
    if (Math.abs(a) < Math.abs(b)) return "<";
    if (Math.abs(a) > Math.abs(b)) return ">";
    return "=";
  }
  if (a < b) return "<";
  if (a > b) return ">";
  return "=";
};

const [A, B, C] = input().split(" ").map(Number);
console.log(solve(A, B, C));
