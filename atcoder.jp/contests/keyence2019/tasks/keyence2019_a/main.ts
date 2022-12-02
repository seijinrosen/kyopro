import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const main = () => {
  const N = input().split(" ");

  const ans = N.sort().join("") === "1974".split("").sort().join("");
  console.log(ans ? "YES" : "NO");
};

main();
