# frozen_string_literal: true

X, Y, Z = gets.split.map(&:to_i)

ans = (X - Z) / (Y + Z)

p ans
