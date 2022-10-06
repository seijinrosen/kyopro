import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const range = (a: number, b?: number) =>
  b ? [...Array(b - a)].map((_, i) => a + i) : [...Array(a)].map((_, i) => i);

const main = () => {
  const N = +input();
  const D = range(N).map(() => +input());

  const ans = new Set(D).size;

  print(ans);
};

main();
