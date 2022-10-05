import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const asciiLowercase = "abcdefghijklmnopqrstuvwxyz";

const Counter = <T>(arr: T[]) => {
  const counter = new Map<T, number>();
  for (const v of arr) counter.set(v, (counter.get(v) || 0) + 1);
  return counter;
};
const combinations3 = <T>(array: T[]): [T, T, T][] => {
  const n = array.length;
  const ret: [T, T, T][] = [];
  for (let i = 0; i < n - 2; i++)
    for (let j = i + 1; j < n - 1; j++)
      for (let k = j + 1; k < n; k++) ret.push([array[i], array[j], array[k]]);
  return ret;
};
const count = (x: string, s: string) =>
  s.split("").filter((c) => c === x).length;
const enumerate = <T>(array: T[]): [number, T][] => array.map((v, i) => [i, v]);
const runLengthEncoding = (str: string): [string, number][] => {
  const ret: [string, number][] = [[str[0], 1]];
  for (const c of str.slice(1)) {
    if (c === ret[ret.length - 1][0]) ret[ret.length - 1][1]++;
    else ret.push([c, 1]);
  }
  return ret;
};
const int2bin = (num: number, width: number): string =>
  num.toString(2).padStart(width, "0");
const isOdd = (n: number): boolean => n % 2 === 1;
const last = <T>(array: T[]): T => array[array.length - 1];
const max = (data: number[]) => data.reduce((a, b) => Math.max(a, b));
const pairwise = <T>(array: T[]) => zip(array, array.slice(1));
// https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Array/from#連番の生成_範囲指定
// const range = (start: number, stop: number, step = 1) =>
//   Array.from({ length: (stop - start) / step + 1 }, (_, i) => start + i * step);
const range = (a: number, b?: number): number[] =>
  b ? [...Array(b - a)].map((_, i) => a + i) : [...Array(a)].map((_, i) => i);
const reverse = (s: string) => s.split("").reverse().join("");
// https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/BigInt#比較演算
const sorted = <T extends number | bigint>(array: T[]) =>
  array.slice().sort((a, b) => (a < b ? -1 : a > b ? 1 : 0));
const sum = (array: number[]): number => array.reduce((a, b) => a + b, 0);
const takeWhile = <T>(predicate: (a: T) => boolean, array: T[]): T[] => {
  const ret: T[] = [];
  for (const a of array)
    if (predicate(a)) ret.push(a);
    else break;
  return ret;
};
const tails = (str: string): string[] =>
  [...Array(str.length + 1)].map((_, i) => str.slice(i));
const yesNo = (b: boolean | number) => (b ? "Yes" : "No");
// const zip = <T1, T2>(a: T1[], b: T2[]): [T1, T2][] =>
//   [...Array(Math.min(a.length, b.length))].map((_, i) => [a[i], b[i]]);
const zip: {
  (a: string, b: string): [string, string][];
  <B>(a: string, b: B[]): [string, B][];
  <A>(a: A[], b: string): [A, string][];
  <A, B>(a: A[], b: B[]): [A, B][];
} = <A, B>(a: string | A[], b: string | B[]) =>
  typeof a === "string" && typeof b === "string"
    ? [...Array(Math.min(a.length, b.length))].map(
        (_, i) => [a[i], b[i]] as [string, string]
      )
    : typeof a === "string" && typeof b !== "string"
    ? [...Array(Math.min(a.length, b.length))].map(
        (_, i) => [a[i], b[i]] as [string, B]
      )
    : typeof a !== "string" && typeof b === "string"
    ? [...Array(Math.min(a.length, b.length))].map(
        (_, i) => [a[i], b[i]] as [A, string]
      )
    : [...Array(Math.min(a.length, b.length))].map(
        (_, i) => [a[i], b[i]] as [A, B]
      );

// input functions -------------------------------------------------------------
const inputNumberArray = (): number[] => input().split(" ").map(Number);
const inputPairArray = (n: number) =>
  [...Array(n)].map(() => input().split(" ").map(Number) as [number, number]);
// input functions -------------------------------------------------------------

const main = () => {
  const N = +input();
};

main();
