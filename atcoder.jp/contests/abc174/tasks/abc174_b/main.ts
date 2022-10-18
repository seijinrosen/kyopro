import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const countIf = <T>(p: (x: T) => boolean, xs: T[]) => xs.filter(p).length;
const inputNumberArray = () => input().split(" ").map(Number);

const main = () => {
  const [N, D] = inputNumberArray();
  const XY = [...Array(N)].map(() => inputNumberArray() as [number, number]);

  const ans = countIf(([x, y]) => x ** 2 + y ** 2 <= D ** 2, XY);
  console.log(ans);
};

main();
