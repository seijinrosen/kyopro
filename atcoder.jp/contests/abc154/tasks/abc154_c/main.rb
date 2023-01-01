# frozen_string_literal: true

N = gets.to_i
A = gets.split.map(&:to_i)

ans = A.uniq.size == N

puts ans ? 'YES' : 'NO'
