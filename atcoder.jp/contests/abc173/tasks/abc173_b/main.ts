import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const Counter = <T>(arr: T[]) => {
  const counter = new Map<T, number>();
  for (const v of arr) counter.set(v, (counter.get(v) || 0) + 1);
  return counter;
};
const range = (a: number, b?: number) =>
  b ? [...Array(b - a)].map((_, i) => a + i) : [...Array(a)].map((_, i) => i);

const main = () => {
  const N = +input();
  const S = range(N).map(() => input());

  const counter = Counter(S);
  const results = ["AC", "WA", "TLE", "RE"];

  for (const r of results) {
    console.log(r, "x", counter.get(r) || 0);
  }
};

main();
