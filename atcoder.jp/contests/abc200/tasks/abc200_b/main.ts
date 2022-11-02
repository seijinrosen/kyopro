import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

function* iterate<T>(func: (arg: T) => T, start: T) {
  while (true) {
    yield start;
    start = func(start);
  }
}

const nth = <T>(iterable: Generator<T, void, unknown>, n: number) => {
  for (let i = 0; i < n; i++) iterable.next();
  return iterable.next().value;
};

const func = (n: number) => (n % 200 === 0 ? n / 200 : 1000 * n + 200);

const main = () => {
  const [N, K] = input().split(" ").map(Number);

  const ans = nth(iterate(func, N), K);
  console.log(ans);
};

main();
