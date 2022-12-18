import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const N = +input();
const H = +input();
const W = +input();

const h = N - H + 1;
const w = N - W + 1;

console.log(h * w);
