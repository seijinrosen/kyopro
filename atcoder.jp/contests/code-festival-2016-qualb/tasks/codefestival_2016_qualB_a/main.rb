# frozen_string_literal: true

S = gets.chomp
T = 'CODEFESTIVAL2016'

ans = 0
(0...S.size).each do |i|
  ans += 1 if S[i] != T[i]
end

p ans
