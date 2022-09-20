import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const sorted = <T extends number | bigint>(array: T[]) =>
  array.sort((a, b) => (a < b ? -1 : a > b ? 1 : 0));

const [N, M] = sorted(input().split(" ").map(BigInt));

const f = (n: bigint, m: bigint) => {
  if (n === 1n) return m === 1n ? 1n : m - 2n;
  return (n - 2n) * (m - 2n);
};

const ans = f(N, M);
print(ans.toString());
