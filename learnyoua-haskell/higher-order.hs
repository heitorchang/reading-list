mySum :: (Num a) => [a] -> a
mySum = foldl (+) 0