import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const sum = (data: number[]) => data.reduce((a, b) => a + b);
const Counter = <T>(arr: T[]) => {
  const counter = new Map<T, number>();
  for (const v of arr) counter.set(v, (counter.get(v) || 0) + 1);
  return counter;
};

const N = +input();
const A = input().split(" ").map(Number);

const nC2 = (n: number) => (n < 2 ? 0 : (n * (n - 1)) / 2);

const counter = Counter(A);
const total = sum([...counter.values()].map(nC2));

const ansArray = A.map(
  (a) => total - nC2(counter.get(a)!) + nC2(counter.get(a)! - 1)
);

print(ansArray.join("\n"));
