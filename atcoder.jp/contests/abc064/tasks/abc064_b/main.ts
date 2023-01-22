import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const max = <T extends number | bigint>(array: T[]) =>
  array.reduce((a, b) => (a < b ? b : a));
const min = <T extends number | bigint>(array: T[]) =>
  array.reduce((a, b) => (a < b ? a : b));

input();
const A = input().split(" ").map(Number);

const ans = max(A) - min(A);

console.log(ans);
