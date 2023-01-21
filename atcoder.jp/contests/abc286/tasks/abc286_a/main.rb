# frozen_string_literal: true

# @return [Array(Integer)]
def input_int_array
  gets.split.map(&:to_i)
end

N, P, Q, R, S = input_int_array
A = input_int_array

A[P - 1...Q], A[R - 1...S] = A[R - 1...S], A[P - 1...Q]

puts A.join ' '
