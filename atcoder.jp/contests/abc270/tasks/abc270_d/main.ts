import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const max = (data: number[]) => data.reduce((a, b) => Math.max(a, b));
const range = (a: number, b?: number): number[] =>
  b ? [...Array(b - a)].map((_, i) => a + i) : [...Array(a)].map((_, i) => i);
const takeWhile = <T>(predicate: (a: T) => boolean, array: T[]): T[] => {
  const ret: T[] = [];
  for (const a of array)
    if (predicate(a)) ret.push(a);
    else break;
  return ret;
};

const [N, K] = input().split(" ").map(Number);
const A = input().split(" ").map(Number);

const dp = range(N + 1).fill(0);

for (const n of range(1, N + 1))
  dp[n] = max(takeWhile((a) => a <= n, A).map((a) => n - dp[n - a]));

const ans = dp[N];
print(ans);
