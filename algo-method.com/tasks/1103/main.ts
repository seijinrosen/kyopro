import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const [N, K] = input().split(" ").map(Number);
const X = input().split(" ").map(Number);

const func = (minDist: number): boolean => {
  let k = 1;
  let now = X[0];
  for (const x of X.slice(1)) {
    if (minDist <= x - now) {
      if (++k === K) return true;
      now = x;
    }
  }
  return false;
};

let lo = 1;
let hi = 10 ** 10;
while (hi - lo > 1) {
  const mid = Math.floor((hi + lo) / 2);
  if (func(mid)) lo = mid;
  else hi = mid;
}

const ans = lo;
print(ans);
