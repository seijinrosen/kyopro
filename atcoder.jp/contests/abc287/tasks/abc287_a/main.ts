import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const N = +input();
const S = [...Array(N)].map(() => input());

const ans = N / 2 < S.filter((s) => s === "For").length;

console.log(ans ? "Yes" : "No");
