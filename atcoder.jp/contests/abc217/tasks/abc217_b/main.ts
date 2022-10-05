import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

// https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Set#基本的な集合演算の実装
const difference = <T>(setA: Set<T>, setB: Set<T>) => {
  const _difference = new Set(setA);
  for (const elem of setB) _difference.delete(elem);
  return _difference;
};

const range = (a: number, b?: number) =>
  b ? [...Array(b - a)].map((_, i) => a + i) : [...Array(a)].map((_, i) => i);

const main = () => {
  const S = range(3).map(() => input());

  const contests = new Set(["ABC", "ARC", "AGC", "AHC"]);
  const ans = difference(contests, new Set(S));

  print(...ans);
};

main();
