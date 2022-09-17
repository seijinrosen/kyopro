import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const [N, K] = input().split(" ").map(Number);
const P = input().split(" ").map(Number);

const bucket: boolean[] = Array(N + 1).fill(false);
for (const p of P.slice(0, K)) bucket[p] = true;

let idx = bucket.indexOf(true);
const ansArray = [idx];

for (const p of P.slice(K)) {
  if (idx < p) {
    bucket[p] = true;
    idx = bucket.indexOf(true, idx + 1);
  }
  ansArray.push(idx);
}

print(ansArray.join("\n"));
