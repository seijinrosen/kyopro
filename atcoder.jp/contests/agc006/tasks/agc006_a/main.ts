import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const tails = (str: string): string[] =>
  [...Array(str.length + 1)].map((_, i) => str.slice(i));

const N = +input();
const S = input();
const T = input();

const ans = tails(S).findIndex((tail) => T.startsWith(tail)) + N;
print(ans);
