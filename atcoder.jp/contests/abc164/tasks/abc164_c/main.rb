# frozen_string_literal: true

require 'set'

N = gets.to_i
S = N.times.map { gets.chomp }

ans = Set.new(S).size

p ans
