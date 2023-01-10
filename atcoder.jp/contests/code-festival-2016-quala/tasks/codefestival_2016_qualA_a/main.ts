import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const s = input();

const ans = s.slice(0, 4) + " " + s.slice(4);

console.log(ans);
