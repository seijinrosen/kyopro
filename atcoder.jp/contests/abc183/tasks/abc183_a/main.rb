# frozen_string_literal: true

def relu(x)
  x >= 0 ? x : 0
end

x = gets.to_i

p relu x
