import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const countSerialChar = (str: string): [string, number][] => {
  const ret: [string, number][] = [[str[0], 1]];
  for (const c of str.slice(1)) {
    if (c === ret[ret.length - 1][0]) ret[ret.length - 1][1]++;
    else ret.push([c, 1]);
  }
  return ret;
};
const isOdd = (n: number): boolean => n % 2 === 1;
const last = <T>(array: T[]): T => array[array.length - 1];
const sum = (array: number[]): number => array.reduce((a, b) => a + b, 0);

const S = input();
const K = +input();

const counter = countSerialChar(S);
let ans = sum(counter.map(([, v]) => Math.floor(v / 2))) * K;

if (counter.length === 1 && isOdd(counter[0][1])) {
  ans += Math.floor(K / 2);
} else if (
  counter[0][0] === last(counter)[0] &&
  isOdd(counter[0][1]) &&
  isOdd(last(counter)[1])
) {
  ans += K - 1;
}

print(ans);
