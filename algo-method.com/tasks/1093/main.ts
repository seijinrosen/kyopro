import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const sum = (array: number[]) => array.reduce((a, b) => a + b, 0);

type Tuple = [number, number, number, number];
const inputTupleArray = (n: number) =>
  [...Array(n)].map(() => input().split(" ").map(Number) as Tuple);

const subtractBreakTime = (m: number): number => {
  if (m <= 360) return m;
  if (m <= 480) return m - 45;
  return m - 60;
};

const func = ([sh, sm, eh, em]: Tuple): number =>
  subtractBreakTime(60 * (eh - sh) + em - sm);

const main = () => {
  const INFO = inputTupleArray(30);

  const totalMinutes = sum(INFO.map(func));
  const h = Math.floor(totalMinutes / 60);
  const m = totalMinutes % 60;

  console.log(h, m);
};

main();
