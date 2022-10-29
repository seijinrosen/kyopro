import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const main = () => {
  const N = +input();
  const S = input();

  const m = Math.floor(N / 2);
  const ans = S.slice(0, m) === S.slice(m);

  console.log(ans ? "Yes" : "No");
};

main();
