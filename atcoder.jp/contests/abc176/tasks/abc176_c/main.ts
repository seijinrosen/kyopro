import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];

const scanl1 = <T>(func: (a: T, b: T) => T, array: T[]) => {
  const ret = [array[0]];
  array.reduce((a, b) => {
    const x = func(a, b);
    ret.push(x);
    return x;
  });
  return ret;
};
const sum = (array: number[]) => array.reduce((a, b) => a + b, 0);
const zip: {
  (a: string, b: string): [string, string][];
  <B>(a: string, b: B[]): [string, B][];
  <A>(a: A[], b: string): [A, string][];
  <A, B>(a: A[], b: B[]): [A, B][];
} = <A, B>(a: string | A[], b: string | B[]) =>
  typeof a === "string" && typeof b === "string"
    ? [...Array(Math.min(a.length, b.length))].map(
        (_, i) => [a[i], b[i]] as [string, string]
      )
    : typeof a === "string" && typeof b !== "string"
    ? [...Array(Math.min(a.length, b.length))].map(
        (_, i) => [a[i], b[i]] as [string, B]
      )
    : typeof a !== "string" && typeof b === "string"
    ? [...Array(Math.min(a.length, b.length))].map(
        (_, i) => [a[i], b[i]] as [A, string]
      )
    : [...Array(Math.min(a.length, b.length))].map(
        (_, i) => [a[i], b[i]] as [A, B]
      );

const main = () => {
  const N = +input();
  const A = input().split(" ").map(Number);

  const accMax = scanl1(Math.max, A);
  const ans = sum(zip(accMax, A).map(([a, b]) => a - b));

  console.log(ans);
};

main();
