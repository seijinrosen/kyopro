import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const main = () => {
  input();
  const S = input();
  const K = +input();

  const ans = S.split("")
    .map((c) => (c === S[K - 1] ? c : "*"))
    .join("");
  console.log(ans);
};

main();
