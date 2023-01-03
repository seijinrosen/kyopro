# frozen_string_literal: true

require 'set'

N = gets.to_i
S = Array.new(N) { gets.chomp }

ans = Set.new(S).size

p ans
