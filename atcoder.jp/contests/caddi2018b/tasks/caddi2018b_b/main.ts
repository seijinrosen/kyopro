import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const [N, H, W] = input().split(" ").map(Number);
const AB = [...Array(N)].map(
  () => input().split(" ").map(Number) as [number, number]
);

const ans = AB.filter(([a, b]) => H <= a && W <= b).length;
console.log(ans);
