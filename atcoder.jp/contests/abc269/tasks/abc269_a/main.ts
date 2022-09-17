import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const [A, B, C, D] = input().split(" ").map(Number);

const ans = (A + B) * (C - D);

print(ans.toString());
print("Takahashi");
