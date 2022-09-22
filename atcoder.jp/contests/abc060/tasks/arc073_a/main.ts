import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const sum = (data: number[]) => data.reduce((a, b) => a + b, 0);
const zip = <T1, T2>(a: T1[], b: T2[]): [T1, T2][] =>
  [...Array(Math.min(a.length, b.length))].map((_, i) => [a[i], b[i]]);
const pairwise = <T>(array: T[]) => zip(array, array.slice(1));

const [N, T] = input().split(" ").map(Number);
const T_LIST = input().split(" ").map(Number);

const ans = sum(pairwise(T_LIST).map(([a, b]) => Math.min(T, b - a))) + T;
print(ans);
