import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const sort = <T extends number | bigint>(array: T[], reverse = false) =>
  reverse
    ? array.slice().sort((a, b) => (a > b ? -1 : a < b ? 1 : 0))
    : array.slice().sort((a, b) => (a < b ? -1 : a > b ? 1 : 0));
const sum = (array: number[]) => array.reduce((a, b) => a + b, 0);

const [_N, K] = input().split(" ").map(Number);
const H = input().split(" ").map(Number);

const ans = sum(sort(H, true).slice(K));

console.log(ans);
