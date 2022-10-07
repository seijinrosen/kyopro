import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const int2bin = (num: number, width: number): string =>
  num.toString(2).padStart(width, "0");

const main = () => {
  const N = +input();

  const ans = int2bin(N, 10);

  print(ans);
};

main();
