# frozen_string_literal: true

require 'set'

N, M = gets.split.map(&:to_i)
S = Array.new(N) { gets.chomp }
T = Array.new(M) { gets.chomp }

st = Set.new(T)
ans = S.count { |s| st.include? s.slice(3, 3) }

p ans
