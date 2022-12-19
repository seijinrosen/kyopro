import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const sort = <T extends number | bigint>(array: T[], reverse = false) =>
  reverse
    ? array.slice().sort((a, b) => (a > b ? -1 : a < b ? 1 : 0))
    : array.slice().sort((a, b) => (a < b ? -1 : a > b ? 1 : 0));

// https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Set#基本的な集合演算の実装
const symmetricDifference = <T>(setA: Set<T>, setB: Set<T>) => {
  const _difference = new Set(setA);
  for (const elem of setB)
    if (_difference.has(elem)) _difference.delete(elem);
    else _difference.add(elem);
  return _difference;
};

input();
const A = input().split(" ").map(Number);
const B = input().split(" ").map(Number);

const ans = sort([...symmetricDifference(new Set(A), new Set(B))]);
console.log(ans.join(" "));
