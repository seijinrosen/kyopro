import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const sum = (data: number[]) => data.reduce((a, b) => a + b);

const N = +input();

const MOD = 998244353;
const dp: number[][] = [...Array(N)].map(() => Array(10).fill(0));
dp[0] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1];

const plusMod = (x: number, y: number) => (x + y) % MOD;

for (let i = 0; i < N - 1; i++) {
  for (let x = 1; x <= 9; x++) {
    dp[i + 1][x] = plusMod(dp[i + 1][x], dp[i][x]);
    if (x != 1) dp[i + 1][x - 1] = plusMod(dp[i + 1][x - 1], dp[i][x]);
    if (x != 9) dp[i + 1][x + 1] = plusMod(dp[i + 1][x + 1], dp[i][x]);
  }
}

const ans = sum(dp[N - 1]) % MOD;
print(ans);
