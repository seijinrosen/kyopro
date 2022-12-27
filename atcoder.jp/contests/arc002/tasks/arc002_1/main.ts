import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const isLeap = (y: number) =>
  y % 400 === 0 ? true : y % 100 === 0 ? false : y % 4 === 0;

console.log(isLeap(+input()) ? "YES" : "NO");
