import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const enumerate = <T>(array: T[]): [number, T][] => array.map((v, i) => [i, v]);
const range = (a: number, b?: number): number[] =>
  b ? [...Array(b - a)].map((_, i) => a + i) : [...Array(a)].map((_, i) => i);
const yesNo = (b: boolean | number) => (b ? "Yes" : "No");

const [N, M] = input().split(" ").map(Number);
const W = input().split(" ").map(Number);

const dp = range(N + 1).map(() =>
  range(M + 1).map(() => [false, false] as [boolean, boolean])
);
dp[0][0][0] = true;

for (const [i, w] of enumerate(W)) {
  for (const j of range(M + 1)) {
    for (const k of [0, 1]) {
      if (dp[i][j][k]) dp[i + 1][j][k] = true;
      if (j + w <= M && dp[i][j][k]) dp[i + 1][j + w][k ^ 1] = true;
    }
  }
}

const ans = dp[N][M][1];
print(yesNo(ans));
