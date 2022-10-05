import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const min = (array: number[]) => array.reduce((a, b) => Math.min(a, b));
const prime_factorize = (n: number) => {
  const counter = new Map<number, number>();
  let p = 2;
  while (p * p <= n) {
    let e = 0;
    while (n % p === 0) {
      e++;
      n /= p;
    }
    if (e !== 0) counter.set(p, e);
    p++;
  }
  if (n !== 1) counter.set(n, 1);
  return counter;
};

// input functions -------------------------------------------------------------
const inputNumberArray = (): number[] => input().split(" ").map(Number);
// input functions -------------------------------------------------------------

const main = () => {
  const N = +input();
  const A = inputNumberArray();

  const ans = min(A.map((a) => prime_factorize(a).get(2) || 0));
  print(ans);
};

main();
