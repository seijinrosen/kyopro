import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const S = input();

const arr: string[] = [];

for (const s of S) {
  if (s in ["0", "1"]) arr.push(s);
  else if (s === "B" && arr) arr.pop();
}

print(arr.join(""));
