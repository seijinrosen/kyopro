import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const [N, M] = input().split(" ").map(Number);

const arr = [
  "1110111",
  "0100100",
  "1011101",
  "1101101",
  "0101110",
  "1101011",
  "1111011",
  "0100111",
  "1111111",
  "1101111",
];

const ans = parseInt(arr[N], 2) ^ parseInt(arr[M], 2);
print(ans);
