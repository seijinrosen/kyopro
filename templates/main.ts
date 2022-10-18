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
const accumulate = (array: number[]) => {
  let now = 0;
  return array.map((v) => (now += v));
};
const accumulateMax = (array: number[]) => {
  let now = -Infinity;
  return array.map((v) => (now = Math.max(now, v)));
};
const bin2int = (b: string) => parseInt(b, 2);
const combinations3 = <T>(array: T[]): [T, T, T][] => {
  const n = array.length;
  const ret: [T, T, T][] = [];
  for (let i = 0; i < n - 2; i++)
    for (let j = i + 1; j < n - 1; j++)
      for (let k = j + 1; k < n; k++) ret.push([array[i], array[j], array[k]]);
  return ret;
};
const count: {
  (x: string, iterable: string): number;
  <T>(x: T, iterable: T[]): number;
} = <T>(x: string | T, iterable: string | T[]) =>
  typeof iterable === "string"
    ? iterable.split("").filter((a) => a === x).length
    : iterable.filter((a) => a === x).length;
const countIf = <T>(p: (x: T) => boolean, xs: T[]) => xs.filter(p).length;
// https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Set#基本的な集合演算の実装
const difference = <T>(setA: Set<T>, setB: Set<T>) => {
  const _difference = new Set(setA);
  for (const elem of setB) _difference.delete(elem);
  return _difference;
};
const enumerate = <T>(array: T[], start: number = 0): [number, T][] =>
  array.map((v, i) => [start + i, v]);
const even = (n: number) => n % 2 === 0;
const fst = <T>(x: [T, any]) => x[0];
const gcd = (x: number, y: number): number => (y === 0 ? x : gcd(y, x % y));
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
const odd = (n: number) => n % 2 === 1;
const last = <T>(array: T[]): T => array[array.length - 1];
const max = (array: number[]) => array.reduce((a, b) => Math.max(a, b));
const min = (array: number[]) => array.reduce((a, b) => Math.min(a, b));
const pairwise = <T>(array: T[]) => zip(array, array.slice(1));
const prime_factorize = (n: number) => {
  const counter = new Map<number, number>();
  let p = 2;
  while (p * p <= n) {
    let e = 0;
    while (n % p === 0) {
      e++;
      n /= p;
    }
    if (e !== 0) counter.set(p, e);
    p++;
  }
  if (n !== 1) counter.set(n, 1);
  return counter;
};
// https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/Array/from#連番の生成_範囲指定
// const range = (start: number, stop: number, step = 1) =>
//   Array.from({ length: (stop - start) / step + 1 }, (_, i) => start + i * step);
const range = (a: number, b?: number) =>
  b ? [...Array(b - a)].map((_, i) => a + i) : [...Array(a)].map((_, i) => i);
const reverse = (s: string) => s.split("").reverse().join("");
// https://developer.mozilla.org/ja/docs/Web/JavaScript/Reference/Global_Objects/BigInt#比較演算
const sort = <T extends number | bigint>(array: T[], reverse = false) =>
  reverse
    ? array.slice().sort((a, b) => (a > b ? -1 : a < b ? 1 : 0))
    : array.slice().sort((a, b) => (a < b ? -1 : a > b ? 1 : 0));
const step2 = <T>(array: T[]) => array.filter((_, i) => i % 2 === 0);
const sum = (array: number[]) => array.reduce((a, b) => a + b, 0);
const sumOfEachDigit = (i: number) => sum(i.toString().split("").map(Number));
const take = (n: number, s: string) => s.slice(0, n);
const takeWhile = <T>(predicate: (a: T) => boolean, array: T[]): T[] => {
  const ret: T[] = [];
  for (const a of array)
    if (predicate(a)) ret.push(a);
    else break;
  return ret;
};
const tail = <T>(array: T[]) => array.slice(1);
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
type Pair = [number, number];
type Tuple = [number, number, number];
const inputNumberArray = () => input().split(" ").map(Number);
const inputPairArray = (n: number) =>
  [...Array(n)].map(() => input().split(" ").map(Number) as Pair);
const inputTupleArray = (n: number) =>
  [...Array(n)].map(() => input().split(" ").map(Number) as Tuple);
// input functions -------------------------------------------------------------

const main = () => {
  const N = +input();
};

main();
