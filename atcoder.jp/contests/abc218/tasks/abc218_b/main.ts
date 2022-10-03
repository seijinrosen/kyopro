import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const asciiLowercase = "abcdefghijklmnopqrstuvwxyz";

// input functions -------------------------------------------------------------
const inputNumberArray = (): number[] => input().split(" ").map(Number);
// input functions -------------------------------------------------------------

const main = () => {
  const P = inputNumberArray();

  const ans = P.map((p) => asciiLowercase[p - 1]);
  print(ans.join(""));
};

main();
