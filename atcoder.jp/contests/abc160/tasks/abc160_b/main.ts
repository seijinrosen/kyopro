import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const X = +input();

const coin500 = Math.floor(X / 500);
const coin5 = Math.floor((X % 500) / 5);

const ans = 1000 * coin500 + 5 * coin5;
print(ans);
