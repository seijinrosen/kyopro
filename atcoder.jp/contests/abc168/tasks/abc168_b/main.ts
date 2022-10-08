import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const take = (n: number, s: string) => s.slice(0, n);

const main = () => {
  const K = +input();
  const S = input();

  const ans = S.length <= K ? S : take(K, S) + "...";

  print(ans);
};

main();
