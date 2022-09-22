import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const yesNo = (b: boolean) => (b ? "Yes" : "No");
const sum = (data: number[]) => data.reduce((a, b) => a + b, 0);
const reverse = (s: string) => s.split("").reverse().join("");
const zip = <T1, T2>(a: T1[], b: T2[]): [T1, T2][] =>
  [...Array(Math.min(a.length, b.length))].map((_, i) => [a[i], b[i]]);
const pairwise = <T>(array: T[]) => zip(array, array.slice(1));
const Counter = <T>(arr: T[]) => {
  const counter = new Map<T, number>();
  for (const v of arr) counter.set(v, (counter.get(v) || 0) + 1);
  return counter;
};

// https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Array/from#連番の生成_範囲指定
const range = (start: number, stop: number, step = 1) =>
  Array.from({ length: (stop - start) / step + 1 }, (_, i) => start + i * step);

// https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/BigInt#比較演算
const sorted = <T extends number | bigint>(array: T[]) =>
  array.sort((a, b) => (a < b ? -1 : a > b ? 1 : 0));

const inputPairArray = (n: number) =>
  [...Array(n)].map(() => input().split(" ").map(Number) as [number, number]);

const N = +input();
