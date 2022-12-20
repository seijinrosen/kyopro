import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const max = <T extends number | bigint>(array: T[]) =>
  array.reduce((a, b) => (a < b ? b : a));
const min = <T extends number | bigint>(array: T[]) =>
  array.reduce((a, b) => (a < b ? a : b));

const [A, B, C, D] = input().split(" ").map(BigInt);
console.log(max([A, C]) <= min([B, D]) ? "Yes" : "No");
