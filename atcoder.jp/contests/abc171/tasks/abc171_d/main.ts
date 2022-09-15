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

const inputPairArray = (n: number) =>
  [...Array(n)].map(() => input().split(" ").map(Number) as [number, number]);

const N = +input();
const A = input().split(" ").map(Number);
const Q = +input();
const BC = inputPairArray(Q);

let s = sum(A);
const counter = Counter(A);

const ansArray = BC.map(([b, c]) => {
  s += (c - b) * (counter.get(b) || 0);
  counter.set(c, (counter.get(c) || 0) + (counter.get(b) || 0));
  counter.set(b, 0);
  return s;
});

print(ansArray.join("\n"));
