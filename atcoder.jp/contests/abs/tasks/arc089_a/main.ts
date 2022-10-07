import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const even = (n: number) => n % 2 === 0;
const pairwise = <T>(array: T[]) => zip(array, array.slice(1));
const yesNo = (b: boolean | number) => (b ? "Yes" : "No");
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

// input functions -------------------------------------------------------------
const inputTupleArray = (n: number) =>
  [...Array(n)].map(
    () => input().split(" ").map(Number) as [number, number, number]
  );
// input functions -------------------------------------------------------------

type Info = [number, number, number];

const ok = ([[t1, x1, y1], [t2, x2, y2]]: [Info, Info]): boolean => {
  const time = t2 - t1 - Math.abs(x2 - x1) - Math.abs(y2 - y1);
  return 0 <= time && even(time);
};

const main = () => {
  const N = +input();
  const TXY = inputTupleArray(N);

  const ans = pairwise([[0, 0, 0] as Info, ...TXY]).every(ok);

  print(yesNo(ans));
};

main();
