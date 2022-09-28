import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const yesNo = (b: boolean | number) => (b ? "Yes" : "No");

const N = +input();
const A = input()
  .split(" ")
  .map((x) => +x - 1);

const bucket: boolean[] = Array(N).fill(false);

let ans = true;
for (const a of A) {
  if (bucket[a]) {
    ans = false;
    break;
  }
  bucket[a] = true;
}

print(yesNo(ans));
