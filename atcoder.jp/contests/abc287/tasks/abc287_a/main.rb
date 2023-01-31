# frozen_string_literal: true

N = gets.to_i
S = Array.new(N) { gets.chomp }

ans = N / 2 < S.count('For')

puts ans ? 'Yes' : 'No'
