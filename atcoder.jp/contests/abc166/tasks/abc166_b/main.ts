import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const [N, K] = input().split(" ").map(Number);

const st = new Set();

for (let _ = 0; _ < K; _++) {
  input();
  const A = input().split(" ").map(Number);

  for (const a of A) st.add(a);
}

const ans = N - st.size;

console.log(ans);
