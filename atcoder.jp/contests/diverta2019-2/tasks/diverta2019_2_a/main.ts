import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const main = () => {
  const [N, K] = input().split(" ").map(Number);

  const ans = K === 1 ? 0 : N - K;
  console.log(ans);
};

main();
