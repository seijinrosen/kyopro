import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const relu = (x: number) => (x >= 0 ? x : 0);

const x = +input();

console.log(relu(x));
