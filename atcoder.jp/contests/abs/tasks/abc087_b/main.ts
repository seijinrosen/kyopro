import { readFileSync } from "fs";
let inputLinesIndex = 0;
const inputLines = readFileSync("/dev/stdin", "utf8").split("\n");
const input = () => inputLines[inputLinesIndex++];
const print = (...messages: any) => console.log(...messages);

const count = <T>(x: string | T, iterable: string | T[]) =>
  typeof iterable === "string"
    ? iterable.split("").filter((a) => a === x).length
    : iterable.filter((a) => a === x).length;
const range = (a: number, b?: number) =>
  b ? [...Array(b - a)].map((_, i) => a + i) : [...Array(a)].map((_, i) => i);

const main = () => {
  const A = +input();
  const B = +input();
  const C = +input();
  const X = +input();

  const ans = count(
    X,
    range(A + 1).flatMap((a) =>
      range(B + 1).flatMap((b) =>
        range(C + 1).flatMap((c) => 500 * a + 100 * b + 50 * c)
      )
    )
  );

  print(ans);
};

main();
