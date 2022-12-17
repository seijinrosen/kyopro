import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const asciiUppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

console.log(asciiUppercase.slice(0, +input()));
