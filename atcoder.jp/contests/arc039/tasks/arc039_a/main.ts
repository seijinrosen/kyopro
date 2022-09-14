import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const [A, B] = input().split(" ");

const maxA = (a: string): number => {
  if (a[0] != "9") return +("9" + a[1] + a[2]);
  if (a[1] != "9") return +(a[0] + "9" + a[2]);
  return +(a[0] + a[1] + "9");
};

const minB = (b: string): number => {
  if (b[0] != "1") return +("1" + b[1] + b[2]);
  if (b[1] != "0") return +(b[0] + "0" + b[2]);
  return +(b[0] + b[1] + "0");
};

const ans = Math.max(maxA(A) - +B, +A - minB(B));
print(ans);
