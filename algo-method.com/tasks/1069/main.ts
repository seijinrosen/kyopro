import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const int2bin = (num: number, width: number): string =>
  num.toString(2).padStart(width, "0");

const X = input().split(" ").map(Number);

const getSquare = (binX: string, j: number): string => {
  if (binX[2 * j] === "0" && binX[2 * j + 1] === "0") return ".";
  if (binX[2 * j] === "0" && binX[2 * j + 1] === "1") return "o";
  return "x";
};

const getLine = (x: number): string => {
  const binX = int2bin(x, 16);
  return [...Array(8)].map((_, j) => getSquare(binX, j)).join("");
};

const ans = X.map(getLine);
print(ans.join("\n"));
